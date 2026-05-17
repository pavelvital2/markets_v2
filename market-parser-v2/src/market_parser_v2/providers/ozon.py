"""Ozon provider boundary placeholder.

No browser automation or marketplace scraping logic is implemented here.
"""

from __future__ import annotations

from market_parser_v2.providers.base import ProviderPlan


class OzonProvider:
    provider_id = "ozon"
    marketplace = "ozon"

    def build_plan(self) -> ProviderPlan:
        return ProviderPlan(
            provider_id=self.provider_id,
            marketplace=self.marketplace,
            components=("suggest", "filter", "serp", "sellers", "export"),
            live_scraping_enabled=False,
            status="not_ready",
            notes=(
                "placeholder only",
                "future implementation must keep cookies path-based and never log cookie content",
                "future implementation must preserve partial/failure status for anti-bot and empty pages",
            ),
        )
