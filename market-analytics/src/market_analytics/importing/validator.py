from __future__ import annotations

from dataclasses import dataclass, field
import hashlib
import json
from pathlib import Path
import tarfile
from typing import Any

from market_analytics.config import Settings, load_settings
from market_analytics.models import Marketplace, SourceSystem


REQUIRED_MANIFEST_FIELDS = {
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
}

REQUIRED_USABLE_MARTS = {
    "marts/queries.csv",
    "marts/products.csv",
    "marts/sellers.csv",
    "marts/seller_query_product_bridge.csv",
    "quality/data_quality_summary.json",
    "metadata/contract.json",
}

SECRET_LIKE_PARTS = {
    "cookie",
    "cookies",
    "secret",
    "secrets",
    "token",
    "tokens",
    "credential",
    "credentials",
    "har",
    "browser_profile",
    "profile",
    "raw_html",
    "raw_json",
    "log",
    "logs",
    "tmp",
    "temp",
}


@dataclass(frozen=True)
class ExportBundlePaths:
    manifest_path: Path
    bundle_path: Path
    checksums_path: Path


@dataclass
class ValidationIssue:
    code: str
    message: str
    path: str | None = None


@dataclass
class BundleValidationResult:
    valid: bool
    manifest: dict[str, Any] | None = None
    issues: list[ValidationIssue] = field(default_factory=list)

    @property
    def warnings(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if issue.code.startswith("warning.")]

    @property
    def errors(self) -> list[ValidationIssue]:
        return [issue for issue in self.issues if not issue.code.startswith("warning.")]


