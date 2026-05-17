"""Analytics export-bundle layout skeleton."""

from __future__ import annotations

import csv
import hashlib
import json
import tarfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.constants import (
    FORBIDDEN_EXPORT_CONTENT_MARKERS,
    FORBIDDEN_EXPORT_NAME_PARTS,
    REQUIRED_EXPORT_FILES,
    SCHEMA_VERSION,
)
from market_parser_v2.core.contracts import COMMON_MART_SCHEMAS, ValidationIssue, validate_manifest
from market_parser_v2.core.contracts import validate_mart_rows
from market_parser_v2.core.quality import summarize_data_quality


@dataclass(frozen=True)
class ExportSkeletonResult:
    latest_json: Path
    manifest_json: Path
    bundle_tar_gz: Path
    checksums_sha256: Path
    manifest_valid: bool
    validation_issues: tuple[ValidationIssue, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "latest_json": str(self.latest_json),
            "manifest_json": str(self.manifest_json),
            "bundle_tar_gz": str(self.bundle_tar_gz),
            "checksums_sha256": str(self.checksums_sha256),
            "manifest_valid": self.manifest_valid,
            "validation_issues": [
                {"code": issue.code, "message": issue.message, "field": issue.field}
                for issue in self.validation_issues
            ],
        }


@dataclass(frozen=True)
class ExportValidationResult:
    ok: bool
    manifest_valid: bool
    checksums_valid: bool
    latest_valid: bool
    forbidden_artifacts: tuple[str, ...]
    issues: tuple[ValidationIssue, ...] = ()

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "manifest_valid": self.manifest_valid,
            "checksums_valid": self.checksums_valid,
            "latest_valid": self.latest_valid,
            "forbidden_artifacts": list(self.forbidden_artifacts),
            "issues": [
                {"code": issue.code, "message": issue.message, "field": issue.field}
                for issue in self.issues
            ],
        }


def create_export_skeleton(*, config: ParserConfig, marketplace: str, run_id: str) -> ExportSkeletonResult:
    if marketplace not in {"wb", "ozon"}:
        raise ValueError(f"unsupported marketplace for export skeleton: {marketplace}")

    export_root = config.paths.export_path
    run_dir = export_root / marketplace / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory(dir=config.paths.temp_path if config.paths.temp_path.exists() else None) as temp_dir:
        bundle_root = Path(temp_dir) / "bundle"
        quality_summary = summarize_data_quality(
            run_id=run_id,
            marketplace=marketplace,
            source_system=marketplace,
            component_statuses={
                "suggest": "not_ready",
                "filter": "not_ready",
                "serp": "not_ready",
                "sellers": "not_ready",
                "export": "success",
            },
        )
        _write_placeholder_bundle_files(
            bundle_root,
            marketplace=marketplace,
            run_id=run_id,
            data_quality_summary=quality_summary.to_dict(),
        )
        checksums = _checksums_for_files(bundle_root, REQUIRED_EXPORT_FILES)
        _assert_export_file_names_safe(REQUIRED_EXPORT_FILES)

        bundle_path = run_dir / "bundle.tar.gz"
        with tarfile.open(bundle_path, "w:gz") as archive:
            for relative in REQUIRED_EXPORT_FILES:
                archive.add(bundle_root / relative, arcname=relative)

    manifest = _manifest_payload(
        marketplace=marketplace,
        run_id=run_id,
        checksums=checksums,
        data_quality_summary=quality_summary.to_dict(),
    )
    manifest_path = run_dir / "manifest.json"
    _write_json(manifest_path, manifest)

    checksums_path = run_dir / "checksums.sha256"
    checksums_path.write_text(
        "".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())),
        encoding="utf-8",
    )

    latest_path = export_root / "latest.json"
    _write_json(
        latest_path,
        {
            "marketplace": marketplace,
            "source_system": marketplace,
            "run_id": run_id,
            "schema_version": SCHEMA_VERSION,
            "manifest_path": f"{marketplace}/{run_id}/manifest.json",
            "bundle_path": f"{marketplace}/{run_id}/bundle.tar.gz",
            "checksums_path": f"{marketplace}/{run_id}/checksums.sha256",
            "updated_at_utc": datetime.now(UTC).isoformat(),
        },
    )

    validation = validate_export_artifacts(export_root=export_root, marketplace=marketplace, run_id=run_id)
    return ExportSkeletonResult(
        latest_json=latest_path,
        manifest_json=manifest_path,
        bundle_tar_gz=bundle_path,
        checksums_sha256=checksums_path,
        manifest_valid=validation.ok,
        validation_issues=validation.issues,
    )


