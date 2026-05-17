from __future__ import annotations

import unittest

from market_parser_v2.core.constants import SCHEMA_VERSION
from market_parser_v2.core.contracts import (
    COMMON_MART_SCHEMAS,
    map_external_product_id,
    map_external_seller_id,
    normalize_source_system,
    synthetic_mart_row,
    synthetic_contract_row,
    validate_contract_rows,
    validate_manifest,
    validate_mart_rows,
    validate_provider_identity,
    validate_schema_version,
)


class ContractValidationTests(unittest.TestCase):
    def test_synthetic_row_validates_provider_and_schema(self) -> None:
        row = synthetic_contract_row(source_system="wb", run_id="run_synthetic_001")
        result = validate_contract_rows([row], source_system="wb")
        self.assertTrue(result.ok, result.to_dict())

    def test_provider_identity_mismatch_is_detected(self) -> None:
        row = synthetic_contract_row(source_system="wb", run_id="run_synthetic_001")
        result = validate_contract_rows([row], source_system="ozon")
        self.assertFalse(result.ok)
        self.assertIn("provider_identity_mismatch", {issue.code for issue in result.issues})

    def test_missing_run_id_is_detected(self) -> None:
        row = synthetic_contract_row(source_system="ozon", run_id="")
        result = validate_contract_rows([row], source_system="ozon")
        self.assertFalse(result.ok)
        self.assertIn("missing_run_id", {issue.code for issue in result.issues})

    def test_manifest_minimum_fields_validate(self) -> None:
        manifest = {
            "marketplace": "wb",
            "source_system": "wb",
            "run_id": "run_synthetic_001",
            "schema_version": SCHEMA_VERSION,
            "export_created_at_utc": "2026-01-01T00:00:00+00:00",
            "component_statuses": {},
            "file_list": [],
            "row_counts": {},
            "checksums": {},
            "data_quality_summary": {},
            "usable_for_reports": "invalid_for_reports",
            "warnings": [],
            "errors": [],
        }
        self.assertTrue(validate_manifest(manifest, source_system="wb").ok)

    def test_common_mart_schemas_include_required_service_fields(self) -> None:
        for mart_name in ("queries", "products", "sellers", "seller_query_product_bridge"):
            fields = set(COMMON_MART_SCHEMAS[mart_name].fields)
            self.assertIn("marketplace", fields)
            self.assertIn("source_system", fields)
            self.assertIn("run_id", fields)
            self.assertIn("schema_version", fields)
            self.assertIn("data_quality_status", fields)

    def test_synthetic_common_mart_rows_validate_strictly(self) -> None:
        for mart_name in COMMON_MART_SCHEMAS:
            row = synthetic_mart_row(mart_name=mart_name, source_system="ozon", run_id="run_synthetic_001")
            result = validate_mart_rows(mart_name, [row], source_system="ozon")
            self.assertTrue(result.ok, result.to_dict())

    def test_common_mart_rejects_unexpected_columns_and_duplicate_positions(self) -> None:
        row = synthetic_mart_row(mart_name="products", source_system="wb", run_id="run_synthetic_001")
        duplicate = dict(row)
        row["extra"] = "not allowed"

        result = validate_mart_rows("products", [row, duplicate], source_system="wb")

        self.assertFalse(result.ok)
        self.assertIn("unexpected_field", {issue.code for issue in result.issues})
        self.assertIn("duplicate_product_position", {issue.code for issue in result.issues})

    def test_missing_seller_id_is_detected_when_seller_data_is_expected(self) -> None:
        row = synthetic_mart_row(mart_name="products", source_system="wb", run_id="run_synthetic_001")
        row["external_seller_id"] = ""

        result = validate_mart_rows("products", [row], source_system="wb", seller_data_expected=True)

        self.assertFalse(result.ok)
        self.assertIn("missing_seller_id", {issue.code for issue in result.issues})

    def test_unsupported_schema_can_be_rejected_or_quarantined(self) -> None:
        reject = validate_schema_version("unsupported", unsupported_action="reject")
        quarantine = validate_schema_version("unsupported", unsupported_action="quarantine")

        self.assertFalse(reject.ok)
        self.assertEqual(reject.action, "reject")
        self.assertFalse(quarantine.ok)
        self.assertEqual(quarantine.action, "quarantine")

    def test_invalid_provider_identity_can_be_rejected_or_quarantined(self) -> None:
        reject = validate_provider_identity("wildberries", invalid_action="reject")
        quarantine = validate_provider_identity("unknown", invalid_action="quarantine")

        self.assertFalse(reject.ok)
        self.assertEqual(reject.action, "reject")
        self.assertFalse(quarantine.ok)
        self.assertEqual(quarantine.action, "quarantine")

    def test_wildberries_alias_must_be_normalized_before_common_validation(self) -> None:
        self.assertEqual(normalize_source_system("wildberries"), "wb")
        row = synthetic_mart_row(mart_name="queries", source_system="wildberries", run_id="run_synthetic_001")

        result = validate_mart_rows("queries", [row], source_system="wildberries")

        self.assertFalse(result.ok)
        self.assertIn("invalid_provider", {issue.code for issue in result.issues})

    def test_compatibility_mapping_requires_provider_context(self) -> None:
        with self.assertRaises(ValueError):
            map_external_product_id(source_system=None, nm_id=123)
        with self.assertRaises(ValueError):
            map_external_seller_id(source_system=None, supplier_id=456)

        wb_product = map_external_product_id(source_system="wb", nm_id=123)
        ozon_product = map_external_product_id(source_system="ozon", nm_id=123)
        wb_seller = map_external_seller_id(source_system="wb", supplier_id=456)

        self.assertEqual(wb_product.join_key, ("wb", "123"))
        self.assertEqual(ozon_product.join_key, ("ozon", "123"))
        self.assertNotEqual(wb_product.join_key, ozon_product.join_key)
        self.assertEqual(wb_seller.to_dict()["source_field"], "supplier_id")


if __name__ == "__main__":
    unittest.main()