class ExportBundleValidator:
    def __init__(self, settings: Settings | None = None) -> None:
        self._settings = settings or load_settings()

    def validate(self, paths: ExportBundlePaths) -> BundleValidationResult:
        issues: list[ValidationIssue] = []
        manifest = self._read_manifest(paths.manifest_path, issues)
        checksum_file = self._read_checksum_file(paths.checksums_path, issues)
        bundle_checksums = self._read_bundle_checksums(paths.bundle_path, issues)

        if manifest is not None:
            self._validate_manifest(manifest, issues)
            self._validate_required_files(manifest, bundle_checksums, issues)
            self._validate_secret_like_paths(manifest, bundle_checksums, issues)

        self._validate_checksum_sets(manifest, checksum_file, bundle_checksums, issues)

        return BundleValidationResult(
            valid=not [issue for issue in issues if not issue.code.startswith("warning.")],
            manifest=manifest,
            issues=issues,
        )

    def _read_manifest(
        self, manifest_path: Path, issues: list[ValidationIssue]
    ) -> dict[str, Any] | None:
        if not manifest_path.is_file():
            issues.append(ValidationIssue("manifest.missing", "manifest.json is missing."))
            return None
        try:
            return json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(ValidationIssue("manifest.invalid_json", str(exc)))
            return None

    def _read_checksum_file(
        self, checksums_path: Path, issues: list[ValidationIssue]
    ) -> dict[str, str]:
        if not checksums_path.is_file():
            issues.append(ValidationIssue("checksums.missing", "checksums.sha256 is missing."))
            return {}

        checksums: dict[str, str] = {}
        try:
            lines = checksums_path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            issues.append(ValidationIssue("checksums.unreadable", str(exc)))
            return {}

        for line_number, line in enumerate(lines, start=1):
            stripped = line.strip()
            if not stripped:
                continue
            parts = stripped.split(maxsplit=1)
            if len(parts) != 2:
                issues.append(
                    ValidationIssue(
                        "checksums.invalid_line",
                        f"Invalid checksum line {line_number}.",
                    )
                )
                continue
            digest, path = parts
            checksums[path.lstrip("*")] = digest
        return checksums

    def _read_bundle_checksums(
        self, bundle_path: Path, issues: list[ValidationIssue]
    ) -> dict[str, str]:
        if not bundle_path.is_file():
            issues.append(ValidationIssue("bundle.missing", "bundle.tar.gz is missing."))
            return {}

        checksums: dict[str, str] = {}
        try:
            with tarfile.open(bundle_path, mode="r:gz") as bundle:
                for member in bundle.getmembers():
                    if not member.isfile():
                        continue
                    normalized_name = member.name.lstrip("./")
                    file_obj = bundle.extractfile(member)
                    if file_obj is None:
                        issues.append(
                            ValidationIssue(
                                "bundle.member_unreadable",
                                "Bundle member could not be read.",
                                normalized_name,
                            )
                        )
                        continue
                    checksums[normalized_name] = hashlib.sha256(file_obj.read()).hexdigest()
        except (OSError, tarfile.TarError) as exc:
            issues.append(ValidationIssue("bundle.invalid_tar", str(exc)))
        return checksums

    def _validate_manifest(self, manifest: dict[str, Any], issues: list[ValidationIssue]) -> None:
        missing = sorted(REQUIRED_MANIFEST_FIELDS.difference(manifest))
        for field_name in missing:
            issues.append(
                ValidationIssue(
                    "manifest.missing_field",
                    f"Manifest is missing required field {field_name}.",
                    field_name,
                )
            )

        if not manifest.get("run_id"):
            issues.append(ValidationIssue("manifest.invalid_run_id", "run_id is required."))

        marketplace = manifest.get("marketplace")
        source_system = manifest.get("source_system")
        if marketplace not in {item.value for item in Marketplace}:
            issues.append(
                ValidationIssue(
                    "manifest.invalid_marketplace",
                    f"Unsupported marketplace {marketplace!r}.",
                )
            )
        if source_system not in {item.value for item in SourceSystem}:
            issues.append(
                ValidationIssue(
                    "manifest.invalid_source_system",
                    f"Unsupported source_system {source_system!r}.",
                )
            )
        if marketplace and source_system and marketplace != source_system:
            issues.append(
                ValidationIssue(
                    "manifest.provider_mismatch",
                    "marketplace and source_system must match in the current contract.",
                )
            )

        schema_version = manifest.get("schema_version")
        if schema_version not in self._settings.supported_schema_versions:
            issues.append(
                ValidationIssue(
                    "manifest.unsupported_schema_version",
                    f"Unsupported schema_version {schema_version!r}.",
                )
            )

    def _validate_required_files(
        self,
        manifest: dict[str, Any],
        bundle_checksums: dict[str, str],
        issues: list[ValidationIssue],
    ) -> None:
        file_list = set(_string_list(manifest.get("file_list")))
        if not file_list and bundle_checksums:
            issues.append(ValidationIssue("manifest.empty_file_list", "file_list is empty."))

        usable = manifest.get("usable_for_reports")
        if usable is True:
            missing = sorted(REQUIRED_USABLE_MARTS.difference(file_list))
            for path in missing:
                issues.append(
                    ValidationIssue(
                        "manifest.missing_required_mart",
                        "Usable bundle is missing a required analytics file.",
                        path,
                    )
                )

        for path in sorted(file_list.difference(bundle_checksums)):
            issues.append(
                ValidationIssue(
                    "bundle.file_list_missing_from_bundle",
                    "Manifest file_list entry is absent from bundle.",
                    path,
                )
            )

    def _validate_secret_like_paths(
        self,
        manifest: dict[str, Any],
        bundle_checksums: dict[str, str],
        issues: list[ValidationIssue],
    ) -> None:
        candidate_paths = set(_string_list(manifest.get("file_list"))) | set(bundle_checksums)
        for path in sorted(candidate_paths):
            path_parts = {part.lower() for part in Path(path).parts}
            stem_parts = set(Path(path).stem.lower().replace("-", "_").split("_"))
            suffix = Path(path).suffix.lower().lstrip(".")
            if (path_parts | stem_parts | {suffix}).intersection(SECRET_LIKE_PARTS):
                issues.append(
                    ValidationIssue(
                        "bundle.forbidden_secret_like_path",
                        "Bundle contains a forbidden secret-like or raw/runtime path.",
                        path,
                    )
                )

    def _validate_checksum_sets(
        self,
        manifest: dict[str, Any] | None,
        checksum_file: dict[str, str],
        bundle_checksums: dict[str, str],
        issues: list[ValidationIssue],
    ) -> None:
        manifest_checksums = manifest.get("checksums") if manifest else None
        if manifest_checksums is not None and not isinstance(manifest_checksums, dict):
            issues.append(
                ValidationIssue("manifest.invalid_checksums", "checksums must be an object.")
            )
            manifest_checksums = {}

        expected_sets = [("checksums.sha256", checksum_file)]
        if isinstance(manifest_checksums, dict):
            expected_sets.append(("manifest.checksums", manifest_checksums))

        for source_name, expected in expected_sets:
            for path, expected_digest in expected.items():
                actual_digest = bundle_checksums.get(path)
                if actual_digest is None:
                    issues.append(
                        ValidationIssue(
                            f"{source_name}.missing_from_bundle",
                            "Checksummed file is absent from bundle.",
                            path,
                        )
                    )
                    continue
                if actual_digest != expected_digest:
                    issues.append(
                        ValidationIssue(
                            f"{source_name}.checksum_mismatch",
                            "Checksum mismatch.",
                            path,
                        )
                    )

        for path in sorted(set(bundle_checksums).difference(checksum_file)):
            issues.append(
                ValidationIssue(
                    "checksums.bundle_file_not_covered",
                    "Bundle file is not covered by checksums.sha256.",
                    path,
                )
            )


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]
