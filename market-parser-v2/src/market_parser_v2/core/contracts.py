"""Provider-aware parser contract validation and compatibility mapping."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any

from market_parser_v2.core.constants import (
    MANIFEST_REQUIRED_FIELDS,
    MANDATORY_SERVICE_FIELDS,
    MART_FIELDS,
    REQUIRED_EXPORT_FILES,
    SCHEMA_VERSION,
    SUPPORTED_PROVIDER_IDS,
    SUPPORTED_SCHEMA_VERSIONS,
)


@dataclass(frozen=True)
class ValidationIssue:
    code: str
    message: str
    field: str | None = None


@dataclass(frozen=True)
class ValidationResult:
    ok: bool
    issues: tuple[ValidationIssue, ...] = field(default_factory=tuple)
    action: str = "accept"

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "action": self.action,
            "issues": [
                {"code": issue.code, "message": issue.message, "field": issue.field}
                for issue in self.issues
            ],
        }


@dataclass(frozen=True)
class ProviderScopedId:
    source_system: str
    external_id: str
    source_field: str

    @property
    def join_key(self) -> tuple[str, str]:
        return (self.source_system, self.external_id)

    def to_dict(self) -> dict[str, str]:
        return {
            "source_system": self.source_system,
            "external_id": self.external_id,
            "source_field": self.source_field,
        }


@dataclass(frozen=True)
class MartSchema:
    name: str
    fields: tuple[str, ...]

    def to_dict(self) -> dict[str, Any]:
        return {"name": self.name, "fields": list(self.fields)}


COMMON_MART_SCHEMAS: dict[str, MartSchema] = {
    name: MartSchema(name=name, fields=fields) for name, fields in MART_FIELDS.items()
}


def validate_provider_identity(source_system: str | None, *, invalid_action: str = "reject") -> ValidationResult:
    if source_system in SUPPORTED_PROVIDER_IDS:
        return ValidationResult(ok=True)
    return ValidationResult(
        ok=False,
        action=_invalid_action(invalid_action),
        issues=(
            ValidationIssue("invalid_provider", f"unsupported provider: {source_system}", "source_system"),
        ),
    )


def normalize_source_system(source_system: str) -> str:
    """Normalize known provider aliases before common mart emission."""

    if source_system == "wildberries":
        return "wb"
    if source_system in SUPPORTED_PROVIDER_IDS:
        return source_system
    raise ValueError(f"unsupported provider: {source_system}")


def validate_schema_version(schema_version: str | None, *, unsupported_action: str = "reject") -> ValidationResult:
    if schema_version in SUPPORTED_SCHEMA_VERSIONS:
        return ValidationResult(ok=True)
    return ValidationResult(
        ok=False,
        action=_invalid_action(unsupported_action),
        issues=(
            ValidationIssue(
                "schema_version_mismatch",
                f"unsupported schema_version: {schema_version}",
                "schema_version",
            ),
        ),
    )


def map_external_product_id(
    *,
    source_system: str | None,
    nm_id: Any | None = None,
    product_id: Any | None = None,
) -> ProviderScopedId:
    provider = _require_provider_context(source_system)
    if provider == "wb":
        value = _require_identifier(nm_id, source_field="nmId")
        return ProviderScopedId(source_system=provider, external_id=value, source_field="nmId")
    value = _require_identifier(product_id if product_id is not None else nm_id, source_field="ozon_product_id")
    source_field = "product_id" if product_id is not None else "ozon_compat_nmId"
    return ProviderScopedId(source_system=provider, external_id=value, source_field=source_field)


def map_external_seller_id(*, source_system: str | None, supplier_id: Any | None) -> ProviderScopedId:
    provider = _require_provider_context(source_system)
    value = _require_identifier(supplier_id, source_field="supplier_id")
    return ProviderScopedId(source_system=provider, external_id=value, source_field="supplier_id")


def validate_contract_rows(
    rows: list[dict[str, Any]],
    *,
    source_system: str,
    schema_version: str = SCHEMA_VERSION,
    invalid_action: str = "reject",
) -> ValidationResult:
    issues: list[ValidationIssue] = []
    action = "accept"
    provider_result = validate_provider_identity(source_system, invalid_action=invalid_action)
    if not provider_result.ok:
        issues.extend(provider_result.issues)
        action = provider_result.action

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

        version_result = validate_schema_version(row.get("schema_version"), unsupported_action=invalid_action)
        if row.get("schema_version") != schema_version or not version_result.ok:
            issues.extend(
                ValidationIssue(issue.code, f"{row_ref} {issue.message}", issue.field)
                for issue in version_result.issues
            )
            if version_result.action != "accept":
                action = version_result.action

        if not row.get("run_id"):
            issues.append(ValidationIssue("missing_run_id", f"{row_ref} run_id is absent", "run_id"))

        position_key = _position_key(row)
        if position_key:
            if position_key in seen_positions:
                issues.append(
                    ValidationIssue("duplicate_product_position", f"{row_ref} duplicates product position", None)
                )
            seen_positions.add(position_key)

    return ValidationResult(ok=not issues, issues=tuple(issues), action="accept" if not issues else action)


def validate_mart_rows(
    mart_name: str,
    rows: list[dict[str, Any]],
    *,
    source_system: str,
    strict: bool = True,
    seller_data_expected: bool = False,
    invalid_action: str = "reject",
) -> ValidationResult:
    schema = COMMON_MART_SCHEMAS.get(mart_name)
    if schema is None:
        return ValidationResult(
            ok=False,
            action=_invalid_action(invalid_action),
            issues=(ValidationIssue("unknown_mart", f"unknown mart: {mart_name}", None),),
        )

    issues: list[ValidationIssue] = []
    action = "accept"
    provider_result = validate_provider_identity(source_system, invalid_action=invalid_action)
    if not provider_result.ok:
        issues.extend(provider_result.issues)
        action = provider_result.action

    allowed_fields = set(schema.fields)
    seen_positions: set[tuple[str, str, Any, Any]] = set()
    for index, row in enumerate(rows):
        row_ref = f"rows[{index}]"
        for field_name in schema.fields:
            if field_name not in row:
                issues.append(ValidationIssue("missing_field", f"{row_ref} missing {field_name}", field_name))

        if strict:
            for field_name in sorted(set(row) - allowed_fields):
                issues.append(
                    ValidationIssue("unexpected_field", f"{row_ref} has unexpected field {field_name}", field_name)
                )

        if row.get("source_system") != source_system:
            issues.append(
                ValidationIssue(
                    "provider_identity_mismatch",
                    f"{row_ref} source_system does not match requested provider",
                    "source_system",
                )
            )
        if row.get("marketplace") != source_system:
            issues.append(
                ValidationIssue("provider_identity_mismatch", f"{row_ref} marketplace mismatch", "marketplace")
            )

        version_result = validate_schema_version(row.get("schema_version"), unsupported_action=invalid_action)
        if not version_result.ok:
            issues.extend(
                ValidationIssue(issue.code, f"{row_ref} {issue.message}", issue.field)
                for issue in version_result.issues
            )
            action = version_result.action

        if not row.get("run_id"):
            issues.append(ValidationIssue("missing_run_id", f"{row_ref} run_id is absent", "run_id"))
        if "data_quality_status" in schema.fields and not row.get("data_quality_status"):
            issues.append(
                ValidationIssue("missing_data_quality_status", f"{row_ref} data_quality_status is absent", None)
            )
        if mart_name in {"products", "seller_query_product_bridge"} and seller_data_expected:
            if not row.get("external_seller_id"):
                issues.append(ValidationIssue("missing_seller_id", f"{row_ref} seller id is absent", None))

        position_key = _position_key(row)
        if position_key:
            if position_key in seen_positions:
                issues.append(
                    ValidationIssue("duplicate_product_position", f"{row_ref} duplicates product position", None)
                )
            seen_positions.add(position_key)

    return ValidationResult(ok=not issues, issues=tuple(issues), action="accept" if not issues else action)


def validate_manifest(
    manifest: dict[str, Any],
    *,
    source_system: str,
    unsupported_schema_action: str = "reject",
) -> ValidationResult:
    issues = [
        ValidationIssue("missing_manifest_field", f"manifest missing {name}", name)
        for name in MANIFEST_REQUIRED_FIELDS
        if name not in manifest
    ]
    action = "accept"

    provider_result = validate_provider_identity(manifest.get("source_system"), invalid_action="reject")
    if not provider_result.ok:
        issues.extend(provider_result.issues)
        action = provider_result.action
    if manifest.get("source_system") != source_system:
        issues.append(ValidationIssue("provider_identity_mismatch", "manifest source_system mismatch", "source_system"))
    if manifest.get("marketplace") != source_system:
        issues.append(ValidationIssue("provider_identity_mismatch", "manifest marketplace mismatch", "marketplace"))

    version_result = validate_schema_version(
        manifest.get("schema_version"),
        unsupported_action=unsupported_schema_action,
    )
    if not version_result.ok:
        issues.extend(version_result.issues)
        action = version_result.action

    if not manifest.get("run_id"):
        issues.append(ValidationIssue("missing_run_id", "manifest run_id is absent", "run_id"))

    file_list = set(manifest.get("file_list") or ())
    missing_files = sorted(set(REQUIRED_EXPORT_FILES) - file_list)
    if manifest.get("usable_for_reports") != "invalid_for_reports":
        for missing_file in missing_files:
            issues.append(
                ValidationIssue("missing_required_export_file", f"manifest file_list missing {missing_file}", "file_list")
            )

    return ValidationResult(ok=not issues, issues=tuple(issues), action="accept" if not issues else action)


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


def synthetic_mart_row(*, mart_name: str, source_system: str, run_id: str) -> dict[str, Any]:
    fields = COMMON_MART_SCHEMAS[mart_name].fields
    row: dict[str, Any] = {field_name: "" for field_name in fields}
    row.update(
        {
            "marketplace": source_system,
            "source_system": source_system,
            "run_id": run_id,
            "schema_version": SCHEMA_VERSION,
            "data_quality_status": "valid_for_reports",
            "query": "synthetic query",
            "query_group": "synthetic",
            "external_product_id": "product-1",
            "external_seller_id": "seller-1",
            "seller_name": "Synthetic seller",
            "product_run_id": f"{run_id}:product-1",
        }
    )
    if mart_name == "queries":
        row.update({"normalized_query": "synthetic query", "canonical_query": "synthetic query"})
    if mart_name == "products":
        row.update({"page": 1, "position_on_page": 1, "absolute_position": 1, "product_name": "Synthetic product"})
    return {field_name: row.get(field_name, "") for field_name in fields}


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


def _require_provider_context(source_system: str | None) -> str:
    if not source_system:
        raise ValueError("provider context is required for compatibility id mapping")
    provider = normalize_source_system(source_system)
    if provider not in SUPPORTED_PROVIDER_IDS:
        raise ValueError(f"unsupported provider: {source_system}")
    return provider


def _require_identifier(value: Any | None, *, source_field: str) -> str:
    if value is None or value == "":
        raise ValueError(f"{source_field} is required")
    return str(value)


def _invalid_action(action: str) -> str:
    if action not in {"reject", "quarantine"}:
        raise ValueError(f"unsupported invalid action: {action}")
    return action
