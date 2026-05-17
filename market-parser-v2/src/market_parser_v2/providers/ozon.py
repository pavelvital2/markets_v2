"""Ozon provider migration behind the V2 provider boundary.

The default implementation is offline and testable with sanitized/mocked
responses. Live browser collection remains outside default tests; runtime
settings here model the required Ozon browser boundaries without reading or
logging cookie contents.
"""

from __future__ import annotations

import csv
import json
import re
import shutil
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.constants import MART_FIELDS, SCHEMA_VERSION
from market_parser_v2.core.contracts import (
    COMMON_MART_SCHEMAS,
    map_external_product_id,
    map_external_seller_id,
    validate_mart_rows,
)
from market_parser_v2.core.export import ExportSkeletonResult, create_export_bundle
from market_parser_v2.core.quality import map_source_status, summarize_data_quality
from market_parser_v2.core.run import new_run_id
from market_parser_v2.providers.base import ProviderPlan


OZON_COMPONENTS = ("suggest", "filter", "serp", "sellers", "export")
OZON_ORIGIN = "https://www.ozon.ru"
OZON_COOKIE_ENV = "OZON_COOKIE_FILE"
MAX_QUERY_SUGGESTIONS = 5
SELLER_ALLOWED_RESOURCE_TYPES = ("document",)

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
    "min_position",
    "source_typed_queries_count",
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

PRODUCT_RAW_FIELDS = (
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
    "raw_json_fragment",
    "raw_file",
    "raw_page_path",
    "product_url",
    "image_url",
    "marketplace",
    "schema_version",
    "data_quality_status",
)
PRODUCT_PROVIDER_MART_FIELDS = tuple(field_name for field_name in PRODUCT_RAW_FIELDS if field_name != "raw_json_fragment")

PAGES_INDEX_FIELDS = (
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
    "http_status",
    "products_count",
    "next_page",
    "raw_file",
    "raw_page_path",
    "marketplace",
    "schema_version",
    "data_quality_status",
)

SELLER_RAW_FIELDS = (
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
    "raw_json_fragment",
    "marketplace",
    "schema_version",
    "data_quality_status",
)
SELLER_PROVIDER_MART_FIELDS = tuple(field_name for field_name in SELLER_RAW_FIELDS if field_name != "raw_json_fragment")

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
class OzonRuntimeOptions:
    cookie_file: Path | None = None
    seller_concurrency: int = 4
    seller_delay_ms: int = 250
    seller_jitter_ms: int = 250
    suggest_throttle_ms: int = 350
    serp_throttle_ms: int = 250
    seller_document_only: bool = True

    @classmethod
    def from_config(cls, config: ParserConfig) -> "OzonRuntimeOptions":
        return cls(cookie_file=config.secrets.ozon_cookie_file)

    def to_safe_dict(self) -> dict[str, Any]:
        return {
            "cookie_file_env": OZON_COOKIE_ENV,
            "cookie_file_configured": self.cookie_file is not None,
            "seller_concurrency": self.seller_concurrency,
            "seller_delay_ms": self.seller_delay_ms,
            "seller_jitter_ms": self.seller_jitter_ms,
            "suggest_throttle_ms": self.suggest_throttle_ms,
            "serp_throttle_ms": self.serp_throttle_ms,
            "seller_document_only": self.seller_document_only,
            "allowed_seller_resource_types": list(SELLER_ALLOWED_RESOURCE_TYPES),
            "block_non_document_resources": self.seller_document_only,
        }


@dataclass(frozen=True)
class OzonSuggestTask:
    base_prefix: str
    typed_query: str
    letter: str
    depth: int
    response: dict[str, Any]
    status: str = "success"
    error_message: str = ""


@dataclass(frozen=True)
class OzonProductPage:
    query: str
    response: dict[str, Any]
    query_group: str = "all"
    page: int | None = None
    status: str = "success"
    error_message: str = ""
    http_status: int = 200


@dataclass(frozen=True)
class OzonFixtureInput:
    suggest_tasks: tuple[OzonSuggestTask, ...] = ()
    product_pages: tuple[OzonProductPage, ...] = ()
    seller_states_by_product_id: dict[str, Any] = field(default_factory=dict)
    component_statuses: dict[str, str] = field(default_factory=dict)
    errors: tuple[str, ...] = ()


@dataclass(frozen=True)
class OzonProviderRunResult:
    run_id: str
    status: str
    report_usability: str
    provider_files: dict[str, str]
    common_mart_files: dict[str, str]
    latest_files: dict[str, str]
    checkpoint_path: Path
    seller_progress_path: Path
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
            "seller_progress_path": str(self.seller_progress_path),
            "run_report_path": str(self.run_report_path),
            "latest_run_report_path": str(self.latest_run_report_path),
            "export": self.export_result.to_dict(),
        }


