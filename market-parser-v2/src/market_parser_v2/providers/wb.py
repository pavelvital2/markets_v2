"""WB provider boundary placeholder.

No source project logic is copied or migrated in this skeleton.
"""

from __future__ import annotations

from market_parser_v2.providers.base import ProviderPlan


class WbProvider:
    provider_id = "wb"
    marketplace = "wb"

    def build_plan(self) -> ProviderPlan:
        return ProviderPlan(
            provider_id=self.provider_id,
            marketplace=self.marketplace,
            components=("suggest", "filter", "serp", "sellers", "export"),
            live_scraping_enabled=False,
            status="not_ready",
            notes=(
                "placeholder only",
                "future implementation must normalize any source wildberries identity to wb",
                "future implementation must preserve run-scoped outputs and latest mirrors",
            ),
        )
