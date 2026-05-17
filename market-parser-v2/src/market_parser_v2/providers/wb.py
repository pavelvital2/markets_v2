"""WB provider migration behind the V2 provider boundary.

The implementation is intentionally offline: it accepts fixture/mocked rows that
match audited WB V1 contracts, writes V2 runtime artifacts, and normalizes common
marts/export data without invoking Wildberries or reading cookies.
"""

from __future__ import annotations

import csv
import json
import shutil
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.constants import MART_FIELDS, SCHEMA_VERSION
from market_parser_v2.core.contracts import COMMON_MART_SCHEMAS, normalize_source_system, validate_mart_rows
from market_parser_v2.core.export import ExportSkeletonResult, create_export_bundle
from market_parser_v2.core.quality import map_source_status, summarize_data_quality
from market_parser_v2.core.run import new_run_id
from market_parser_v2.providers.base import ProviderPlan


WB_COMPONENTS = ("suggest", "filter", "serp", "sellers", "export")
WB_SOURCE_ALIAS = "wildberries"

SUGGEST_RAW_FIELDS = (
    "run_id",
    "component",
    "collected_at_utc",
    "source_system",
    "source_type",
    "source_ref",
    "status",
    "error_message",
    "base_prefix",
    "typed_query",
    "letter",
    "depth",
    "position",
    "list_size",
    "suggestion",
    "marketplace",
    "schema_version",
    "data_quality_status",
)
SUGGEST_STAGING_FIELDS = SUGGEST_RAW_FIELDS + ("suggestion_lc", "is_empty_suggestion")

FILTER_TOP_FIELDS = (
    "run_id",
    "component",
    "rank",
    "query",
    "query_group",
    "niche",
    "normalized_query",
    "canonical_query",
    "source_query",
    "hybrid_score",
    "score_suggest",
    "score_wordstat",
    "wordstat_volume",
    "count",
    "selected_reason",
    "collected_at_utc",
    "source_system",
    "source_type",
    "source_ref",
    "status",
    "error_message",
    "marketplace",
    "schema_version",
    "data_quality_status",
)

SERP_PRODUCT_FIELDS = (
    "run_id",
    "component",
    "collected_at_utc",
    "source_system",
    "source_type",
    "source_ref",
    "status",
    "error_message",
    "query",
    "query_group",
    "page",
    "position_on_page",
    "absolute_position",
    "nmId",
    "imtId",
    "product_name",
    "brand",
    "brandId",
    "supplier_id",
    "supplier_name",
    "final_price",
    "price",
    "sale_price",
    "discount",
    "sale",
    "rating",
    "feedbacks",
    "valuation",
    "total_quantity",
    "promo_markers",
    "raw_file",
    "raw_page_path",
    "marketplace",
    "schema_version",
    "data_quality_status",
)

SELLER_FIELDS = (
    "run_id",
    "component",
    "collected_at_utc",
    "source_system",
    "source_type",
    "source_ref",
    "status",
    "error_message",
    "supplier_id",
    "supplier_name",
    "rating",
    "valuation",
    "feedbacks_count",
    "sale_item_quantity",
    "registration_date",
    "update_date",
    "delivery_duration",
    "supp_ratio",
    "ratio_mark_supp",
    "rating_is_invisible",
    "http_status",
    "query_count",
    "product_count",
    "queries_ref",
    "query_groups_ref",
    "nm_ids_ref",
    "source_product_run_ids",
    "raw_file",
    "marketplace",
    "schema_version",
    "data_quality_status",
)

BRIDGE_FIELDS = (
    "run_id",
    "component",
    "collected_at_utc",
    "source_system",
    "source_type",
    "source_ref",
    "status",
    "error_message",
    "supplier_id",
    "supplier_name",
    "query",
    "query_group",
    "nmId",
    "product_run_id",
    "marketplace",
    "schema_version",
    "data_quality_status",
)


