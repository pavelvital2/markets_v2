from __future__ import annotations

import unittest

from market_parser_v2.core.constants import SCHEMA_VERSION
from market_parser_v2.core.contracts import (
    synthetic_contract_row,
    validate_contract_rows,
    validate_manifest,
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


if __name__ == "__main__":
    unittest.main()