class OzonProvider:
    provider_id = "ozon"
    marketplace = "ozon"

    def build_plan(self) -> ProviderPlan:
        return ProviderPlan(
            provider_id=self.provider_id,
            marketplace=self.marketplace,
            components=OZON_COMPONENTS,
            live_scraping_enabled=False,
            status="ready_offline_fixture",
            notes=(
                "Ozon fixture/mocked migration path is implemented",
                "live marketplace collection is intentionally disabled",
                "cookie contents are never read by the offline provider path",
                "seller enrichment policy allows document resources only",
            ),
        )

    def run_fixture(
        self,
        *,
        config: ParserConfig,
        fixture: OzonFixtureInput | None = None,
        run_id: str | None = None,
        resume: bool = True,
    ) -> OzonProviderRunResult:
        run_id = run_id or new_run_id()
        fixture = fixture or synthetic_ozon_fixture()
        config.ensure_runtime_dirs()
        runtime_options = OzonRuntimeOptions.from_config(config)

        suggest_rows = _suggest_rows_from_tasks(fixture.suggest_tasks, run_id=run_id)
        suggest_staging_rows = [_suggest_staging_row(row) for row in suggest_rows]
        filter_rows = _top_query_rows(suggest_staging_rows, run_id=run_id)

        product_rows, pages_rows = _product_rows_from_pages(fixture.product_pages, run_id=run_id)
        seller_progress_path = _seller_progress_path(config, run_id)
        seller_results = _enrich_sellers_from_states(
            config=config,
            run_id=run_id,
            product_rows=product_rows,
            seller_states_by_product_id=fixture.seller_states_by_product_id,
            progress_path=seller_progress_path,
            resume=resume,
        )
        enriched_product_rows = _apply_seller_results(product_rows, seller_results)
        seller_rows, bridge_rows = _seller_and_bridge_rows(enriched_product_rows, seller_results, run_id=run_id)

        provider_files = {
            "suggest_raw": _write_provider_csv(
                config,
                "raw",
                "suggest",
                run_id,
                "suggest_alpha_raw.csv",
                suggest_rows,
                SUGGEST_RAW_FIELDS,
            ),
            "suggest_staging": _write_provider_csv(
                config,
                "staging",
                "suggest",
                run_id,
                "suggest_alpha_staging.csv",
                suggest_staging_rows,
                SUGGEST_STAGING_FIELDS,
            ),
            "filter_top_queries": _write_provider_csv(
                config,
                "marts",
                "filter",
                run_id,
                "top_queries.csv",
                filter_rows,
                FILTER_TOP_FIELDS,
            ),
            "serp_products_raw": _write_provider_csv(
                config,
                "raw",
                "serp",
                run_id,
                "products_raw.csv",
                enriched_product_rows,
                PRODUCT_RAW_FIELDS,
            ),
            "serp_products_staging": _write_provider_csv(
                config,
                "staging",
                "serp",
                run_id,
                "products_staging.csv",
                enriched_product_rows,
                PRODUCT_RAW_FIELDS,
            ),
            "serp_products_daily": _write_provider_csv(
                config,
                "marts",
                "serp",
                run_id,
                "products_daily.csv",
                [_provider_mart_row(row, PRODUCT_PROVIDER_MART_FIELDS) for row in enriched_product_rows],
                PRODUCT_PROVIDER_MART_FIELDS,
            ),
            "serp_pages_index": _write_provider_csv(
                config,
                "raw",
                "serp",
                run_id,
                "pages_raw_index.csv",
                pages_rows,
                PAGES_INDEX_FIELDS,
            ),
            "sellers_raw": _write_provider_csv(
                config,
                "raw",
                "sellers",
                run_id,
                "sellers_raw.csv",
                seller_rows,
                SELLER_RAW_FIELDS,
            ),
            "sellers_staging": _write_provider_csv(
                config,
                "staging",
                "sellers",
                run_id,
                "sellers_staging.csv",
                seller_rows,
                SELLER_RAW_FIELDS,
            ),
            "sellers_daily": _write_provider_csv(
                config,
                "marts",
                "sellers",
                run_id,
                "sellers_daily.csv",
                [_provider_mart_row(row, SELLER_PROVIDER_MART_FIELDS) for row in seller_rows],
                SELLER_PROVIDER_MART_FIELDS,
            ),
            "seller_query_product_bridge": _write_provider_csv(
                config,
                "marts",
                "sellers",
                run_id,
                "seller_query_product_bridge.csv",
                bridge_rows,
                BRIDGE_FIELDS,
            ),
        }
        provider_files["filter_queries_txt"] = _write_queries_txt(config, run_id, filter_rows)

        common_marts = {
            "queries": [_query_mart_row(row) for row in filter_rows],
            "products": [_product_mart_row(row) for row in enriched_product_rows if row.get("nmId")],
            "sellers": [_seller_mart_row(row) for row in seller_rows if row.get("supplier_id")],
            "seller_query_product_bridge": [
                _bridge_mart_row(row) for row in bridge_rows if row.get("nmId") and row.get("supplier_id")
            ],
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
                "serp": pages_rows,
                "sellers": seller_rows,
            },
            seller_progress_path=seller_progress_path,
        )

        component_statuses = _component_statuses(
            explicit=fixture.component_statuses,
            suggest_rows=suggest_rows,
            filter_rows=filter_rows,
            product_rows=enriched_product_rows,
            pages_rows=pages_rows,
            seller_results=seller_results,
            seller_rows=seller_rows,
        )
        row_statuses = tuple(
            str(row.get("status") or "success")
            for rows in (suggest_rows, filter_rows, enriched_product_rows, pages_rows, seller_rows, bridge_rows)
            for row in rows
        ) + tuple(str(result.get("status") or "error") for result in seller_results.values())
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
            seller_progress_path=seller_progress_path,
            export_result=export_result,
            runtime_options=runtime_options,
            warnings=quality_summary.warnings + tuple(validation_issues),
            errors=quality_summary.errors,
        )
        return OzonProviderRunResult(
            run_id=run_id,
            status=quality_summary.run_status,
            report_usability=quality_summary.report_usability,
            provider_files=provider_files,
            common_mart_files=common_mart_files,
            latest_files=latest_files,
            checkpoint_path=checkpoint_path,
            seller_progress_path=seller_progress_path,
            run_report_path=run_report_path,
            latest_run_report_path=latest_run_report_path,
            export_result=export_result,
        )


def synthetic_ozon_fixture() -> OzonFixtureInput:
    suggest_state = {
        "items": [
            _suggest_item("coffee beans"),
            _suggest_item("coffee beans arabica"),
            _suggest_item("coffee beans robusta"),
            _suggest_item("coffee filter"),
            _suggest_item("coffee grinder"),
            _suggest_item("brand item outside first five"),
        ]
    }
    return OzonFixtureInput(
        suggest_tasks=(
            OzonSuggestTask(
                base_prefix="coffee",
                typed_query="coffee",
                letter="seed",
                depth=0,
                response={"widgetStates": {"webSuggestions-1-default-1": json.dumps(suggest_state)}},
            ),
        ),
        product_pages=(
            OzonProductPage(
                query="coffee beans",
                page=1,
                response={
                    "nextPage": "/search/?text=coffee%20beans&page=2&opaque=abc",
                    "widgetStates": {"tileGridDesktop-1": json.dumps({"page": 1, "items": [_product_item("1001"), _product_item("1002")]})},
                },
            ),
            OzonProductPage(
                query="coffee beans",
                page=2,
                response={"widgetStates": {"tileGridDesktop-2": json.dumps({"page": 2, "items": [_product_item("1003")]})}},
            ),
        ),
        seller_states_by_product_id={
            "1001": _seller_state("seller-10", "Ozon Seller A", rating="4.9", feedbacks="12 reviews"),
            "1002": _seller_state("seller-10", "Ozon Seller A", rating="4.9", feedbacks="12 reviews"),
            "1003": _seller_state("seller-20", "Ozon Seller B", rating="4.7", feedbacks="8 reviews"),
        },
    )


