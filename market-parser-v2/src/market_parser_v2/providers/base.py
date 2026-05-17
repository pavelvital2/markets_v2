"""Provider abstraction for parser V2."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class ProviderPlan:
    provider_id: str
    marketplace: str
    components: tuple[str, ...]
    live_scraping_enabled: bool
    status: str
    notes: tuple[str, ...] = ()

    def to_dict(self) -> dict[str, object]:
        return {
            "provider_id": self.provider_id,
            "marketplace": self.marketplace,
            "components": list(self.components),
            "live_scraping_enabled": self.live_scraping_enabled,
            "status": self.status,
            "notes": list(self.notes),
        }


class Provider(Protocol):
    provider_id: str
    marketplace: str

    def build_plan(self) -> ProviderPlan:
        """Return an offline execution plan skeleton."""
