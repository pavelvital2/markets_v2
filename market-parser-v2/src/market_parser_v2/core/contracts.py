"""Contract validation skeleton for provider-aware parser rows and manifests."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from market_parser_v2.core.constants import MANDATORY_SERVICE_FIELDS, SCHEMA_VERSION, SUPPORTED_PROVIDER_IDS


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    message: str
    field: str | None = None


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    issues: tuple[ValidationIssue, ...] = field(default_factory=tuple)

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "issues": [
                {"code": issue.code, "message": issue.message, "field": issue.field}
                for issue in self.issues
            ],
        }


def validate_contract_rows(
    rows: list[dict[str, Any]],
    *,
    source_system: str,
    schema_version: str = SCHEMA_VERSION,
) -> ValidationResult:
    issues: list[ValidationIssue] = []
    if source_system not in SUPPORTED_PROVIDER_IDS:
        issues.append(ValidationIssue("invalid_provider", f"unsupported provider: {source_system}", "source_system"))

    seen_positions: set[tuple[str, str, Any, Any]] = set()
    for index, row in enumerate(rows):
        row_ref = f"rows[{index}]"
        for field_name in MANDATORY_SERVICE_FIELDS:
            if field_name not in row:
                issues.append(ValidationIssue("missing_field", f"{row_ref} missing {field_name}", field_name))

        if row.get("source_system") != source_system:
            issues.append(
                ValidationIssue(
                    "provider_identity_mismatch",
                    f"{row_ref} source_system does not match requested provider",
                    "source_system",
                )
            )

        if row.get("schema_version") != schema_version:
            issues.append(
                ValidationIssue("schema_version_mismatch", f"{row_ref} schema_version is unsupported", "schema_version")
            )

        if not row.get("run_id"):
            issues.append(ValidationIssue("missing_run_id", f"{row_ref} run_id is absent", "run_id"))

        position_key = _position_key(row)
        if position_key:
            if position_key in seen_positions:
                issues.append(
                    ValidationIssue("duplicate_product_position", f"{row_ref} duplicates product position", None)
                )
            seen_positions.add(position_key)

    return ValidationResult(ok=not issues, issues=tuple(issues))


def validate_manifest(manifest: dict[str, Any], *, source_system: str) -> ValidationResult:
    required = (
        "marketplace",
        "source_system",
        "run_id",
        "schema_version",
        "export_created_at_utc",
        "component_statuses",
        "file_list",
        "row_counts",
        "checksums",
        "data_quality_summary",
        "usable_for_reports",
        "warnings",
        "errors",
    )
    issues = [ValidationIssue("missing_manifest_field", f"manifest missing {name}", name) for name in required if name not in manifest]
    if manifest.get("source_system") != source_system:
        issues.append(ValidationIssue("provider_identity_mismatch", "manifest source_system mismatch", "source_system"))
    if manifest.get("schema_version") != SCHEMA_VERSION:
        issues.append(ValidationIssue("schema_version_mismatch", "manifest schema_version mismatch", "schema_version"))
    if not manifest.get("run_id"):
        issues.append(ValidationIssue("missing_run_id", "manifest run_id is absent", "run_id"))
    return ValidationResult(ok=not issues, issues=tuple(issues))


def synthetic_contract_row(*, source_system: str, run_id: str) -> dict[str, Any]:
    now = datetime.now(UTC).isoformat()
    return {
        "marketplace": source_system,
        "source_system": source_system,
        "run_id": run_id,
        "component": "synthetic",
        "collected_at_utc": now,
        "source_type": "synthetic_fixture",
        "source_ref": "tests/synthetic",
        "status": "success",
        "error_message": "",
        "schema_version": SCHEMA_VERSION,
        "query": "synthetic query",
        "external_product_id": f"{source_system}-product-1",
        "external_seller_id": f"{source_system}-seller-1",
        "absolute_position": 1,
        "data_quality_status": "valid_for_reports",
    }


def _position_key(row: dict[str, Any]) -> tuple[str, str, Any, Any] | None:
    required = ("source_system", "query", "absolute_position", "run_id")
    if not all(row.get(name) is not None for name in required):
        return None
    return (
        str(row["source_system"]),
        str(row["query"]),
        row["absolute_position"],
        row["run_id"],
    )
