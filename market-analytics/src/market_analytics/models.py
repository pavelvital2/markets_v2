from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import StrEnum
from typing import Any


class Marketplace(StrEnum):
    WB = "wb"
    OZON = "ozon"


class SourceSystem(StrEnum):
    WB = "wb"
    OZON = "ozon"


class ImportStatus(StrEnum):
    PENDING = "pending"
    IMPORTED = "imported"
    QUARANTINED = "quarantined"


class UsabilityStatus(StrEnum):
    VALID_FOR_REPORTS = "valid_for_reports"
    PARTIAL_USE_WITH_WARNING = "partial_use_with_warning"
    INVALID_FOR_REPORTS = "invalid_for_reports"


@dataclass(frozen=True)
class ProviderRef:
    marketplace: Marketplace
    source_system: SourceSystem


@dataclass(frozen=True)
class RunIdentity:
    run_id: str
    provider: ProviderRef


@dataclass
class ImportRun:
    identity: RunIdentity
    schema_version: str
    status: ImportStatus
    usability_status: UsabilityStatus
    source_bundle_ref: str
    export_created_at_utc: str | None = None
    imported_at_utc: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    row_counts: dict[str, int] = field(default_factory=dict)
    component_statuses: dict[str, str] = field(default_factory=dict)
    data_quality_summary: dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class QueryAnalyticsPlaceholder:
    marketplace: Marketplace
    source_system: SourceSystem
    run_id: str
    query: str
    normalized_query: str | None = None
    query_group: str | None = None
    data_quality_status: str | None = None
    schema_version: str | None = None


@dataclass(frozen=True)
class ProductAnalyticsPlaceholder:
    marketplace: Marketplace
    source_system: SourceSystem
    run_id: str
    external_product_id: str
    query: str | None = None
    external_seller_id: str | None = None
    data_quality_status: str | None = None
    schema_version: str | None = None


@dataclass(frozen=True)
class SellerAnalyticsPlaceholder:
    marketplace: Marketplace
    source_system: SourceSystem
    run_id: str
    external_seller_id: str
    seller_name: str | None = None
    data_quality_status: str | None = None
    schema_version: str | None = None