def extract_web_suggestions(payload: dict[str, Any]) -> list[str]:
    body = payload.get("response_body", payload)
    if not isinstance(body, dict):
        return []

    suggestions: list[str] = []
    seen: set[str] = set()
    widget_states = body.get("widgetStates") or {}
    if not isinstance(widget_states, dict):
        return []

    for key, raw_state in widget_states.items():
        if not key.startswith("webSuggestions"):
            continue
        state = _parse_jsonish(raw_state)
        items = state.get("items") if isinstance(state, dict) else None
        if not isinstance(items, list):
            continue
        for item in items[:MAX_QUERY_SUGGESTIONS]:
            text = _norm(_nested_get(item, ("cellItem", "centerBlock", "title", "text")))
            dedupe_key = _norm_lc(text)
            if not dedupe_key or dedupe_key in seen:
                continue
            seen.add(dedupe_key)
            suggestions.append(text)
    return suggestions


def extract_tile_grids(payload: dict[str, Any]) -> list[dict[str, Any]]:
    body = payload.get("response_body", payload)
    if not isinstance(body, dict):
        return []
    widget_states = body.get("widgetStates") or {}
    if not isinstance(widget_states, dict):
        return []

    grids: list[dict[str, Any]] = []
    for key, raw_state in widget_states.items():
        if not key.startswith("tileGrid"):
            continue
        state = _parse_jsonish(raw_state)
        if isinstance(state, dict) and isinstance(state.get("items"), list):
            grids.append(state)
    return grids


def extract_seller_from_product_card_state(payload: Any, *, nm_id: str, product_url: str = "") -> dict[str, Any]:
    wrapper = payload if isinstance(payload, dict) else {}
    state = _seller_state_payload(payload)
    if not isinstance(state, dict):
        return {
            "nmId": nm_id,
            "product_url": product_url,
            "status": "error",
            "error_message": "seller_state_not_found",
            "http_status": wrapper.get("http_status", 0) if isinstance(wrapper, dict) else 0,
        }

    seller_id = _find_first_key(state, "sellerId")
    seller_name = _norm(_nested_get(state, ("sellerCell", "centerBlock", "title", "text")))
    seller_link = _nested_get(state, ("sellerCell", "common", "action", "link")) or ""
    rating = _norm(_nested_get(state, ("rating", "title", "text")))
    feedbacks = _norm(
        _nested_get(state, ("reviews", "title", "text"))
        or _nested_get(state, ("reviews", "subtitle", "text"))
        or ""
    )
    feedbacks_count = re.sub(r"\D+", "", feedbacks)
    status = "success" if seller_id or seller_name else "error"
    return {
        "nmId": nm_id,
        "product_url": product_url,
        "status": status,
        "error_message": "" if status == "success" else "seller_empty",
        "supplier_id": seller_id,
        "supplier_name": seller_name,
        "seller_link": seller_link,
        "rating": rating,
        "feedbacks_count": feedbacks_count,
        "http_status": wrapper.get("http_status", 200) if isinstance(wrapper, dict) else 200,
        "raw_json_fragment": json.dumps(state, ensure_ascii=False, sort_keys=True),
    }


def seller_resource_action(resource_type: str) -> str:
    return "continue" if resource_type in SELLER_ALLOWED_RESOURCE_TYPES else "abort"


