from __future__ import annotations

import json
import tarfile
import tempfile
import unittest
from pathlib import Path

from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.constants import REQUIRED_EXPORT_FILES
from market_parser_v2.core.export import create_export_skeleton


class ExportSkeletonTests(unittest.TestCase):
    def test_export_layout_is_created_without_forbidden_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            config = ParserConfig.with_export_root(export_root)
            result = create_export_skeleton(config=config, marketplace="wb", run_id="run_synthetic_001")

            self.assertTrue(result.manifest_valid)
            self.assertTrue(result.latest_json.exists())
            self.assertTrue(result.manifest_json.exists())
            self.assertTrue(result.bundle_tar_gz.exists())
            self.assertTrue(result.checksums_sha256.exists())

            latest = json.loads(result.latest_json.read_text(encoding="utf-8"))
            self.assertEqual(latest["manifest_path"], "wb/run_synthetic_001/manifest.json")

            with tarfile.open(result.bundle_tar_gz, "r:gz") as archive:
                names = set(archive.getnames())
            self.assertEqual(names, set(REQUIRED_EXPORT_FILES))
            self.assertFalse(any("cookie" in name or "secret" in name for name in names))


if __name__ == "__main__":
    unittest.main()
