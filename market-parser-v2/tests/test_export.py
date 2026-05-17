from __future__ import annotations

import io
import json
import tarfile
import tempfile
import unittest
from pathlib import Path

from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.constants import REQUIRED_EXPORT_FILES
from market_parser_v2.core.export import create_export_skeleton, validate_export_artifacts


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

            validation = validate_export_artifacts(
                export_root=export_root,
                marketplace="wb",
                run_id="run_synthetic_001",
            )
            self.assertTrue(validation.ok, validation.to_dict())
            self.assertTrue(validation.checksums_valid)
            self.assertEqual(validation.forbidden_artifacts, ())

    def test_checksum_tampering_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            config = ParserConfig.with_export_root(export_root)
            create_export_skeleton(config=config, marketplace="ozon", run_id="run_synthetic_001")

            checksums_path = export_root / "ozon/run_synthetic_001/checksums.sha256"
            lines = checksums_path.read_text(encoding="utf-8").splitlines()
            digest, relative = lines[0].split(None, 1)
            tampered_digest = ("0" if digest[0] != "0" else "1") + digest[1:]
            lines[0] = f"{tampered_digest}  {relative.strip()}"
            checksums_path.write_text("\n".join(lines) + "\n", encoding="utf-8")

            validation = validate_export_artifacts(
                export_root=export_root,
                marketplace="ozon",
                run_id="run_synthetic_001",
            )

            self.assertFalse(validation.ok)
            self.assertFalse(validation.checksums_valid)
            self.assertIn("checksum_mismatch", {issue.code for issue in validation.issues})

    def test_forbidden_bundle_content_is_detected(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            export_root = Path(temp_dir) / "exports"
            config = ParserConfig.with_export_root(export_root)
            create_export_skeleton(config=config, marketplace="wb", run_id="run_synthetic_001")
            bundle_path = export_root / "wb/run_synthetic_001/bundle.tar.gz"
            replacement = Path(temp_dir) / "replacement.tar.gz"

            with tarfile.open(bundle_path, "r:gz") as source, tarfile.open(replacement, "w:gz") as target:
                for member in source.getmembers():
                    extracted = source.extractfile(member)
                    if extracted is not None:
                        target.addfile(member, extracted)
                payload = b"cookie=session"
                info = tarfile.TarInfo("raw/cookie.txt")
                info.size = len(payload)
                target.addfile(info, io.BytesIO(payload))
            replacement.replace(bundle_path)

            validation = validate_export_artifacts(
                export_root=export_root,
                marketplace="wb",
                run_id="run_synthetic_001",
            )

            self.assertFalse(validation.ok)
            self.assertIn("raw/cookie.txt", validation.forbidden_artifacts)
            self.assertIn("forbidden_bundle_artifact", {issue.code for issue in validation.issues})


if __name__ == "__main__":
    unittest.main()