def _suggest_rows_from_tasks(tasks: tuple[OzonSuggestTask, ...], *, run_id: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for task in tasks:
        collected_at = datetime.now(UTC).isoformat()
        status = task.status
        error_message = task.error_message
        suggestions = extract_web_suggestions(task.response) if status == "success" else []
        if status == "success" and not suggestions:
            status = "empty"
        row_suggestions = suggestions or [""]
        for index, suggestion in enumerate(row_suggestions, start=1):
            row = _service_row(
                {
                    "base_prefix": task.base_prefix,
                    "typed_query": task.typed_query,
                    "letter": task.letter,
                    "depth": task.depth,
                    "position": index if suggestion else 0,
                    "list_size": len(suggestions),
                    "suggestion": _norm(suggestion),
                    "collected_at_utc": collected_at,
                    "status": status,
                    "error_message": error_message,
                },
                run_id=run_id,
                component="suggest",
                source_type="ozon_search_suggestions_entrypoint",
            )
            rows.append(row)
    return rows


def _suggest_staging_row(row: dict[str, Any]) -> dict[str, Any]:
    suggestion = str(row.get("suggestion") or "")
    return {
        **row,
        "suggestion_lc": _norm_lc(suggestion),
        "is_empty_suggestion": 0 if suggestion else 1,
    }


def _top_query_rows(staging_rows: list[dict[str, Any]], *, run_id: str, top_n: int = 50) -> list[dict[str, Any]]:
    stats: dict[str, dict[str, Any]] = {}
    for row in staging_rows:
        suggestion_lc = str(row.get("suggestion_lc") or "")
        if row.get("status") != "success" or not suggestion_lc:
            continue
        current = stats.setdefault(
            suggestion_lc,
            {
                "query": suggestion_lc,
                "source_query": row.get("suggestion") or suggestion_lc,
                "count": 0,
                "min_position": 10**9,
                "source_typed_queries": set(),
            },
        )
        current["count"] += 1
        current["min_position"] = min(current["min_position"], int(row.get("position") or 0) or 10**9)
        current["source_typed_queries"].add(row.get("typed_query") or "")

    ranked = []
    for item in stats.values():
        min_position = item["min_position"]
        score = item["count"] * 100 + max(0, 20 - min_position)
        ranked.append(
            {
                **item,
                "score": score,
                "source_typed_queries_count": len(item["source_typed_queries"]),
            }
        )
    ranked.sort(key=lambda item: (-item["score"], -item["count"], item["min_position"], item["query"]))
    selected = ranked if top_n <= 0 else ranked[:top_n]

    rows: list[dict[str, Any]] = []
    for index, item in enumerate(selected, start=1):
        rows.append(
            _service_row(
                {
                    "component": "filter",
                    "rank": index,
                    "query": item["query"],
                    "query_group": "all",
                    "niche": "all",
                    "normalized_query": item["query"],
                    "canonical_query": item["query"],
                    "source_query": item["source_query"],
                    "hybrid_score": item["score"],
                    "score_suggest": item["score"],
                    "score_wordstat": 0,
                    "wordstat_volume": 0,
                    "count": item["count"],
                    "selected_reason": "ozon_suggest_score",
                    "min_position": 0 if item["min_position"] == 10**9 else item["min_position"],
                    "source_typed_queries_count": item["source_typed_queries_count"],
                    "status": "success",
                    "source_ref": item["query"],
                },
                run_id=run_id,
                component="filter",
                source_type="ozon_suggest_score",
            )
        )
    return rows


def _product_rows_from_pages(
    pages: tuple[OzonProductPage, ...],
    *,
    run_id: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    product_rows: list[dict[str, Any]] = []
    page_rows: list[dict[str, Any]] = []
    absolute_count = 0

    for page_index, page_input in enumerate(pages, start=1):
        collected_at = datetime.now(UTC).isoformat()
        body = page_input.response.get("response_body", page_input.response)
        grids = extract_tile_grids(page_input.response) if page_input.status == "success" else []
        page_products: list[dict[str, Any]] = []
        page_no = page_input.page or _page_from_body(body) or page_index
        raw_file = _raw_page_rel(page_input.query, page_no, run_id)
        next_page = body.get("nextPage", "") if isinstance(body, dict) else ""

        for grid in grids:
            grid_page = _as_int(grid.get("page")) or page_no
            items = grid.get("items") if isinstance(grid.get("items"), list) else []
            position_base = len(page_products)
            for item_index, item in enumerate(items, start=1):
                if not isinstance(item, dict):
                    continue
                observed_index = position_base + item_index
                row = _product_row_from_item(
                    item,
                    run_id=run_id,
                    query=page_input.query,
                    query_group=page_input.query_group,
                    page_no=grid_page,
                    position_on_page=observed_index,
                    absolute_position=absolute_count + observed_index,
                    raw_file=raw_file,
                    collected_at=collected_at,
                )
                page_products.append(row)
            page_no = grid_page

        absolute_count += len(page_products)
        product_rows.extend(page_products)
        status = page_input.status
        error_message = page_input.error_message
        if status == "success" and not page_products:
            status = "empty"
        page_rows.append(
            _service_row(
                {
                    "query": page_input.query,
                    "query_group": page_input.query_group,
                    "page": page_no,
                    "http_status": page_input.http_status,
                    "products_count": len(page_products),
                    "next_page": next_page,
                    "raw_file": raw_file,
                    "raw_page_path": raw_file,
                    "status": status,
                    "error_message": error_message,
                    "collected_at_utc": collected_at,
                },
                run_id=run_id,
                component="serp",
                source_type="ozon_search_entrypoint_tilegrid",
            )
        )
    return product_rows, page_rows


def _product_row_from_item(
    item: dict[str, Any],
    *,
    run_id: str,
    query: str,
    query_group: str,
    page_no: int,
    position_on_page: int,
    absolute_position: int,
    raw_file: str,
    collected_at: str,
) -> dict[str, Any]:
    prices = _extract_prices(item)
    rating = _extract_rating_feedbacks(item)
    sku = _clean_id(item.get("sku") or _nested_get(item, ("multiButton", "ozonButton", "addToCart", "skuId")))
    product_id = _clean_id(item.get("id") or sku)
    row = _service_row(
        {
            "query": query,
            "query_group": query_group,
            "page": page_no,
            "position_on_page": position_on_page,
            "absolute_position": absolute_position,
            "nmId": sku or product_id,
            "imtId": product_id or sku,
            "product_name": _extract_title(item),
            "brand": _extract_brand(item),
            "brandId": "",
            "supplier_id": "",
            "supplier_name": "",
            "final_price": prices["final_price"],
            "price": prices["price"],
            "sale_price": prices["sale_price"],
            "discount": prices["discount"],
            "sale": "",
            "rating": rating["rating"],
            "feedbacks": rating["feedbacks"],
            "valuation": "",
            "total_quantity": "",
            "promo_markers": _promo_markers(item),
            "raw_json_fragment": json.dumps(item, ensure_ascii=False, sort_keys=True),
            "raw_file": raw_file,
            "raw_page_path": raw_file,
            "product_url": _canonical_product_url(_nested_get(item, ("action", "link"))),
            "image_url": _extract_image_url(item),
            "collected_at_utc": collected_at,
        },
        run_id=run_id,
        component="serp",
        source_type="ozon_search_entrypoint_tilegrid",
    )
    return row


def _enrich_sellers_from_states(
    *,
    config: ParserConfig,
    run_id: str,
    product_rows: list[dict[str, Any]],
    seller_states_by_product_id: dict[str, Any],
    progress_path: Path,
    resume: bool,
) -> dict[str, dict[str, Any]]:
    del config, run_id
    results = _load_seller_progress(progress_path) if resume else {}
    jobs = _seller_jobs(product_rows)
    for job in jobs:
        nm_id = job["nmId"]
        if resume and results.get(nm_id, {}).get("status") == "success":
            continue
        result = extract_seller_from_product_card_state(
            seller_states_by_product_id.get(nm_id),
            nm_id=nm_id,
            product_url=job.get("product_url", ""),
        )
        results[nm_id] = result
        _write_seller_progress(progress_path, results)
    if jobs and not progress_path.exists():
        _write_seller_progress(progress_path, results)
    return results


def _seller_jobs(product_rows: list[dict[str, Any]]) -> list[dict[str, str]]:
    seen: set[str] = set()
    jobs: list[dict[str, str]] = []
    for row in product_rows:
        if row.get("supplier_id"):
            continue
        nm_id = str(row.get("nmId") or "")
        product_url = str(row.get("product_url") or "")
        if not nm_id or not product_url or nm_id in seen:
            continue
        seen.add(nm_id)
        jobs.append({"nmId": nm_id, "product_url": product_url})
    return jobs


def _apply_seller_results(
    product_rows: list[dict[str, Any]],
    seller_results: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    enriched: list[dict[str, Any]] = []
    for row in product_rows:
        updated = dict(row)
        seller = seller_results.get(str(row.get("nmId") or ""))
        if seller and seller.get("status") == "success":
            updated["supplier_id"] = seller.get("supplier_id") or row.get("supplier_id", "")
            updated["supplier_name"] = seller.get("supplier_name") or row.get("supplier_name", "")
        _downgrade_missing_seller_quality(updated, seller)
        enriched.append(updated)
    return enriched


def _downgrade_missing_seller_quality(row: dict[str, Any], seller_result: dict[str, Any] | None) -> None:
    if row.get("supplier_id"):
        return
    current_status = str(row.get("status") or "success")
    if map_source_status(current_status)[1] != "valid_for_reports":
        return

    row["status"] = "partial"
    row["data_quality_status"] = map_source_status("partial")[1]
    existing_message = str(row.get("error_message") or "")
    enrichment_message = _missing_seller_error_message(seller_result)
    row["error_message"] = "|".join(message for message in (existing_message, enrichment_message) if message)


def _missing_seller_error_message(seller_result: dict[str, Any] | None) -> str:
    if not seller_result:
        return "seller_enrichment_missing_seller_id"
    result_message = str(seller_result.get("error_message") or "")
    if result_message:
        return f"seller_enrichment_missing_seller_id:{result_message}"
    return "seller_enrichment_missing_seller_id"


def _seller_and_bridge_rows(
    product_rows: list[dict[str, Any]],
    seller_results: dict[str, dict[str, Any]],
    *,
    run_id: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    collected_at = datetime.now(UTC).isoformat()
    seller_map: dict[str, dict[str, Any]] = {}
    for row in product_rows:
        seller_id = str(row.get("supplier_id") or "")
        if not seller_id:
            continue
        seller = seller_map.setdefault(
            seller_id,
            {
                "supplier_id": seller_id,
                "supplier_name": row.get("supplier_name", ""),
                "queries": set(),
                "query_groups": set(),
                "nm_ids": set(),
                "source_product_run_ids": set(),
                "rating": "",
                "feedbacks_count": "",
                "http_status": "",
                "raw_json_fragment": "",
            },
        )
        result = seller_results.get(str(row.get("nmId") or "")) or {}
        seller["queries"].add(row.get("query", ""))
        seller["query_groups"].add(row.get("query_group", ""))
        seller["nm_ids"].add(row.get("nmId", ""))
        seller["source_product_run_ids"].add(row.get("run_id", ""))
        seller["rating"] = seller["rating"] or result.get("rating", "")
        seller["feedbacks_count"] = seller["feedbacks_count"] or result.get("feedbacks_count", "")
        seller["http_status"] = seller["http_status"] or result.get("http_status", "")
        seller["raw_json_fragment"] = seller["raw_json_fragment"] or result.get("raw_json_fragment", "")

    seller_rows = [
        _service_row(
            {
                "source_type": "ozon_product_current_seller_state",
                "source_ref": f"seller:{seller['supplier_id']}",
                "supplier_id": seller["supplier_id"],
                "supplier_name": seller["supplier_name"],
                "rating": seller["rating"],
                "valuation": "",
                "feedbacks_count": seller["feedbacks_count"],
                "sale_item_quantity": "",
                "registration_date": "",
                "update_date": "",
                "delivery_duration": "",
                "supp_ratio": "",
                "ratio_mark_supp": "",
                "rating_is_invisible": "",
                "http_status": seller["http_status"],
                "query_count": len(seller["queries"]),
                "product_count": len(seller["nm_ids"]),
                "queries_ref": "|".join(sorted(filter(None, seller["queries"]))),
                "query_groups_ref": "|".join(sorted(filter(None, seller["query_groups"]))),
                "nm_ids_ref": "|".join(sorted(filter(None, seller["nm_ids"]))),
                "source_product_run_ids": "|".join(sorted(filter(None, seller["source_product_run_ids"]))),
                "raw_file": "",
                "raw_json_fragment": seller["raw_json_fragment"],
                "collected_at_utc": collected_at,
            },
            run_id=run_id,
            component="sellers",
            source_type="ozon_product_current_seller_state",
        )
        for seller in seller_map.values()
    ]

    bridge_rows = [
        _service_row(
            {
                "source_type": "seller_query_product_bridge",
                "source_ref": f"{row.get('supplier_id')}|{row.get('nmId')}|{row.get('query')}",
                "supplier_id": row.get("supplier_id", ""),
                "supplier_name": row.get("supplier_name", ""),
                "query": row.get("query", ""),
                "query_group": row.get("query_group", ""),
                "nmId": row.get("nmId", ""),
                "product_run_id": row.get("run_id", ""),
                "collected_at_utc": collected_at,
            },
            run_id=run_id,
            component="sellers",
            source_type="seller_query_product_bridge",
        )
        for row in product_rows
        if row.get("supplier_id") and row.get("nmId")
    ]
    return seller_rows, bridge_rows


def _service_row(row: dict[str, Any], *, run_id: str, component: str, source_type: str) -> dict[str, Any]:
    status = str(row.get("status") or "success")
    return {
        **row,
        "run_id": run_id,
        "component": component,
        "collected_at_utc": str(row.get("collected_at_utc") or datetime.now(UTC).isoformat()),
        "source_system": "ozon",
        "source_type": str(row.get("source_type") or source_type),
        "source_ref": str(row.get("source_ref") or _default_source_ref(row, component)),
        "status": status,
        "error_message": str(row.get("error_message") or ""),
        "marketplace": "ozon",
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


def _query_mart_row(row: dict[str, Any]) -> dict[str, Any]:
    query = str(row.get("query") or row.get("normalized_query") or "")
    return _mart_row(
        "queries",
        {
            "marketplace": "ozon",
            "source_system": "ozon",
            "run_id": row.get("run_id"),
            "query": query,
            "normalized_query": row.get("normalized_query") or query,
            "canonical_query": row.get("canonical_query") or row.get("normalized_query") or query,
            "query_group": row.get("query_group") or row.get("niche") or "all",
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
    external_product_id = map_external_product_id(source_system="ozon", nm_id=row.get("nmId")).external_id
    seller_id = ""
    if row.get("supplier_id"):
        seller_id = map_external_seller_id(source_system="ozon", supplier_id=row.get("supplier_id")).external_id
    price = row.get("price", "")
    final_price = row.get("final_price", "")
    return _mart_row(
        "products",
        {
            "marketplace": "ozon",
            "source_system": "ozon",
            "run_id": row.get("run_id"),
            "query": row.get("query", ""),
            "query_group": row.get("query_group", ""),
            "page": row.get("page", ""),
            "position_on_page": row.get("position_on_page", ""),
            "absolute_position": row.get("absolute_position", ""),
            "external_product_id": external_product_id,
            "product_name": row.get("product_name", ""),
            "brand": row.get("brand", ""),
            "external_seller_id": seller_id,
            "seller_name": row.get("supplier_name", ""),
            "final_price": final_price,
            "price": price,
            "old_price": row.get("old_price", price if price and price != final_price else ""),
            "sale_price": row.get("sale_price", ""),
            "rating": row.get("rating", ""),
            "reviews_count": row.get("reviews_count", row.get("feedbacks", "")),
            "feedbacks": row.get("feedbacks", ""),
            "promo_markers": row.get("promo_markers", ""),
            "raw_file": row.get("raw_file", ""),
            "raw_page_path": row.get("raw_page_path", ""),
            "data_quality_status": row.get("data_quality_status"),
            "schema_version": SCHEMA_VERSION,
        },
    )


def _seller_mart_row(row: dict[str, Any]) -> dict[str, Any]:
    return _mart_row(
        "sellers",
        {
            "marketplace": "ozon",
            "source_system": "ozon",
            "run_id": row.get("run_id"),
            "external_seller_id": map_external_seller_id(source_system="ozon", supplier_id=row.get("supplier_id")).external_id,
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
    return _mart_row(
        "seller_query_product_bridge",
        {
            "marketplace": "ozon",
            "source_system": "ozon",
            "run_id": row.get("run_id"),
            "query": row.get("query", ""),
            "query_group": row.get("query_group", ""),
            "external_product_id": map_external_product_id(source_system="ozon", nm_id=row.get("nmId")).external_id,
            "external_seller_id": map_external_seller_id(source_system="ozon", supplier_id=row.get("supplier_id")).external_id,
            "seller_name": row.get("supplier_name", ""),
            "product_run_id": row.get("product_run_id", ""),
            "schema_version": SCHEMA_VERSION,
            "data_quality_status": row.get("data_quality_status"),
        },
    )


def _mart_row(mart_name: str, values: dict[str, Any]) -> dict[str, Any]:
    return {field_name: values.get(field_name, "") for field_name in MART_FIELDS[mart_name]}


def _provider_mart_row(row: dict[str, Any], fields: tuple[str, ...]) -> dict[str, Any]:
    return {field_name: row.get(field_name, "") for field_name in fields}


def _write_provider_csv(
    config: ParserConfig,
    layer: str,
    component: str,
    run_id: str,
    filename: str,
    rows: list[dict[str, Any]],
    fields: tuple[str, ...],
) -> str:
    path = config.paths.data_path / layer / "ozon" / component / run_id / filename
    _write_csv(path, rows, fields)
    return str(path)


def _write_common_mart_csv(config: ParserConfig, mart_name: str, run_id: str, rows: list[dict[str, Any]]) -> str:
    path = config.paths.data_path / "marts" / "ozon" / "common" / run_id / f"{mart_name}.csv"
    _write_csv(path, rows, COMMON_MART_SCHEMAS[mart_name].fields)
    return str(path)


def _write_csv(path: Path, rows: list[dict[str, Any]], fields: tuple[str, ...]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fields), delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def _write_queries_txt(config: ParserConfig, run_id: str, filter_rows: list[dict[str, Any]]) -> str:
    path = config.paths.data_path / "marts" / "ozon" / "filter" / run_id / "queries.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    text = "".join(f"{row.get('query', '')}\n" for row in filter_rows if row.get("query"))
    path.write_text(text, encoding="utf-8")
    return str(path)


def _publish_latest(source_path: Path) -> Path:
    run_parent = source_path.parent.parent
    latest_dir = run_parent / "latest"
    latest_dir.mkdir(parents=True, exist_ok=True)
    target = latest_dir / source_path.name
    shutil.copy2(source_path, target)
    return target


def _write_checkpoints(
    config: ParserConfig,
    *,
    run_id: str,
    rows_by_component: dict[str, list[dict[str, Any]]],
    seller_progress_path: Path,
) -> Path:
    checkpoint_dir = config.paths.data_path / "checkpoints" / "ozon" / run_id
    checkpoint_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        component: [
            {
                "checkpoint_key": _checkpoint_key(component, row),
                "checkpoint_value": _checkpoint_value(component, row, run_id),
                "status": row.get("status") or "success",
                "updated_at_utc": row.get("collected_at_utc"),
            }
            for row in rows
        ]
        for component, rows in rows_by_component.items()
    }
    payload["seller_progress"] = {
        "checkpoint_key": "seller_progress",
        "checkpoint_value": str(seller_progress_path),
        "status": "success" if seller_progress_path.exists() else "not_ready",
        "updated_at_utc": datetime.now(UTC).isoformat(),
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
        return str(row.get("supplier_id") or row.get("source_ref") or "")
    return component


def _checkpoint_value(component: str, row: dict[str, Any], run_id: str) -> str:
    if component == "serp":
        return f"{row.get('status') or 'success'}|{run_id}|nextPage={row.get('next_page', '')}"
    return f"{row.get('status') or 'success'}|{run_id}|{row.get('collected_at_utc')}"


def _component_statuses(
    *,
    explicit: dict[str, str],
    suggest_rows: list[dict[str, Any]],
    filter_rows: list[dict[str, Any]],
    product_rows: list[dict[str, Any]],
    pages_rows: list[dict[str, Any]],
    seller_results: dict[str, dict[str, Any]],
    seller_rows: list[dict[str, Any]],
) -> dict[str, str]:
    return {
        "suggest": explicit.get("suggest") or _infer_component_status(suggest_rows),
        "filter": explicit.get("filter") or _infer_component_status(filter_rows),
        "serp": explicit.get("serp") or _serp_component_status(product_rows, pages_rows),
        "sellers": explicit.get("sellers") or _seller_component_status(product_rows, seller_results, seller_rows),
    }


def _infer_component_status(rows: list[dict[str, Any]]) -> str:
    source_statuses = [str(row.get("status") or "success") for row in rows]
    if not source_statuses:
        return "not_ready"
    if all(status == "success" for status in source_statuses):
        return "success"
    if all(status in {"error", "failed", "not_ready"} for status in source_statuses):
        return source_statuses[0]
    return "partial"


def _serp_component_status(product_rows: list[dict[str, Any]], pages_rows: list[dict[str, Any]]) -> str:
    if not pages_rows:
        return "not_ready"
    page_statuses = [str(row.get("status") or "success") for row in pages_rows]
    if product_rows and all(status == "success" for status in page_statuses):
        return "success"
    if product_rows:
        return "partial"
    if any(status == "error" for status in page_statuses):
        return "error"
    return "empty"


def _seller_component_status(
    product_rows: list[dict[str, Any]],
    seller_results: dict[str, dict[str, Any]],
    seller_rows: list[dict[str, Any]],
) -> str:
    if not product_rows:
        return "not_ready"
    if not seller_results and not seller_rows:
        return "empty"
    statuses = [str(result.get("status") or "error") for result in seller_results.values()]
    if seller_rows and all(status == "success" for status in statuses):
        return "success"
    if seller_rows:
        return "partial"
    if statuses and all(status == "error" for status in statuses):
        return "error"
    return "empty"


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
    seller_progress_path: Path,
    export_result: ExportSkeletonResult,
    runtime_options: OzonRuntimeOptions,
    warnings: tuple[str, ...],
    errors: tuple[str, ...],
) -> tuple[Path, Path]:
    reports_dir = config.paths.data_path / "run_reports" / "ozon"
    reports_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "run_id": run_id,
        "marketplace": "ozon",
        "source_system": "ozon",
        "schema_version": SCHEMA_VERSION,
        "status": status,
        "report_usability": report_usability,
        "component_statuses": component_statuses,
        "provider_files": provider_files,
        "common_mart_files": common_mart_files,
        "latest_files": latest_files,
        "checkpoint_path": str(checkpoint_path),
        "seller_progress_path": str(seller_progress_path),
        "runtime": runtime_options.to_safe_dict(),
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


def _seller_progress_path(config: ParserConfig, run_id: str) -> Path:
    return config.paths.data_path / "checkpoints" / "ozon" / run_id / "seller_progress.json"


def _load_seller_progress(path: Path) -> dict[str, dict[str, Any]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    results = payload.get("results") if isinstance(payload, dict) else None
    if not isinstance(results, dict):
        return {}
    return {str(key): value for key, value in results.items() if isinstance(value, dict)}


def _write_seller_progress(path: Path, results: dict[str, dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    safe_results = {key: _safe_seller_result(value) for key, value in sorted(results.items())}
    payload = {
        "updated_at_utc": datetime.now(UTC).isoformat(),
        "results": safe_results,
    }
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    tmp.replace(path)


def _safe_seller_result(result: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in result.items()
        if key not in {"raw_json_fragment"} and not str(key).lower().startswith("cookie")
    }


def _raw_page_rel(query: str, page_no: int, run_id: str) -> str:
    return f"data/raw/ozon/serp/{run_id}/{_slugify(query)}/page_{page_no}.json"


def _slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", _norm_lc(value)).strip("-")
    return slug or "query"


def _parse_jsonish(value: Any) -> Any:
    if isinstance(value, str):
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return None
    return value


def _seller_state_payload(payload: Any) -> Any:
    if isinstance(payload, str):
        return _parse_jsonish(payload)
    if isinstance(payload, dict):
        for key in ("json", "state", "data_state", "raw"):
            if key in payload:
                return _parse_jsonish(payload[key])
        return payload
    return None


def _nested_get(obj: Any, path: tuple[str, ...]) -> Any:
    current = obj
    for key in path:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def _find_first_key(obj: Any, key: str) -> str:
    if not isinstance(obj, dict):
        return ""
    if key in obj and obj[key] is not None:
        return str(obj[key])
    for value in obj.values():
        found = _find_first_key(value, key)
        if found:
            return found
    return ""


def _page_from_body(body: Any) -> int | None:
    if not isinstance(body, dict):
        return None
    page_info = body.get("pageInfo") or {}
    if isinstance(page_info, dict):
        return _page_from_url(page_info.get("url"))
    return None


def _page_from_url(url: Any) -> int | None:
    if not isinstance(url, str):
        return None
    match = re.search(r"(?:^|[?&])page=(\d+)", url)
    return int(match.group(1)) if match else None


def _as_int(value: Any) -> int | None:
    try:
        if value is None or value == "":
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def _norm(value: Any) -> str:
    return " ".join(str(value or "").replace("\u00a0", " ").replace("\u2009", " ").split())


def _norm_lc(value: Any) -> str:
    return _norm(value).lower().replace("ё", "е")


def _clean_id(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def _canonical_product_url(link: Any) -> str:
    if not isinstance(link, str) or not link:
        return ""
    if link.startswith("/"):
        link = f"{OZON_ORIGIN}{link}"
    parts = urlsplit(link)
    return urlunsplit((parts.scheme, parts.netloc, parts.path, "", ""))


def _extract_title(item: dict[str, Any]) -> str:
    for state in item.get("mainState") or []:
        if isinstance(state, dict) and state.get("id") == "name":
            text_atom = state.get("textAtom")
            if isinstance(text_atom, dict) and text_atom.get("text"):
                return _norm(text_atom.get("text"))
    for state in item.get("mainState") or []:
        if isinstance(state, dict) and isinstance(state.get("textAtom"), dict):
            return _norm(state["textAtom"].get("text"))
    return ""


def _extract_prices(item: dict[str, Any]) -> dict[str, Any]:
    for state in item.get("mainState") or []:
        if not isinstance(state, dict):
            continue
        price_v2 = state.get("priceV2")
        prices = price_v2.get("price") if isinstance(price_v2, dict) else None
        if not isinstance(prices, list):
            continue
        current = ""
        original = ""
        for price in prices:
            if not isinstance(price, dict):
                continue
            if price.get("textStyle") == "ORIGINAL_PRICE":
                original = _price_number(price.get("text"))
            if not current and price.get("textStyle") in {"PRICE", "SALE_PRICE"}:
                current = _price_number(price.get("text"))
        if not current and prices and isinstance(prices[0], dict):
            current = _price_number(prices[0].get("text"))
        return {
            "final_price": current,
            "price": original or current,
            "sale_price": current,
            "discount": price_v2.get("discount", "") if isinstance(price_v2, dict) else "",
        }
    return {"final_price": "", "price": "", "sale_price": "", "discount": ""}


def _price_number(text: Any) -> int | float | str:
    cleaned = re.sub(r"[^\d,.-]+", "", _norm(text)).replace(",", ".")
    if not cleaned:
        return ""
    try:
        value = float(cleaned)
    except ValueError:
        return ""
    return int(value) if value.is_integer() else value


def _extract_brand(item: dict[str, Any]) -> str:
    before_name = []
    for state in item.get("mainState") or []:
        if not isinstance(state, dict):
            continue
        if state.get("id") == "name":
            break
        before_name.append(state)
    for state in before_name:
        labels = _nested_get(state, ("labelListV2", "items"))
        if not isinstance(labels, list):
            continue
        text_labels = [
            _norm(_nested_get(label, ("text", "text")))
            for label in labels
            if isinstance(label, dict) and label.get("type") == "text" and _nested_get(label, ("text", "text"))
        ]
        has_icon = any(isinstance(label, dict) and label.get("type") == "icon" for label in labels)
        if not has_icon and len(text_labels) == 1:
            return text_labels[0]
    return ""


def _extract_rating_feedbacks(item: dict[str, Any]) -> dict[str, Any]:
    for state in item.get("mainState") or []:
        if _nested_get(state, ("labelListV2", "testInfo", "automatizationId")) != "tile-list-rating":
            continue
        items = _nested_get(state, ("labelListV2", "items"))
        texts = [
            _norm(_nested_get(label, ("text", "text")))
            for label in items or []
            if isinstance(label, dict) and label.get("type") == "text" and _nested_get(label, ("text", "text"))
        ]
        rating = next((text for text in texts if re.match(r"^\d+([,.]\d+)?$", text)), "")
        feedback_text = next((text for text in texts if re.search(r"review|отзыв", text, re.IGNORECASE)), "")
        feedbacks = int(re.sub(r"\D+", "", feedback_text)) if re.sub(r"\D+", "", feedback_text) else ""
        return {"rating": rating.replace(",", "."), "feedbacks": feedbacks}
    return {"rating": "", "feedbacks": ""}


def _extract_image_url(item: dict[str, Any]) -> str:
    images = _nested_get(item, ("tileImage", "items"))
    if not isinstance(images, list):
        return ""
    for image in images:
        link = _nested_get(image, ("image", "link"))
        if isinstance(link, str) and link:
            return link
    return ""


def _promo_markers(item: dict[str, Any]) -> str:
    data = {
        key: _nested_get(item, ("tileImage", key))
        for key in ("leftBottomBadgeV2", "secondLeftBottomBadgeV2")
        if _nested_get(item, ("tileImage", key))
    }
    return json.dumps(data, ensure_ascii=False, sort_keys=True) if data else ""


def _suggest_item(text: str) -> dict[str, Any]:
    return {"cellItem": {"centerBlock": {"title": {"text": text}}}}


def _product_item(product_id: str) -> dict[str, Any]:
    return {
        "id": product_id,
        "sku": product_id,
        "action": {"link": f"/product/test-product-{product_id}/?tracking=removed"},
        "mainState": [
            {"labelListV2": {"items": [{"type": "text", "text": {"text": "Test Brand"}}]}},
            {"id": "name", "textAtom": {"text": f"Test Ozon Product {product_id}"}},
            {
                "priceV2": {
                    "price": [
                        {"textStyle": "PRICE", "text": "353"},
                        {"textStyle": "ORIGINAL_PRICE", "text": "499"},
                    ],
                    "discount": "-29%",
                }
            },
            {
                "labelListV2": {
                    "testInfo": {"automatizationId": "tile-list-rating"},
                    "items": [
                        {"type": "text", "text": {"text": "4.8"}},
                        {"type": "text", "text": {"text": "11 reviews"}},
                    ],
                }
            },
        ],
        "tileImage": {"items": [{"image": {"link": f"https://img.example.test/{product_id}.jpg"}}]},
    }


def _seller_state(seller_id: str, seller_name: str, *, rating: str = "", feedbacks: str = "") -> dict[str, Any]:
    return {
        "sellerCell": {
            "centerBlock": {"title": {"text": seller_name}},
            "common": {"action": {"link": f"/seller/{seller_id}/"}},
        },
        "rating": {"title": {"text": rating}},
        "reviews": {"title": {"text": feedbacks}},
        "header": {"badge": {"unsubscribed": {"common": {"action": {"params": {"sellerId": seller_id}}}}}},
    }