@dataclass(frozen=True)
class WbFixtureInput:
    suggest_rows: tuple[dict[str, Any], ...] = ()
    filter_rows: tuple[dict[str, Any], ...] = ()
    product_rows: tuple[dict[str, Any], ...] = ()
    seller_rows: tuple[dict[str, Any], ...] = ()
    bridge_rows: tuple[dict[str, Any], ...] = ()
    component_statuses: dict[str, str] = field(default_factory=dict)
    errors: tuple[str, ...] = ()


@dataclass(frozen=True)
class WbProviderRunResult:
    run_id: str
    status: str
    report_usability: str
    provider_files: dict[str, str]
    common_mart_files: dict[str, str]
    latest_files: dict[str, str]
    checkpoint_path: Path
    run_report_path: Path
    latest_run_report_path: Path
    export_result: ExportSkeletonResult

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "status": self.status,
            "report_usability": self.report_usability,
            "provider_files": self.provider_files,
            "common_mart_files": self.common_mart_files,
            "latest_files": self.latest_files,
            "checkpoint_path": str(self.checkpoint_path),
            "run_report_path": str(self.run_report_path),
            "latest_run_report_path": str(self.latest_run_report_path),
            "export": self.export_result.to_dict(),
        }


class WbProvider:
    provider_id = "wb"
    marketplace = "wb"

    def build_plan(self) -> ProviderPlan:
        return ProviderPlan(
            provider_id=self.provider_id,
            marketplace=self.marketplace,
            components=WB_COMPONENTS,
            live_scraping_enabled=False,
            status="ready_offline_fixture",
            notes=(
                "WB fixture/mocked migration path is implemented",
                "live marketplace collection is intentionally disabled",
                "common marts and export normalize wildberries source identity to wb",
            ),
        )

    def run_fixture(
        self,
        *,
        config: ParserConfig,
        fixture: WbFixtureInput | None = None,
        run_id: str | None = None,
    ) -> WbProviderRunResult:
        run_id = run_id or new_run_id()
        fixture = fixture or synthetic_wb_fixture()
        config.ensure_runtime_dirs()

        suggest_rows = [_service_row(row, run_id=run_id, component="suggest", source_type="wb_suggest_dom") for row in fixture.suggest_rows]
        suggest_staging_rows = [_suggest_staging_row(row) for row in suggest_rows]
        filter_rows = [_service_row(row, run_id=run_id, component="filter", source_type="wb_filter_top_queries") for row in fixture.filter_rows]
        product_rows = [_service_row(row, run_id=run_id, component="serp", source_type="wb_serp_exactmatch_v18") for row in fixture.product_rows]
        seller_rows = [_service_row(row, run_id=run_id, component="sellers", source_type="wb_suppliers_shipment_api_v1") for row in fixture.seller_rows]
        bridge_rows = [
            _service_row(row, run_id=run_id, component="sellers", source_type="seller_query_product_bridge")
            for row in (fixture.bridge_rows or tuple(_bridge_rows_from_products(product_rows, run_id=run_id)))
        ]

        provider_files = {
            "suggest_raw": _write_provider_csv(config, "raw", "suggest", run_id, "suggest_alpha_raw.csv", suggest_rows, SUGGEST_RAW_FIELDS),
            "suggest_staging": _write_provider_csv(
                config, "staging", "suggest", run_id, "suggest_alpha_staging.csv", suggest_staging_rows, SUGGEST_STAGING_FIELDS
            ),
            "filter_top_queries": _write_provider_csv(
                config, "marts", "filter", run_id, "top_queries.csv", filter_rows, FILTER_TOP_FIELDS
            ),
            "serp_products": _write_provider_csv(
                config, "marts", "serp", run_id, "products_daily.csv", product_rows, SERP_PRODUCT_FIELDS
            ),
            "sellers_daily": _write_provider_csv(
                config, "marts", "sellers", run_id, "sellers_daily.csv", seller_rows, SELLER_FIELDS
            ),
            "seller_query_product_bridge": _write_provider_csv(
                config, "marts", "sellers", run_id, "seller_query_product_bridge.csv", bridge_rows, BRIDGE_FIELDS
            ),
        }

        common_marts = {
            "queries": [_query_mart_row(row) for row in filter_rows],
            "products": [_product_mart_row(row) for row in product_rows if row.get("nmId")],
            "sellers": [_seller_mart_row(row) for row in seller_rows if row.get("supplier_id")],
            "seller_query_product_bridge": [_bridge_mart_row(row) for row in bridge_rows if row.get("nmId") and row.get("supplier_id")],
        }
        common_mart_files = {
            name: _write_common_mart_csv(config, name, run_id, rows) for name, rows in common_marts.items()
        }

        latest_inputs = {
            **provider_files,
            **{f"common_{name}": path for name, path in common_mart_files.items()},
        }
        latest_files = {name: str(_publish_latest(Path(path))) for name, path in latest_inputs.items()}
        checkpoint_path = _write_checkpoints(
            config,
            run_id=run_id,
            rows_by_component={
                "suggest": suggest_rows,
                "filter": filter_rows,
                "serp": product_rows,
                "sellers": seller_rows,
            },
        )

        component_statuses = _component_statuses(
            fixture.component_statuses,
            suggest=suggest_rows,
            filter=filter_rows,
            serp=product_rows,
            sellers=seller_rows,
        )
        row_statuses = tuple(
            str(row.get("status") or "success")
            for rows in (suggest_rows, filter_rows, product_rows, seller_rows, bridge_rows)
            for row in rows
        )
        quality_summary = summarize_data_quality(
            run_id=run_id,
            marketplace=self.marketplace,
            source_system=self.provider_id,
            component_statuses=component_statuses,
            row_statuses=row_statuses,
            export_errors=fixture.errors,
        )
        validation_issues = [
            issue.message
            for mart_name, rows in common_marts.items()
            for issue in validate_mart_rows(
                mart_name,
                rows,
                source_system=self.provider_id,
                seller_data_expected=mart_name in {"products", "seller_query_product_bridge"} and bool(rows),
            ).issues
        ]

        export_result = create_export_bundle(
            config=config,
            marketplace=self.marketplace,
            run_id=run_id,
            mart_rows=common_marts,
            component_statuses={**component_statuses, "export": "success"},
            row_statuses=row_statuses,
            warnings=tuple(validation_issues),
            errors=fixture.errors,
        )
        run_report_path, latest_run_report_path = _write_run_report(
            config,
            run_id=run_id,
            status=quality_summary.run_status,
            report_usability=quality_summary.report_usability,
            component_statuses=component_statuses,
            provider_files=provider_files,
            common_mart_files=common_mart_files,
            latest_files=latest_files,
            checkpoint_path=checkpoint_path,
            export_result=export_result,
            warnings=quality_summary.warnings + tuple(validation_issues),
            errors=quality_summary.errors,
        )
        return WbProviderRunResult(
            run_id=run_id,
            status=quality_summary.run_status,
            report_usability=quality_summary.report_usability,
            provider_files=provider_files,
            common_mart_files=common_mart_files,
            latest_files=latest_files,
            checkpoint_path=checkpoint_path,
            run_report_path=run_report_path,
            latest_run_report_path=latest_run_report_path,
            export_result=export_result,
        )


