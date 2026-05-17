"""Data-quality status placeholders."""

from __future__ import annotations

from dataclasses import dataclass


RUN_STATUSES = ("success", "partial", "failed")
REPORT_USABILITY_STATUSES = ("valid_for_reports", "partial_use_with_warning", "invalid_for_reports")
SOURCE_ROW_STATUSES = ("success", "empty", "error", "dry_run", "partial", "failed", "not_ready")


@dataclass(frozen=True)
class QualitySummary:
    run_status: str
    report_usability: str
    warnings: tuple[str, ...] = ()
    errors: tuple[str, ...] = ()
    data_confidence_level: float | None = None
