from __future__ import annotations

import csv
import io
import json
import tarfile
import tempfile
import unittest
from pathlib import Path

from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.export import validate_export_artifacts
from market_parser_v2.core.registry import get_provider
from market_parser_v2.providers.wb import WbProvider, synthetic_wb_fixture


class WbProviderMigrationTests(unittest.TestCase):
    def test_wb_fixture_migration_writes_normalized_runtime_and_export(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            config = ParserConfig.with_export_root(export_root)

            result = WbProvider().run_fixture(
                config=config,
                fixture=synthetic_wb_fixture(),
                run_id="run_wb_fixture_001",
            )

            self.assertEqual(result.status, "success")
            self.assertEqual(result.report_usability, "valid_for_reports")
            self.assertTrue(result.checkpoint_path.exists())
            self.assertTrue(result.run_report_path.exists())
            self.assertTrue(result.latest_run_report_path.exists())
            self.assertTrue(result.export_result.manifest_valid, result.export_result.to_dict())

            products_path = Path(result.common_mart_files["products"])
            with products_path.open("r", encoding="utf-8-sig", newline="") as handle:
                product_rows = list(csv.DictReader(handle, delimiter=";"))
            self.assertEqual(product_rows[0]["source_system"], "wb")
            self.assertEqual(product_rows[0]["marketplace"], "wb")
            self.assertEqual(product_rows[0]["external_product_id"], "123456")
            self.assertEqual(product_rows[0]["external_seller_id"], "456789")
            self.assertNotIn("nmId", product_rows[0])
            self.assertNotIn("supplier_id", product_rows[0])

            provider_raw = Path(result.provider_files["suggest_raw"])
            raw_bytes = provider_raw.read_bytes()
            self.assertTrue(raw_bytes.startswith(b"\xef\xbb\xbf"))
            self.assertIn(";", raw_bytes.decode("utf-8-sig").splitlines()[0])

            report = json.loads(result.run_report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["source_system"], "wb")
            self.assertEqual(report["component_statuses"]["serp"], "success")
            self.assertEqual(report["export"]["manifest_valid"], True)

            validation = validate_export_artifacts(
                export_root=export_root,
                marketplace="wb",
                run_id="run_wb_fixture_001",
            )
            self.assertTrue(validation.ok, validation.to_dict())

            with tarfile.open(result.export_result.bundle_tar_gz, "r:gz") as archive:
                products_member = archive.extractfile("marts/products.csv")
                self.assertIsNotNone(products_member)
                products_payload = products_member.read() if products_member is not None else b""
            exported_rows = list(csv.DictReader(io.StringIO(products_payload.decode("utf-8-sig")), delimiter=";"))
            self.assertEqual(exported_rows[0]["source_system"], "wb")
            self.assertEqual(exported_rows[0]["external_product_id"], "123456")

    def test_wb_plan_is_offline_and_registered_behind_provider_abstraction(self) -> None:
        provider = get_provider("wb")
        plan = provider.build_plan()

        self.assertEqual(plan.provider_id, "wb")
        self.assertEqual(plan.components, ("suggest", "filter", "serp", "sellers", "export"))
        self.assertFalse(plan.live_scraping_enabled)
        self.assertEqual(plan.status, "ready_offline_fixture")


if __name__ == "__main__":
    unittest.main()
