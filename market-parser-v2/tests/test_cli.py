from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from market_parser_v2.cli import main


class CliTests(unittest.TestCase):
    def test_offline_commands_return_success(self) -> None:
        self.assertEqual(main(["providers"]), 0)
        self.assertEqual(main(["plan", "--marketplace", "all"]), 0)
        self.assertEqual(main(["validate-synthetic", "--marketplace", "wb"]), 0)

    def test_create_export_skeleton_command(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            status = main(
                [
                    "create-export-skeleton",
                    "--marketplace",
                    "ozon",
                    "--run-id",
                    "run_synthetic_001",
                    "--output-dir",
                    str(export_root),
                ]
            )
            self.assertEqual(status, 0)
            self.assertTrue((export_root / "latest.json").exists())

    def test_run_ozon_synthetic_command(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            status = main(
                [
                    "run-ozon-synthetic",
                    "--run-id",
                    "run_ozon_synthetic_001",
                    "--output-dir",
                    str(export_root),
                ]
            )
            self.assertEqual(status, 0)
            self.assertTrue((export_root / "ozon/run_ozon_synthetic_001/manifest.json").exists())


if __name__ == "__main__":
    unittest.main()
