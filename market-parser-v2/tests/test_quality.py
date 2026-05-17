from __future__ import annotations

import unittest

from market_parser_v2.core.quality import map_source_status, summarize_data_quality


class QualitySummaryTests(unittest.TestCase):
    def test_source_status_mapping_preserves_partial_and_failure(self) -> None:
        self.assertEqual(map_source_status("success"), ("success", "valid_for_reports"))
        self.assertEqual(map_source_status("empty"), ("partial", "partial_use_with_warning"))
        self.assertEqual(map_source_status("error"), ("failed", "invalid_for_reports"))
        self.assertEqual(map_source_status("not_ready"), ("failed", "invalid_for_reports"))

    def test_summary_keeps_run_component_row_and_export_levels(self) -> None:
        summary = summarize_data_quality(
            run_id="run_synthetic_001",
            marketplace="ozon",
            source_system="ozon",
            component_statuses={"suggest": "success", "serp": "empty", "sellers": "error"},
            row_statuses=("success", "empty", "error"),
            export_errors=("checksum mismatch",),
        )
        payload = summary.to_dict()

        self.assertEqual(payload["run_status"], "partial")
        self.assertEqual(payload["report_usability"], "partial_use_with_warning")
        self.assertEqual(payload["export_status"], "failed")
        self.assertEqual(payload["component_statuses"]["serp"]["run_status"], "partial")
        self.assertEqual(payload["component_statuses"]["sellers"]["run_status"], "failed")
        self.assertEqual(payload["row_status_counts"]["empty"], 1)
        self.assertIsNone(payload["data_confidence_level"])
        self.assertTrue(payload["warnings"])


if __name__ == "__main__":
    unittest.main()
