from __future__ import annotations

from typing import Annotated, Any

from fastapi import APIRouter, Depends

from market_analytics.auth import require_basic_auth
from market_analytics.registry import ImportedRunRegistry, registry

router = APIRouter(
    prefix="/analytics",
    dependencies=[Depends(require_basic_auth)],
)


def get_registry() -> ImportedRunRegistry:
    return registry


@router.get("/overview")
def overview(
    run_registry: Annotated[ImportedRunRegistry, Depends(get_registry)],
) -> dict[str, Any]:
    latest = run_registry.latest()
    return {
        "marketplace_filter": "both",
        "analysis_period": None,
        "latest_run": _run_summary(latest),
        "counts": {
            "queries": None,
            "products": None,
            "sellers": None,
            "collection_errors": len(latest.errors) if latest else 0,
        },
        "partial_data_warning": bool(latest and latest.warnings),
        "sections": {
            "top_queries": [],
            "top_sellers_by_visibility": [],
            "top_products_by_visibility": [],
            "price_summaries": {},
            "rating_review_summaries": {},
            "market_opportunities": [],
            "data_quality_problems": latest.errors if latest else [],
        },
        "status": "skeleton",
    }


@router.get("/runs")
def runs(
    run_registry: Annotated[ImportedRunRegistry, Depends(get_registry)],
) -> dict[str, Any]:
    return {"items": [_run_summary(run) for run in run_registry.list_runs()]}


@router.get("/data-quality")
def data_quality() -> dict[str, Any]:
    return _placeholder("data-quality")


@router.get("/queries")
def queries() -> dict[str, Any]:
    return _placeholder("queries")


@router.get("/queries/{query_id}")
def query_detail(query_id: str) -> dict[str, Any]:
    return _placeholder("query-detail", query_id=query_id)


@router.get("/products")
def products() -> dict[str, Any]:
    return _placeholder("products")


@router.get("/products/{product_id}")
def product_detail(product_id: str) -> dict[str, Any]:
    return _placeholder("product-detail", product_id=product_id)


@router.get("/sellers")
def sellers() -> dict[str, Any]:
    return _placeholder("sellers")


@router.get("/sellers/{seller_id}")
def seller_detail(seller_id: str) -> dict[str, Any]:
    return _placeholder("seller-detail", seller_id=seller_id)


@router.get("/marketplaces/compare")
def marketplace_compare() -> dict[str, Any]:
    return _placeholder("marketplaces-compare")


@router.get("/signals")
def signals() -> dict[str, Any]:
    return _placeholder("signals")


@router.get("/export")
def export() -> dict[str, Any]:
    return _placeholder("export")


def _placeholder(surface: str, **extra: str) -> dict[str, Any]:
    return {
        "surface": surface,
        "status": "placeholder",
        "message": "Skeleton endpoint; analytics implementation is out of scope.",
        **extra,
    }


def _run_summary(run) -> dict[str, Any] | None:
    if run is None:
        return None
    return {
        "run_id": run.identity.run_id,
        "marketplace": run.identity.provider.marketplace.value,
        "source_system": run.identity.provider.source_system.value,
        "schema_version": run.schema_version,
        "status": run.status.value,
        "usability_status": run.usability_status.value,
        "export_created_at_utc": run.export_created_at_utc,
        "imported_at_utc": run.imported_at_utc,
        "warnings": run.warnings,
        "errors": run.errors,
        "row_counts": run.row_counts,
    }
