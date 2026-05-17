from __future__ import annotations

from collections.abc import Iterable

from market_analytics.models import ImportRun, RunIdentity


class ImportedRunRegistry:
    """Placeholder registry preserving imported run history in memory."""

    def __init__(self) -> None:
        self._runs: dict[tuple[str, str, str], ImportRun] = {}

    def upsert(self, run: ImportRun) -> ImportRun:
        key = self._key(run.identity)
        self._runs[key] = run
        return run

    def list_runs(self) -> list[ImportRun]:
        return sorted(self._runs.values(), key=lambda run: run.imported_at_utc, reverse=True)

    def latest(self) -> ImportRun | None:
        runs = self.list_runs()
        return runs[0] if runs else None

    def get(self, identity: RunIdentity) -> ImportRun | None:
        return self._runs.get(self._key(identity))

    def extend(self, runs: Iterable[ImportRun]) -> None:
        for run in runs:
            self.upsert(run)

    @staticmethod
    def _key(identity: RunIdentity) -> tuple[str, str, str]:
        return (
            identity.provider.marketplace.value,
            identity.provider.source_system.value,
            identity.run_id,
        )


registry = ImportedRunRegistry()
