from __future__ import annotations

import unittest

from market_parser_v2.core.registry import get_provider, resolve_marketplace


class RegistryTests(unittest.TestCase):
    def test_resolves_wb_ozon_and_all(self) -> None:
        self.assertEqual(resolve_marketplace("wb"), ("wb",))
        self.assertEqual(resolve_marketplace("ozon"), ("ozon",))
        self.assertEqual(resolve_marketplace("all"), ("wb", "ozon"))

    def test_registered_providers_are_offline_placeholders(self) -> None:
        for provider_id in resolve_marketplace("all"):
            plan = get_provider(provider_id).build_plan()
            self.assertFalse(plan.live_scraping_enabled)
            self.assertEqual(plan.status, "not_ready")


if __name__ == "__main__":
    unittest.main()
