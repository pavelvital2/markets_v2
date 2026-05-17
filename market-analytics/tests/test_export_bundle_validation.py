from __future__ import annotations

import hashlib
import io
import json
from pathlib import Path
import sys
import tarfile
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from market_analytics.importing.validator import ExportBundlePaths, ExportBundleValidator


REQUIRED_FILES = {
    "marts/queries.csv": "run_id,marketplace,source_system,query,schema_version\nrun-1,wb,wb,shoes,analytics-export-v1\n",
    "marts/products.csv": "run_id,marketplace,source_system,external_product_id,schema_version\nrun-1,wb,wb,1,analytics-export-v1\n",
    "marts/sellers.csv": "run_id,marketplace,source_system,external_seller_id,schema_version\nrun-1,wb,wb,10,analytics-export-v1\n",
    "marts/seller_query_product_bridge.csv": "run_id,marketplace,source_system,query,external_product_id,external_seller_id,schema_version\nrun-1,wb,wb,shoes,1,10,analytics-export-v1\n",
    "quality/data_quality_summary.json": "{}\n",
    "metadata/contract.json": '{"schema_version":"analytics-export-v1"}\n',
}


class ExportBundleValidationTest(unittest.TestCase):
    def test_valid_synthetic_bundle_passes(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _write_bundle(Path(tmp), REQUIRED_FILES)

            result = ExportBundleValidator().validate(paths)

            self.assertTrue(result.valid, [issue.code for issue in result.issues])
            self.assertEqual(result.manifest["run_id"], "run-1")
            self.assertEqual(result.manifest["marketplace"], "wb")
            self.assertEqual(result.manifest["source_system"], "wb")

    def test_checksum_mismatch_quarantines_bundle(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            paths = _write_bundle(Path(tmp), REQUIRED_FILES)
            paths.checksums_path.write_text(
                "0" * 64 + "  marts/queries.csv\n",
                encoding="utf-8",
            )

            result = ExportBundleValidator().validate(paths)

            self.assertFalse(result.valid)
            self.assertIn(
                "checksums.sha256.checksum_mismatch",
                {issue.code for issue in result.issues},
            )

    def test_secret_like_bundle_path_is_rejected(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            files = dict(REQUIRED_FILES)
            files["logs/session.log"] = "token=must-not-ship\n"
            paths = _write_bundle(Path(tmp), files)

            result = ExportBundleValidator().validate(paths)

            self.assertFalse(result.valid)
            self.assertIn(
                "bundle.forbidden_secret_like_path",
                {issue.code for issue in result.issues},
            )


def _write_bundle(base: Path, files: dict[str, str]) -> ExportBundlePaths:
    bundle_path = base / "bundle.tar.gz"
    checksums = {
        path: hashlib.sha256(content.encode("utf-8")).hexdigest()
        for path, content in files.items()
    }

    with tarfile.open(bundle_path, "w:gz") as archive:
        for path, content in files.items():
            data = content.encode("utf-8")
            info = tarfile.TarInfo(path)
            info.size = len(data)
            archive.addfile(info, io.BytesIO(data))

    manifest = {
        "marketplace": "wb",
        "source_system": "wb",
        "run_id": "run-1",
        "schema_version": "analytics-export-v1",
        "export_created_at_utc": "2026-05-17T00:00:00Z",
        "component_statuses": {"queries": "success"},
        "file_list": list(files),
        "row_counts": {"queries": 1, "products": 1, "sellers": 1},
        "checksums": checksums,
        "data_quality_summary": {"status": "success"},
        "usable_for_reports": True,
        "warnings": [],
        "errors": [],
    }
    manifest_path = base / "manifest.json"
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    checksums_path = base / "checksums.sha256"
    checksums_path.write_text(
        "".join(f"{digest}  {path}\n" for path, digest in checksums.items()),
        encoding="utf-8",
    )

    return ExportBundlePaths(
        manifest_path=manifest_path,
        bundle_path=bundle_path,
        checksums_path=checksums_path,
    )


if __name__ == "__main__":
    unittest.main()