def create_export_bundle(
    *,
    config: ParserConfig,
    marketplace: str,
    run_id: str,
    mart_rows: dict[str, list[dict[str, Any]]],
    component_statuses: dict[str, str],
    row_statuses: tuple[str, ...] = (),
    warnings: tuple[str, ...] = (),
    errors: tuple[str, ...] = (),
) -> ExportSkeletonResult:
    if marketplace not in {"wb", "ozon"}:
        raise ValueError(f"unsupported marketplace for export bundle: {marketplace}")

    export_root = config.paths.export_path
    run_dir = export_root / marketplace / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    normalized_marts = {
        name: _normalize_mart_rows(name, mart_rows.get(name, [])) for name in COMMON_MART_SCHEMAS
    }
    validation_issues: list[ValidationIssue] = []
    for mart_name, rows in normalized_marts.items():
        validation = validate_mart_rows(
            mart_name,
            rows,
            source_system=marketplace,
            seller_data_expected=mart_name in {"products", "seller_query_product_bridge"} and bool(rows),
        )
        validation_issues.extend(validation.issues)

    export_errors = tuple(errors) + tuple(issue.message for issue in validation_issues)
    quality_summary = summarize_data_quality(
        run_id=run_id,
        marketplace=marketplace,
        source_system=marketplace,
        component_statuses=component_statuses,
        row_statuses=row_statuses,
        export_errors=export_errors,
    )

    with TemporaryDirectory(dir=config.paths.temp_path if config.paths.temp_path.exists() else None) as temp_dir:
        bundle_root = Path(temp_dir) / "bundle"
        _write_bundle_files(
            bundle_root,
            marketplace=marketplace,
            run_id=run_id,
            mart_rows=normalized_marts,
            data_quality_summary=quality_summary.to_dict(),
        )
        checksums = _checksums_for_files(bundle_root, REQUIRED_EXPORT_FILES)
        _assert_export_file_names_safe(REQUIRED_EXPORT_FILES)

        bundle_path = run_dir / "bundle.tar.gz"
        with tarfile.open(bundle_path, "w:gz") as archive:
            for relative in REQUIRED_EXPORT_FILES:
                archive.add(bundle_root / relative, arcname=relative)

    manifest = _manifest_payload(
        marketplace=marketplace,
        run_id=run_id,
        checksums=checksums,
        data_quality_summary=quality_summary.to_dict(),
        component_statuses=component_statuses,
        row_counts={name: len(rows) for name, rows in normalized_marts.items()},
        usable_for_reports=quality_summary.report_usability,
        warnings=warnings + quality_summary.warnings,
        errors=export_errors,
    )
    manifest_path = run_dir / "manifest.json"
    _write_json(manifest_path, manifest)

    checksums_path = run_dir / "checksums.sha256"
    checksums_path.write_text(
        "".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())),
        encoding="utf-8",
    )

    latest_path = export_root / "latest.json"
    _write_json(
        latest_path,
        {
            "marketplace": marketplace,
            "source_system": marketplace,
            "run_id": run_id,
            "schema_version": SCHEMA_VERSION,
            "manifest_path": f"{marketplace}/{run_id}/manifest.json",
            "bundle_path": f"{marketplace}/{run_id}/bundle.tar.gz",
            "checksums_path": f"{marketplace}/{run_id}/checksums.sha256",
            "updated_at_utc": datetime.now(UTC).isoformat(),
        },
    )

    validation = validate_export_artifacts(export_root=export_root, marketplace=marketplace, run_id=run_id)
    return ExportSkeletonResult(
        latest_json=latest_path,
        manifest_json=manifest_path,
        bundle_tar_gz=bundle_path,
        checksums_sha256=checksums_path,
        manifest_valid=validation.ok,
        validation_issues=validation.issues,
    )