def synthetic_wb_fixture() -> WbFixtureInput:
    return WbFixtureInput(
        suggest_rows=(
            {
                "source_system": WB_SOURCE_ALIAS,
                "base_prefix": "кофе",
                "typed_query": "кофе а",
                "letter": "а",
                "depth": 1,
                "position": 1,
                "list_size": 1,
                "suggestion": "кофе арабика",
            },
        ),
        filter_rows=(
            {
                "source_system": WB_SOURCE_ALIAS,
                "rank": 1,
                "query": "кофе арабика",
                "query_group": "coffee",
                "niche": "coffee",
                "normalized_query": "кофе арабика",
                "canonical_query": "кофе арабика",
                "source_query": "кофе арабика",
                "hybrid_score": 42.5,
                "score_suggest": 1.0,
                "score_wordstat": 41.5,
                "wordstat_volume": 1250,
                "count": 3,
                "selected_reason": "top_n",
            },
        ),
        product_rows=(
            {
                "source_system": WB_SOURCE_ALIAS,
                "query": "кофе арабика",
                "query_group": "coffee",
                "page": 1,
                "position_on_page": 1,
                "absolute_position": 1,
                "nmId": "123456",
                "imtId": "987",
                "product_name": "Кофе арабика 1 кг",
                "brand": "WB Test Brand",
                "brandId": "12",
                "supplier_id": "456789",
                "supplier_name": "WB Test Seller",
                "final_price": "799.0",
                "price": "999.0",
                "sale_price": "799.0",
                "rating": "4.8",
                "feedbacks": "321",
                "promo_markers": "",
                "raw_file": "data/raw/serp/run/page_1.json",
                "raw_page_path": "data/raw/serp/run/page_1.json",
            },
        ),
        seller_rows=(
            {
                "source_system": WB_SOURCE_ALIAS,
                "supplier_id": "456789",
                "supplier_name": "WB Test Seller",
                "rating": "4.9",
                "valuation": "100",
                "feedbacks_count": "321",
                "product_count": "1",
                "query_count": "1",
                "queries_ref": "кофе арабика",
                "query_groups_ref": "coffee",
                "nm_ids_ref": "123456",
                "source_product_run_ids": "run_synthetic_wb_001",
            },
        ),
    )


