"""Data-quality status mapping for parser runs and export bundles."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


RUN_STATUSES = ("success", "partial", "failed")
REPORT_USABILITY_STATUSES = ("valid_for_reports", "partial_use_with_warning", "invalid_for_reports")
SOURCE_ROW_STATUSES = ("success", "empty", "error", "dry_run", "partial", "failed", "not_ready")

_SOURCE_STATUS_TO_RUN_STATUS = {
    "success": "success",
    "empty": "partial",
    "partial": "partial",
    "dry_run": "partial",
    "error": "failed",
    "failed": "failed",
    "not_ready": "failed",
}

_SOURCE_STATUS_TO_USABILITY = {
    "success": "valid_for_reports",
    "empty": "partial_use_with_warning",
    "partial": "partial_use_with_warning",
    "dry_run": "invalid_for_reports",
    "error": "invalid_for_reports",
    "failed": "invalid_for_reports",
    "not_ready": "invalid_for_reports",
}


@dataclass(frozen=True)
class ComponentQuality:
    component: str
    source_status: str
    run_status: str
    report_usability: str

    def to_dict(self) -> dict[str, str]:
        return {
            "component": self.component,
            "source_status": self.source_status,
            "run_status": self.run_status,
            "report_usability": self.report_usability,
        }


@dataclass(frozen=True)
class QualitySummary:
    run_id: str
    marketplace: str
    source_system: str
    run_status: str
    report_usability: str
    component_statuses: dict[str, ComponentQuality]
    row_status_counts: dict[str, int]
    export_status: str
    warnings: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()
    data_confidence_level: float | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "marketplace": self.marketplace,
            "source_system": self.source_system,
            "run_status": self.run_status,
            "report_usability": self.report_usability,
            "component_statuses": {
                name: quality.to_dict() for name, quality in sorted(self.component_statuses.items())
            },
            "row_status_counts": dict(sorted(self.row_status_counts.items())),
            "export_status": self.export_status,
            "warnings": list(self.warnings),
            "errors": list(self.errors),
            "data_confidence_level": self.data_confidence_level,
        }


def map_source_status(source_status: str) -> tuple[str, str]:
    if source_status not in SOURCE_ROW_STATUSES:
        return ("failed", "invalid_for_reports")
    return (_SOURCE_STATUS_TO_RUN_STATUS[source_status], _SOURCE_STATUS_TO_USABILITY[source_status])


def summarize_data_quality(
    *,
    run_id: str,
    marketplace: str,
    source_system: str,
    component_statuses: dict[str, str],
    row_statuses: tuple[str, ...] = (),
    export_errors: tuple[str, ...] = (),
) -> QualitySummary:
    component_quality = {
        name: ComponentQuality(
            component=name,
            source_status=status,
            run_status=map_source_status(status)[0],
            report_usability=map_source_status(status)[1],
        )
        for name, status in component_statuses.items()
    }
    row_counts: dict[str, int] = {}
    for status in row_statuses:
        row_counts[status] = row_counts.get(status, 0) + 1

    status_inputs = [quality.run_status for quality in component_quality.values()]
    status_inputs.extend(map_source_status(status)[0] for status in row_statuses)
    export_status = "failed" if export_errors else "success"
    status_inputs.append(export_status)

    run_status = _aggregate_run_status(tuple(status_inputs))
    report_usability = _report_usability_for_run_status(run_status)
    warnings = _warnings_for_quality(component_quality, row_counts, export_errors)
    errors = tuple(export_errors)
    if any(quality.report_usability == "invalid_for_reports" for quality in component_quality.values()):
        if run_status == "failed":
            report_usability = "invalid_for_reports"
    return QualitySummary(
        run_id=run_id,
        marketplace=marketplace,
        source_system=source_system,
        run_status=run_status,
        report_usability=report_usability,
        component_statuses=component_quality,
        row_status_counts=row_counts,
        export_status=export_status,
        warnings=warnings,
        errors=errors,
        data_confidence_level=None,
    )


def _aggregate_run_status(statuses: tuple[str, ...]) -> str:
    if not statuses:
        return "failed"
    if all(status == "success" for status in statuses):
        return "success"
    if any(status == "success" for status in statuses) or any(status == "partial" for status in statuses):
        return "partial"
    return "failed"


def _report_usability_for_run_status(run_status: str) -> str:
    if run_status == "success":
        return "valid_for_reports"
    if run_status == "partial":
        return "partial_use_with_warning"
    return "invalid_for_reports"


def _warnings_for_quality(
    component_quality: dict[str, ComponentQuality],
    row_counts: dict[str, int],
    export_errors: tuple[str, ...],
) -> tuple[str, ...]:
    warnings: list[str] = []
    for name, quality in sorted(component_quality.items()):
        if quality.run_status == "partial":
            warnings.append(f"component {name} is partial: {quality.source_status}")
        if quality.run_status == "failed":
            warnings.append(f"component {name} failed: {quality.source_status}")
    for status, count in sorted(row_counts.items()):
        if map_source_status(status)[0] != "success":
            warnings.append(f"{count} row(s) have {status} status")
    if export_errors:
        warnings.append("export has validation errors")
    return tuple(warnings)