def validate_export_artifacts(*, export_root: Path, marketplace: str, run_id: str) -> ExportValidationResult:
    run_dir = export_root / marketplace / run_id
    latest_path = export_root / "latest.json"
    manifest_path = run_dir / "manifest.json"
    bundle_path = run_dir / "bundle.tar.gz"
    checksums_path = run_dir / "checksums.sha256"

    issues: list[ValidationIssue] = []
    forbidden_artifacts: list[str] = []
    manifest: dict[str, Any] = {}
    latest: dict[str, Any] = {}

    for path, field in (
        (latest_path, "latest.json"),
        (manifest_path, "manifest.json"),
        (bundle_path, "bundle.tar.gz"),
        (checksums_path, "checksums.sha256"),
    ):
        if not path.exists():
            issues.append(ValidationIssue("missing_export_artifact", f"missing {field}", field))

    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
        issues.extend(validate_manifest(manifest, source_system=marketplace).issues)

    if latest_path.exists():
        latest = json.loads(latest_path.read_text(encoding="utf-8"))
        expected_latest = {
            "manifest_path": f"{marketplace}/{run_id}/manifest.json",
            "bundle_path": f"{marketplace}/{run_id}/bundle.tar.gz",
            "checksums_path": f"{marketplace}/{run_id}/checksums.sha256",
        }
        for field, expected in expected_latest.items():
            if latest.get(field) != expected:
                issues.append(ValidationIssue("latest_pointer_mismatch", f"latest {field} mismatch", field))
        if latest.get("schema_version") != SCHEMA_VERSION:
            issues.append(ValidationIssue("schema_version_mismatch", "latest schema_version mismatch", "schema_version"))

    expected_checksums = _read_checksums_file(checksums_path) if checksums_path.exists() else {}
    manifest_checksums = manifest.get("checksums") or {}
    if manifest_checksums and manifest_checksums != expected_checksums:
        issues.append(ValidationIssue("checksum_manifest_mismatch", "manifest checksums differ from checksums file", None))

    archive_result = _validate_bundle_archive(bundle_path, expected_checksums)
    issues.extend(archive_result[0])
    forbidden_artifacts.extend(archive_result[1])

    manifest_valid = not any(issue.code.startswith("missing_manifest") for issue in issues) and not any(
        issue.field == "schema_version" or issue.field in {"source_system", "marketplace", "run_id"}
        for issue in issues
    )
    checksums_valid = not any("checksum" in issue.code for issue in issues)
    latest_valid = not any(issue.code == "latest_pointer_mismatch" for issue in issues)
    ok = not issues and not forbidden_artifacts
    return ExportValidationResult(
        ok=ok,
        manifest_valid=manifest_valid,
        checksums_valid=checksums_valid,
        latest_valid=latest_valid,
        forbidden_artifacts=tuple(forbidden_artifacts),
        issues=tuple(issues),
    )


def _write_placeholder_bundle_files(
    bundle_root: Path,
    *,
    marketplace: str,
    run_id: str,
    data_quality_summary: dict[str, Any],
) -> None:
    _write_csv(bundle_root / "marts/queries.csv", list(COMMON_MART_SCHEMAS["queries"].fields))
    _write_csv(bundle_root / "marts/products.csv", list(COMMON_MART_SCHEMAS["products"].fields))
    _write_csv(bundle_root / "marts/sellers.csv", list(COMMON_MART_SCHEMAS["sellers"].fields))
    _write_csv(
        bundle_root / "marts/seller_query_product_bridge.csv",
        list(COMMON_MART_SCHEMAS["seller_query_product_bridge"].fields),
    )
    _write_json(
        bundle_root / "quality/data_quality_summary.json",
        data_quality_summary | {"schema_version": SCHEMA_VERSION},
    )
    _write_json(
        bundle_root / "metadata/contract.json",
        {
            "schema_version": SCHEMA_VERSION,
            "source_system": marketplace,
            "required_files": list(REQUIRED_EXPORT_FILES),
        },
    )


def _write_bundle_files(
    bundle_root: Path,
    *,
    marketplace: str,
    run_id: str,
    mart_rows: dict[str, list[dict[str, Any]]],
    data_quality_summary: dict[str, Any],
) -> None:
    _write_csv_rows(
        bundle_root / "marts/queries.csv",
        list(COMMON_MART_SCHEMAS["queries"].fields),
        mart_rows["queries"],
    )
    _write_csv_rows(
        bundle_root / "marts/products.csv",
        list(COMMON_MART_SCHEMAS["products"].fields),
        mart_rows["products"],
    )
    _write_csv_rows(
        bundle_root / "marts/sellers.csv",
        list(COMMON_MART_SCHEMAS["sellers"].fields),
        mart_rows["sellers"],
    )
    _write_csv_rows(
        bundle_root / "marts/seller_query_product_bridge.csv",
        list(COMMON_MART_SCHEMAS["seller_query_product_bridge"].fields),
        mart_rows["seller_query_product_bridge"],
    )
    _write_json(
        bundle_root / "quality/data_quality_summary.json",
        data_quality_summary | {"schema_version": SCHEMA_VERSION},
    )
    _write_json(
        bundle_root / "metadata/contract.json",
        {
            "schema_version": SCHEMA_VERSION,
            "source_system": marketplace,
            "run_id": run_id,
            "required_files": list(REQUIRED_EXPORT_FILES),
            "marts": {name: list(schema.fields) for name, schema in sorted(COMMON_MART_SCHEMAS.items())},
        },
    )