def _service_row(row: dict[str, Any], *, run_id: str, component: str, source_type: str) -> dict[str, Any]:
    collected_at = str(row.get("collected_at_utc") or datetime.now(UTC).isoformat())
    source_system = str(row.get("source_system") or WB_SOURCE_ALIAS)
    status = str(row.get("status") or "success")
    return {
        **row,
        "run_id": run_id,
        "component": component,
        "collected_at_utc": collected_at,
        "source_system": source_system,
        "source_type": str(row.get("source_type") or source_type),
        "source_ref": str(row.get("source_ref") or _default_source_ref(row, component)),
        "status": status,
        "error_message": str(row.get("error_message") or ""),
        "marketplace": "wb",
        "schema_version": SCHEMA_VERSION,
        "data_quality_status": map_source_status(status)[1],
    }


def _default_source_ref(row: dict[str, Any], component: str) -> str:
    if component == "suggest":
        return str(row.get("typed_query") or row.get("suggestion") or "suggest")
    if component == "serp":
        return f"{row.get('query', '')}|page={row.get('page', '')}"
    if component == "sellers":
        return f"seller:{row.get('supplier_id', '')}"
    return str(row.get("query") or component)


def _suggest_staging_row(row: dict[str, Any]) -> dict[str, Any]:
    suggestion = str(row.get("suggestion") or "")
    return {
        **row,
        "suggestion_lc": suggestion.strip().lower().replace("ё", "е"),
        "is_empty_suggestion": 0 if suggestion else 1,
    }


def _query_mart_row(row: dict[str, Any]) -> dict[str, Any]:
    query = str(row.get("query") or row.get("normalized_query") or "")
    return _mart_row(
        "queries",
        {
            "marketplace": "wb",
            "source_system": normalize_source_system(str(row.get("source_system") or WB_SOURCE_ALIAS)),
            "run_id": row.get("run_id"),
            "query": query,
            "normalized_query": row.get("normalized_query") or query,
            "canonical_query": row.get("canonical_query") or row.get("normalized_query") or query,
            "query_group": row.get("query_group") or row.get("niche") or "",
            "source_query": row.get("source_query") or query,
            "rank": row.get("rank", ""),
            "score": row.get("score", ""),
            "hybrid_score": row.get("hybrid_score", ""),
            "wordstat_volume": row.get("wordstat_volume", ""),
            "count": row.get("count", ""),
            "selected_reason": row.get("selected_reason", ""),
            "data_quality_status": row.get("data_quality_status"),
            "schema_version": SCHEMA_VERSION,
        },
    )


