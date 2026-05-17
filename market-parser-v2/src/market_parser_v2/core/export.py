"""Analytics export-bundle layout skeleton."""

from __future__ import annotations

import csv
import hashlib
import json
import tarfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Any

from market_parser_v2.core.config import ParserConfig
from market_parser_v2.core.constants import (
    FORBIDDEN_EXPORT_NAME_PARTS,
    REQUIRED_EXPORT_FILES,
    SCHEMA_VERSION,
)
from market_parser_v2.core.contracts import validate_manifest


@dataclass(frozen=True)
class ExportSkeletonResult:
    latest_json: Path
    manifest_json: Path
    bundle_tar_gz: Path
    checksums_sha256: Path
    manifest_valid: bool

    def to_dict(self) -> dict[str, Any]:
        return {
            "latest_json": str(self.latest_json),
            "manifest_json": str(self.manifest_json),
            "bundle_tar_gz": str(self.bundle_tar_gz),
            "checksums_sha256": str(self.checksums_sha256),
            "manifest_valid": self.manifest_valid,
        }


def create_export_skeleton(*, config: ParserConfig, marketplace: str, run_id: str) -> ExportSkeletonResult:
    if marketplace not in {"wb", "ozon"}:
        raise ValueError(f"unsupported marketplace for export skeleton: {marketplace}")

    export_root = config.paths.export_path
    run_dir = export_root / marketplace / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    with TemporaryDirectory(dir=config.paths.temp_path if config.paths.temp_path.exists() else None) as temp_dir:
        bundle_root = Path(temp_dir) / "bundle"
        _write_placeholder_bundle_files(bundle_root, marketplace=marketplace, run_id=run_id)
        checksums = _checksums_for_files(bundle_root, REQUIRED_EXPORT_FILES)
        _assert_export_file_names_safe(REQUIRED_EXPORT_FILES)

        bundle_path = run_dir / "bundle.tar.gz"
        with tarfile.open(bundle_path, "w:gz") as archive:
            for relative in REQUIRED_EXPORT_FILES:
                archive.add(bundle_root / relative, arcname=relative)

    manifest = _manifest_payload(
        marketplace=marketplace,
        run_id=run_id,
        checksums=checksums,
    )
    manifest_path = run_dir / "manifest.json"
    _write_json(manifest_path, manifest)

    checksums_path = run_dir / "checksums.sha256"
    checksums_path.write_text(
        "".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())),
        encoding="utf-8",
    )

    latest_path = export_root / "latest.json"
    _write_json(
        latest_path,
        {
            "marketplace": marketplace,
            "source_system": marketplace,
            "run_id": run_id,
            "schema_version": SCHEMA_VERSION,
            "manifest_path": f"{marketplace}/{run_id}/manifest.json",
            "bundle_path": f"{marketplace}/{run_id}/bundle.tar.gz",
            "checksums_path": f"{marketplace}/{run_id}/checksums.sha256",
            "updated_at_utc": datetime.now(UTC).isoformat(),
        },
    )

    validation = validate_manifest(manifest, source_system=marketplace)
    return ExportSkeletonResult(
        latest_json=latest_path,
        manifest_json=manifest_path,
        bundle_tar_gz=bundle_path,
        checksums_sha256=checksums_path,
        manifest_valid=validation.ok,
    )


def _write_placeholder_bundle_files(bundle_root: Path, *, marketplace: str, run_id: str) -> None:
    _write_csv(bundle_root / "marts/queries.csv", ["marketplace", "source_system", "run_id", "query", "schema_version"])
    _write_csv(
        bundle_root / "marts/products.csv",
        [
            "marketplace",
            "source_system",
            "run_id",
            "query",
            "absolute_position",
            "external_product_id",
            "schema_version",
        ],
    )
    _write_csv(
        bundle_root / "marts/sellers.csv",
        ["marketplace", "source_system", "run_id", "external_seller_id", "seller_name", "schema_version"],
    )
    _write_csv(
        bundle_root / "marts/seller_query_product_bridge.csv",
        [
            "marketplace",
            "source_system",
            "run_id",
            "query",
            "external_product_id",
            "external_seller_id",
            "schema_version",
        ],
    )
    _write_json(
        bundle_root / "quality/data_quality_summary.json",
        {
            "marketplace": marketplace,
            "source_system": marketplace,
            "run_id": run_id,
            "status": "not_ready",
            "usable_for_reports": "invalid_for_reports",
            "warnings": ["skeleton export contains headers only"],
            "errors": [],
            "schema_version": SCHEMA_VERSION,
        },
    )
    _write_json(
        bundle_root / "metadata/contract.json",
        {
            "schema_version": SCHEMA_VERSION,
            "source_system": marketplace,
            "required_files": list(REQUIRED_EXPORT_FILES),
        },
    )


def _manifest_payload(*, marketplace: str, run_id: str, checksums: dict[str, str]) -> dict[str, Any]:
    return {
        "marketplace": marketplace,
        "source_system": marketplace,
        "run_id": run_id,
        "schema_version": SCHEMA_VERSION,
        "export_created_at_utc": datetime.now(UTC).isoformat(),
        "component_statuses": {
            "suggest": "not_ready",
            "filter": "not_ready",
            "serp": "not_ready",
            "sellers": "not_ready",
            "export": "success",
        },
        "file_list": list(REQUIRED_EXPORT_FILES),
        "row_counts": {
            "queries": 0,
            "products": 0,
            "sellers": 0,
            "seller_query_product_bridge": 0,
        },
        "checksums": checksums,
        "data_quality_summary": {
            "run_status": "not_ready",
            "report_usability": "invalid_for_reports",
            "data_confidence_level": None,
        },
        "usable_for_reports": "invalid_for_reports",
        "warnings": ["skeleton export contains no collected marketplace rows"],
        "errors": [],
    }


def _write_csv(path: Path, fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()


def _write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def _checksums_for_files(root: Path, relatives: tuple[str, ...]) -> dict[str, str]:
    checksums: dict[str, str] = {}
    for relative in relatives:
        checksums[relative] = hashlib.sha256((root / relative).read_bytes()).hexdigest()
    return checksums


def _assert_export_file_names_safe(relatives: tuple[str, ...]) -> None:
    for relative in relatives:
        lower = relative.lower()
        if any(part in lower for part in FORBIDDEN_EXPORT_NAME_PARTS):
            raise ValueError(f"forbidden export file name: {relative}")
