from __future__ import annotations

import csv
import io
import json
import tarfile
import tempfile
import unittest
from pathlib import Path

from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.constants import REQUIRED_EXPORT_FILES
from market_parser_v2.core.export import validate_export_artifacts
from market_parser_v2.core.registry import get_provider
from market_parser_v2.providers.ozon import (
    OzonProvider,
    extract_web_suggestions,
    seller_resource_action,
    synthetic_ozon_fixture,
)


class OzonProviderMigrationTests(unittest.TestCase):
    def test_web_suggestions_keep_first_five_and_dedupe(self) -> None:
        state = {
            "items": [
                {"cellItem": {"centerBlock": {"title": {"text": "Alpha"}}}},
                {"cellItem": {"centerBlock": {"title": {"text": " alpha "}}}},
                {"cellItem": {"centerBlock": {"title": {"text": "Ёлка"}}}},
                {"cellItem": {"centerBlock": {"title": {"text": "елка"}}}},
                {"cellItem": {"centerBlock": {"title": {"text": "Gamma"}}}},
                {"cellItem": {"centerBlock": {"title": {"text": "Outside first five"}}}},
            ]
        }
        payload = {
            "widgetStates": {
                "webSuggestions-1-default-1": json.dumps(state, ensure_ascii=False),
                "notSuggestions-1": "{}",
            }
        }

        self.assertEqual(extract_web_suggestions(payload), ["Alpha", "Ёлка", "Gamma"])

    def test_ozon_fixture_migration_writes_runtime_common_marts_and_safe_export(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            config = ParserConfig.with_export_root(export_root)

            result = OzonProvider().run_fixture(
                config=config,
                fixture=synthetic_ozon_fixture(),
                run_id="run_ozon_fixture_001",
            )

            self.assertEqual(result.status, "success")
            self.assertEqual(result.report_usability, "valid_for_reports")
            self.assertTrue(result.checkpoint_path.exists())
            self.assertTrue(result.seller_progress_path.exists())
            self.assertTrue(result.run_report_path.exists())
            self.assertTrue(result.latest_run_report_path.exists())
            self.assertTrue(result.export_result.manifest_valid, result.export_result.to_dict())

            products_path = Path(result.common_mart_files["products"])
            with products_path.open("r", encoding="utf-8-sig", newline="") as handle:
                product_rows = list(csv.DictReader(handle, delimiter=";"))
            self.assertEqual([row["absolute_position"] for row in product_rows], ["1", "2", "3"])
            self.assertEqual([row["position_on_page"] for row in product_rows], ["1", "2", "1"])
            self.assertEqual(product_rows[0]["source_system"], "ozon")
            self.assertEqual(product_rows[0]["marketplace"], "ozon")
            self.assertEqual(product_rows[0]["external_product_id"], "1001")
            self.assertEqual(product_rows[0]["external_seller_id"], "seller-10")
            self.assertEqual({row["data_quality_status"] for row in product_rows}, {"valid_for_reports"})
            self.assertNotIn("nmId", product_rows[0])
            self.assertNotIn("supplier_id", product_rows[0])

            pages_path = Path(result.provider_files["serp_pages_index"])
            with pages_path.open("r", encoding="utf-8-sig", newline="") as handle:
                page_rows = list(csv.DictReader(handle, delimiter=";"))
            self.assertEqual([row["products_count"] for row in page_rows], ["2", "1"])
            self.assertEqual(page_rows[0]["next_page"], "/search/?text=coffee%20beans&page=2&opaque=abc")

            checkpoint = json.loads(result.checkpoint_path.read_text(encoding="utf-8"))
            self.assertIn("nextPage=/search/?text=coffee%20beans&page=2&opaque=abc", checkpoint["serp"][0]["checkpoint_value"])

            report = json.loads(result.run_report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["source_system"], "ozon")
            self.assertFalse(report["runtime"]["cookie_file_configured"])
            self.assertEqual(report["runtime"]["cookie_file_env"], "OZON_COOKIE_FILE")
            self.assertNotIn("cookie_file", report["runtime"])
            self.assertTrue(report["runtime"]["block_non_document_resources"])

            validation = validate_export_artifacts(
                export_root=export_root,
                marketplace="ozon",
                run_id="run_ozon_fixture_001",
            )
            self.assertTrue(validation.ok, validation.to_dict())

            with tarfile.open(result.export_result.bundle_tar_gz, "r:gz") as archive:
                names = set(archive.getnames())
                products_member = archive.extractfile("marts/products.csv")
                self.assertIsNotNone(products_member)
                products_payload = products_member.read() if products_member is not None else b""
            self.assertEqual(names, set(REQUIRED_EXPORT_FILES))
            self.assertFalse(any("cookie" in name or "raw" in name or ".har" in name for name in names))
            exported_rows = list(csv.DictReader(io.StringIO(products_payload.decode("utf-8-sig")), delimiter=";"))
            self.assertEqual(exported_rows[0]["source_system"], "ozon")
            self.assertEqual(exported_rows[0]["external_product_id"], "1001")

    def test_seller_enrichment_uses_document_only_policy_and_resume_progress(self) -> None:
        self.assertEqual(seller_resource_action("document"), "continue")
        self.assertEqual(seller_resource_action("image"), "abort")
        self.assertEqual(seller_resource_action("xhr"), "abort")

        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            config = ParserConfig.with_export_root(export_root)
            run_id = "run_ozon_resume_001"
            fixture = synthetic_ozon_fixture()

            first = OzonProvider().run_fixture(config=config, fixture=fixture, run_id=run_id)
            self.assertEqual(first.status, "success")
            self.assertNotIn("raw_json_fragment", first.seller_progress_path.read_text(encoding="utf-8"))

            resumed_fixture = synthetic_ozon_fixture()
            resumed_fixture.seller_states_by_product_id.clear()
            second = OzonProvider().run_fixture(config=config, fixture=resumed_fixture, run_id=run_id, resume=True)

            self.assertEqual(second.status, "success")
            sellers_path = Path(second.common_mart_files["sellers"])
            with sellers_path.open("r", encoding="utf-8-sig", newline="") as handle:
                seller_rows = list(csv.DictReader(handle, delimiter=";"))
            self.assertEqual({row["external_seller_id"] for row in seller_rows}, {"seller-10", "seller-20"})

    def test_blocked_seller_enrichment_only_downgrades_affected_product_rows(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            config = ParserConfig.with_export_root(export_root)
            fixture = synthetic_ozon_fixture()
            fixture.seller_states_by_product_id["1003"] = {"http_status": 403}

            result = OzonProvider().run_fixture(
                config=config,
                fixture=fixture,
                run_id="run_ozon_one_blocked_seller_001",
                resume=False,
            )

            self.assertEqual(result.status, "partial")
            self.assertEqual(result.report_usability, "partial_use_with_warning")

            provider_products_path = Path(result.provider_files["serp_products_daily"])
            with provider_products_path.open("r", encoding="utf-8-sig", newline="") as handle:
                provider_products = {row["nmId"]: row for row in csv.DictReader(handle, delimiter=";")}
            self.assertEqual(provider_products["1001"]["status"], "success")
            self.assertEqual(provider_products["1001"]["data_quality_status"], "valid_for_reports")
            self.assertEqual(provider_products["1001"]["supplier_id"], "seller-10")
            self.assertEqual(provider_products["1003"]["status"], "partial")
            self.assertEqual(provider_products["1003"]["data_quality_status"], "partial_use_with_warning")
            self.assertEqual(provider_products["1003"]["supplier_id"], "")
            self.assertIn("seller_enrichment_missing_seller_id", provider_products["1003"]["error_message"])

            products_path = Path(result.common_mart_files["products"])
            with products_path.open("r", encoding="utf-8-sig", newline="") as handle:
                common_products = {row["external_product_id"]: row for row in csv.DictReader(handle, delimiter=";")}
            self.assertEqual(common_products["1001"]["source_system"], "ozon")
            self.assertEqual(common_products["1001"]["external_seller_id"], "seller-10")
            self.assertEqual(common_products["1001"]["data_quality_status"], "valid_for_reports")
            self.assertEqual(common_products["1003"]["source_system"], "ozon")
            self.assertEqual(common_products["1003"]["external_seller_id"], "")
            self.assertEqual(common_products["1003"]["data_quality_status"], "partial_use_with_warning")

            bridge_path = Path(result.common_mart_files["seller_query_product_bridge"])
            with bridge_path.open("r", encoding="utf-8-sig", newline="") as handle:
                bridge_products = {row["external_product_id"] for row in csv.DictReader(handle, delimiter=";")}
            self.assertEqual(bridge_products, {"1001", "1002"})

            with tarfile.open(result.export_result.bundle_tar_gz, "r:gz") as archive:
                products_member = archive.extractfile("marts/products.csv")
                self.assertIsNotNone(products_member)
                products_payload = products_member.read() if products_member is not None else b""
            exported_products = {
                row["external_product_id"]: row
                for row in csv.DictReader(io.StringIO(products_payload.decode("utf-8-sig")), delimiter=";")
            }
            self.assertEqual(exported_products["1001"]["data_quality_status"], "valid_for_reports")
            self.assertEqual(exported_products["1003"]["data_quality_status"], "partial_use_with_warning")

            report = json.loads(result.run_report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["component_statuses"]["sellers"], "partial")

    def test_missing_seller_enrichment_produces_partial_quality_and_validation_warning(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            config = ParserConfig.with_export_root(export_root)
            fixture = synthetic_ozon_fixture()
            fixture.seller_states_by_product_id.clear()

            result = OzonProvider().run_fixture(
                config=config,
                fixture=fixture,
                run_id="run_ozon_missing_sellers_001",
                resume=False,
            )

            self.assertEqual(result.status, "partial")
            self.assertEqual(result.report_usability, "partial_use_with_warning")

            provider_products_path = Path(result.provider_files["serp_products_daily"])
            with provider_products_path.open("r", encoding="utf-8-sig", newline="") as handle:
                provider_products = list(csv.DictReader(handle, delimiter=";"))
            self.assertEqual({row["status"] for row in provider_products}, {"partial"})
            self.assertEqual({row["data_quality_status"] for row in provider_products}, {"partial_use_with_warning"})
            self.assertEqual({row["supplier_id"] for row in provider_products}, {""})

            products_path = Path(result.common_mart_files["products"])
            with products_path.open("r", encoding="utf-8-sig", newline="") as handle:
                common_products = list(csv.DictReader(handle, delimiter=";"))
            self.assertEqual({row["source_system"] for row in common_products}, {"ozon"})
            self.assertEqual({row["external_seller_id"] for row in common_products}, {""})
            self.assertEqual({row["data_quality_status"] for row in common_products}, {"partial_use_with_warning"})

            with tarfile.open(result.export_result.bundle_tar_gz, "r:gz") as archive:
                products_member = archive.extractfile("marts/products.csv")
                self.assertIsNotNone(products_member)
                products_payload = products_member.read() if products_member is not None else b""
            exported_products = list(csv.DictReader(io.StringIO(products_payload.decode("utf-8-sig")), delimiter=";"))
            self.assertEqual({row["data_quality_status"] for row in exported_products}, {"partial_use_with_warning"})

            report = json.loads(result.run_report_path.read_text(encoding="utf-8"))
            self.assertEqual(report["component_statuses"]["sellers"], "error")
            self.assertTrue(any("seller id is absent" in warning for warning in report["warnings"]))

    def test_ozon_plan_is_registered_behind_provider_abstraction(self) -> None:
        provider = get_provider("ozon")
        plan = provider.build_plan()

        self.assertEqual(plan.provider_id, "ozon")
        self.assertEqual(plan.components, ("suggest", "filter", "serp", "sellers", "export"))
        self.assertFalse(plan.live_scraping_enabled)
        self.assertEqual(plan.status, "ready_offline_fixture")


if __name__ == "__main__":
    unittest.main()