def _product_mart_row(row: dict[str, Any]) -> dict[str, Any]:
    provider = normalize_source_system(str(row.get("source_system") or WB_SOURCE_ALIAS))
    return _mart_row(
        "products",
        {
            "marketplace": "wb",
            "source_system": provider,
            "run_id": row.get("run_id"),
            "query": row.get("query", ""),
            "query_group": row.get("query_group", ""),
            "page": row.get("page", ""),
            "position_on_page": row.get("position_on_page", ""),
            "absolute_position": row.get("absolute_position", ""),
            "external_product_id": str(row.get("nmId") or ""),
            "product_name": row.get("product_name", ""),
            "brand": row.get("brand", ""),
            "external_seller_id": str(row.get("supplier_id") or ""),
            "seller_name": row.get("supplier_name", ""),
            "final_price": row.get("final_price", ""),
            "price": row.get("price", ""),
            "old_price": row.get("old_price", ""),
            "sale_price": row.get("sale_price", ""),
            "rating": row.get("rating", ""),
            "reviews_count": row.get("reviews_count", ""),
            "feedbacks": row.get("feedbacks", ""),
            "promo_markers": row.get("promo_markers", ""),
            "raw_file": row.get("raw_file", ""),
            "raw_page_path": row.get("raw_page_path", ""),
            "data_quality_status": row.get("data_quality_status"),
            "schema_version": SCHEMA_VERSION,
        },
    )


def _seller_mart_row(row: dict[str, Any]) -> dict[str, Any]:
    provider = normalize_source_system(str(row.get("source_system") or WB_SOURCE_ALIAS))
    return _mart_row(
        "sellers",
        {
            "marketplace": "wb",
            "source_system": provider,
            "run_id": row.get("run_id"),
            "external_seller_id": str(row.get("supplier_id") or ""),
            "seller_name": row.get("supplier_name", ""),
            "seller_rating": row.get("rating", ""),
            "seller_reviews": row.get("seller_reviews", row.get("valuation", "")),
            "feedbacks_count": row.get("feedbacks_count", ""),
            "product_count": row.get("product_count", ""),
            "query_count": row.get("query_count", ""),
            "queries_ref": row.get("queries_ref", ""),
            "query_groups_ref": row.get("query_groups_ref", ""),
            "external_product_ids_ref": row.get("external_product_ids_ref", row.get("nm_ids_ref", "")),
            "source_product_run_ids": row.get("source_product_run_ids", ""),
            "data_quality_status": row.get("data_quality_status"),
            "schema_version": SCHEMA_VERSION,
        },
    )


def _bridge_mart_row(row: dict[str, Any]) -> dict[str, Any]:
    provider = normalize_source_system(str(row.get("source_system") or WB_SOURCE_ALIAS))
    return _mart_row(
        "seller_query_product_bridge",
        {
            "marketplace": "wb",
            "source_system": provider,
            "run_id": row.get("run_id"),
            "query": row.get("query", ""),
            "query_group": row.get("query_group", ""),
            "external_product_id": str(row.get("nmId") or ""),
            "external_seller_id": str(row.get("supplier_id") or ""),
            "seller_name": row.get("supplier_name", ""),
            "product_run_id": row.get("product_run_id", ""),
            "schema_version": SCHEMA_VERSION,
            "data_quality_status": row.get("data_quality_status"),
        },
    )


def _mart_row(mart_name: str, values: dict[str, Any]) -> dict[str, Any]:
    return {field_name: values.get(field_name, "") for field_name in MART_FIELDS[mart_name]}


def _bridge_rows_from_products(product_rows: list[dict[str, Any]], *, run_id: str) -> list[dict[str, Any]]:
    seen: set[tuple[str, str, str, str, str]] = set()
    rows: list[dict[str, Any]] = []
    for row in product_rows:
        seller_id = str(row.get("supplier_id") or "")
        nm_id = str(row.get("nmId") or "")
        if not seller_id or not nm_id:
            continue
        query = str(row.get("query") or "")
        query_group = str(row.get("query_group") or "")
        product_run_id = str(row.get("product_run_id") or row.get("run_id") or run_id)
        key = (seller_id, query, query_group, nm_id, product_run_id)
        if key in seen:
            continue
        seen.add(key)
        rows.append(
            {
                "run_id": run_id,
                "supplier_id": seller_id,
                "supplier_name": row.get("supplier_name", ""),
                "query": query,
                "query_group": query_group,
                "nmId": nm_id,
                "product_run_id": product_run_id,
                "source_system": row.get("source_system") or WB_SOURCE_ALIAS,
            }
        )
    return rows


