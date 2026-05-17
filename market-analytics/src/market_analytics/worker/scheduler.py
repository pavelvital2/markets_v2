from __future__ import annotations

from dataclasses import dataclass

from market_analytics.importing.service import ImportService


@dataclass(frozen=True)
class SchedulerTickResult:
    scheduled_imports: int
    message: str


class ImportScheduler:
    """Scheduler placeholder.

    Production scheduling will discover parser export bundles through an accepted
    export source configuration, not by reading parser internal folders.
    """

    def __init__(self, import_service: ImportService) -> None:
        self._import_service = import_service

    def tick(self) -> SchedulerTickResult:
        return SchedulerTickResult(
            scheduled_imports=0,
            message="No import source is configured in the skeleton.",
        )