def _manifest_payload(
    *,
    marketplace: str,
    run_id: str,
    checksums: dict[str, str],
    data_quality_summary: dict[str, Any],
    component_statuses: dict[str, str] | None = None,
    row_counts: dict[str, int] | None = None,
    usable_for_reports: str = "invalid_for_reports",
    warnings: tuple[str, ...] = ("skeleton export contains no collected marketplace rows",),
    errors: tuple[str, ...] = (),
) -> dict[str, Any]:
    return {
        "marketplace": marketplace,
        "source_system": marketplace,
        "run_id": run_id,
        "schema_version": SCHEMA_VERSION,
        "export_created_at_utc": datetime.now(UTC).isoformat(),
        "component_statuses": component_statuses or {
            "suggest": "not_ready",
            "filter": "not_ready",
            "serp": "not_ready",
            "sellers": "not_ready",
            "export": "success",
        },
        "file_list": list(REQUIRED_EXPORT_FILES),
        "row_counts": row_counts or {
            "queries": 0,
            "products": 0,
            "sellers": 0,
            "seller_query_product_bridge": 0,
        },
        "checksums": checksums,
        "data_quality_summary": data_quality_summary,
        "usable_for_reports": usable_for_reports,
        "warnings": list(warnings),
        "errors": list(errors),
    }


def _write_csv(path: Path, fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()


def _write_csv_rows(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fieldnames})


def _normalize_mart_rows(mart_name: str, rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    fields = COMMON_MART_SCHEMAS[mart_name].fields
    return [{field: row.get(field, "") for field in fields} for row in rows]


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _checksums_for_files(root: Path, relatives: tuple[str, ...]) -> dict[str, str]:
    checksums: dict[str, str] = {}
    for relative in relatives:
        checksums[relative] = hashlib.sha256((root / relative).read_bytes()).hexdigest()
    return checksums


def _assert_export_file_names_safe(relatives: tuple[str, ...]) -> None:
    for relative in relatives:
        lower = relative.lower()
        if any(part in lower for part in FORBIDDEN_EXPORT_NAME_PARTS):
            raise ValueError(f"forbidden export file name: {relative}")


def _read_checksums_file(path: Path) -> dict[str, str]:
    checksums: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        digest, relative = line.split(None, 1)
        checksums[relative.strip()] = digest
    return checksums


def _validate_bundle_archive(
    bundle_path: Path,
    expected_checksums: dict[str, str],
) -> tuple[list[ValidationIssue], list[str]]:
    issues: list[ValidationIssue] = []
    forbidden_artifacts: list[str] = []
    if not bundle_path.exists():
        return issues, forbidden_artifacts

    with tarfile.open(bundle_path, "r:gz") as archive:
        members = [member for member in archive.getmembers() if member.isfile()]
        names = [member.name for member in members]
        for name in names:
            if name.startswith("/") or ".." in Path(name).parts:
                issues.append(ValidationIssue("unsafe_bundle_path", f"unsafe bundle path {name}", "bundle"))
            if _is_forbidden_name(name):
                forbidden_artifacts.append(name)
                issues.append(ValidationIssue("forbidden_bundle_artifact", f"forbidden bundle artifact {name}", "bundle"))

        for required in REQUIRED_EXPORT_FILES:
            if required not in names:
                issues.append(ValidationIssue("missing_required_export_file", f"bundle missing {required}", "bundle"))
        for name in sorted(set(names) - set(REQUIRED_EXPORT_FILES)):
            issues.append(ValidationIssue("unexpected_bundle_file", f"bundle has unexpected file {name}", "bundle"))

        for member in members:
            extracted = archive.extractfile(member)
            payload = extracted.read() if extracted is not None else b""
            digest = hashlib.sha256(payload).hexdigest()
            if expected_checksums.get(member.name) != digest:
                issues.append(ValidationIssue("checksum_mismatch", f"checksum mismatch for {member.name}", "checksums"))
            if _contains_forbidden_content(payload):
                forbidden_artifacts.append(member.name)
                issues.append(
                    ValidationIssue("forbidden_bundle_content", f"forbidden content in {member.name}", "bundle")
                )

    for required in REQUIRED_EXPORT_FILES:
        if required not in expected_checksums:
            issues.append(ValidationIssue("missing_checksum", f"missing checksum for {required}", "checksums"))
    return issues, forbidden_artifacts


def _is_forbidden_name(relative: str) -> bool:
    lower = relative.lower()
    return any(part in lower for part in FORBIDDEN_EXPORT_NAME_PARTS)


def _contains_forbidden_content(payload: bytes) -> bool:
    lower = payload[:1024 * 1024].lower()
    return any(marker.encode("utf-8") in lower for marker in FORBIDDEN_EXPORT_CONTENT_MARKERS)