def _write_provider_csv(
    config: ParserConfig,
    layer: str,
    component: str,
    run_id: str,
    filename: str,
    rows: list[dict[str, Any]],
    fields: tuple[str, ...],
) -> str:
    path = config.paths.data_path / layer / "wb" / component / run_id / filename
    _write_csv(path, rows, fields)
    return str(path)


def _write_common_mart_csv(config: ParserConfig, mart_name: str, run_id: str, rows: list[dict[str, Any]]) -> str:
    path = config.paths.data_path / "marts" / "wb" / "common" / run_id / f"{mart_name}.csv"
    _write_csv(path, rows, COMMON_MART_SCHEMAS[mart_name].fields)
    return str(path)


def _write_csv(path: Path, rows: list[dict[str, Any]], fields: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fields), delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _publish_latest(source_path: Path) -> Path:
    run_parent = source_path.parent.parent
    latest_dir = run_parent / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    target = latest_dir / source_path.name
    shutil.copy2(source_path, target)
    return target


def _write_checkpoints(config: ParserConfig, *, run_id: str, rows_by_component: dict[str, list[dict[str, Any]]]) -> Path:
    checkpoint_dir = config.paths.data_path / "checkpoints" / "wb" / run_id
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        component: [
            {
                "checkpoint_key": _checkpoint_key(component, row),
                "checkpoint_value": f"{row.get('status') or 'success'}|{run_id}|{row.get('collected_at_utc')}",
                "status": row.get("status") or "success",
                "updated_at_utc": row.get("collected_at_utc"),
            }
            for row in rows
        ]
        for component, rows in rows_by_component.items()
    }
    path = checkpoint_dir / "checkpoints.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return path


def _checkpoint_key(component: str, row: dict[str, Any]) -> str:
    if component == "suggest":
        return f"{row.get('base_prefix', '')}|{row.get('letter', '')}|{row.get('depth', '')}"
    if component == "filter":
        return "export|all"
    if component == "serp":
        return f"{row.get('query', '')}|{row.get('page', '')}"
    if component == "sellers":
        return str(row.get("supplier_id") or "")
    return component


def _component_statuses(explicit: dict[str, str], **rows_by_component: list[dict[str, Any]]) -> dict[str, str]:
    statuses: dict[str, str] = {}
    for component in ("suggest", "filter", "serp", "sellers"):
        statuses[component] = explicit.get(component) or _infer_component_status(rows_by_component.get(component, []))
    return statuses


def _infer_component_status(rows: list[dict[str, Any]]) -> str:
    source_statuses = [str(row.get("status") or "success") for row in rows]
    if not source_statuses:
        return "not_ready"
    if all(status == "success" for status in source_statuses):
        return "success"
    if all(status in {"error", "failed", "not_ready"} for status in source_statuses):
        return source_statuses[0]
    return "partial"


def _write_run_report(
    config: ParserConfig,
    *,
    run_id: str,
    status: str,
    report_usability: str,
    component_statuses: dict[str, str],
    provider_files: dict[str, str],
    common_mart_files: dict[str, str],
    latest_files: dict[str, str],
    checkpoint_path: Path,
    export_result: ExportSkeletonResult,
    warnings: tuple[str, ...],
    errors: tuple[str, ...],
) -> tuple[Path, Path]:
    reports_dir = config.paths.data_path / "run_reports" / "wb"
    reports_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_id": run_id,
        "marketplace": "wb",
        "source_system": "wb",
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "report_usability": report_usability,
        "component_statuses": component_statuses,
        "provider_files": provider_files,
        "common_mart_files": common_mart_files,
        "latest_files": latest_files,
        "checkpoint_path": str(checkpoint_path),
        "export": export_result.to_dict(),
        "warnings": list(warnings),
        "errors": list(errors),
        "generated_at_utc": datetime.now(UTC).isoformat(),
    }
    path = reports_dir / f"{run_id}.json"
    latest_path = reports_dir / "latest.json"
    text = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    path.write_text(text, encoding="utf-8")
    latest_path.write_text(text, encoding="utf-8")
    return path, latest_path
