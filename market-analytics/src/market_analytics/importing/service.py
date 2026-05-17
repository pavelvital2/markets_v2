from __future__ import annotations

from pathlib import Path

from market_analytics.importing.validator import ExportBundlePaths, ExportBundleValidator
from market_analytics.models import (
    ImportRun,
    ImportStatus,
    Marketplace,
    ProviderRef,
    RunIdentity,
    SourceSystem,
    UsabilityStatus,
)
from market_analytics.registry import ImportedRunRegistry


class ImportService:
    """Placeholder import service around the accepted parser export bundle boundary."""

    def __init__(
        self,
        registry: ImportedRunRegistry,
        validator: ExportBundleValidator | None = None,
    ) -> None:
        self._registry = registry
        self._validator = validator or ExportBundleValidator()

    def validate_bundle(self, paths: ExportBundlePaths):
        return self._validator.validate(paths)

    def register_bundle(self, paths: ExportBundlePaths) -> ImportRun:
        result = self._validator.validate(paths)
        manifest = result.manifest or {}
        identity = RunIdentity(
            run_id=str(manifest.get("run_id") or "unknown"),
            provider=ProviderRef(
                marketplace=_marketplace_or_placeholder(manifest.get("marketplace")),
                source_system=_source_system_or_placeholder(manifest.get("source_system")),
            ),
        )

        run = ImportRun(
            identity=identity,
            schema_version=str(manifest.get("schema_version") or "unknown"),
            status=ImportStatus.IMPORTED if result.valid else ImportStatus.QUARANTINED,
            usability_status=_usability_from_manifest(manifest, result.valid),
            source_bundle_ref=str(Path(paths.bundle_path)),
            export_created_at_utc=manifest.get("export_created_at_utc"),
            warnings=list(manifest.get("warnings") or []),
            errors=[issue.message for issue in result.errors],
            row_counts=dict(manifest.get("row_counts") or {}),
            component_statuses=dict(manifest.get("component_statuses") or {}),
            data_quality_summary=dict(manifest.get("data_quality_summary") or {}),
        )
        return self._registry.upsert(run)


def _usability_from_manifest(manifest: dict, valid: bool) -> UsabilityStatus:
    if not valid:
        return UsabilityStatus.INVALID_FOR_REPORTS
    if manifest.get("usable_for_reports") is True and not manifest.get("warnings"):
        return UsabilityStatus.VALID_FOR_REPORTS
    if manifest.get("usable_for_reports") is True:
        return UsabilityStatus.PARTIAL_USE_WITH_WARNING
    return UsabilityStatus.INVALID_FOR_REPORTS


def _marketplace_or_placeholder(value: object) -> Marketplace:
    return Marketplace(value) if value in {item.value for item in Marketplace} else Marketplace.WB


def _source_system_or_placeholder(value: object) -> SourceSystem:
    return SourceSystem(value) if value in {item.value for item in SourceSystem} else SourceSystem.WB
