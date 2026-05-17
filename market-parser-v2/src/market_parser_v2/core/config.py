"""Runtime path configuration boundaries."""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class RuntimePaths:
    code_path: Path
    data_path: Path
    logs_path: Path
    secrets_path: Path
    cookies_path: Path
    raw_archives_path: Path
    temp_path: Path
    export_path: Path

    def non_sensitive_runtime_dirs(self) -> tuple[Path, ...]:
        return (
            self.data_path,
            self.logs_path,
            self.raw_archives_path,
            self.temp_path,
            self.export_path,
        )


@dataclass(frozen=True)
class SecretPathConfig:
    ozon_cookie_file: Path | None = None
    wb_secret_file: Path | None = None

    @classmethod
    def from_env(cls) -> "SecretPathConfig":
        return cls(
            ozon_cookie_file=_optional_path(os.getenv("OZON_COOKIE_FILE")),
            wb_secret_file=_optional_path(os.getenv("WB_SECRET_FILE")),
        )


@dataclass(frozen=True)
class ParserConfig:
    paths: RuntimePaths
    secrets: SecretPathConfig
    default_schema_version: str

    @classmethod
    def from_env(cls) -> "ParserConfig":
        from market_parser_v2.core.constants import SCHEMA_VERSION

        base_dir = Path(os.getenv("MARKET_PARSER_V2_BASE_DIR", ".")).resolve()
        paths = RuntimePaths(
            code_path=Path(os.getenv("MARKET_PARSER_V2_CODE_DIR", base_dir)).resolve(),
            data_path=Path(os.getenv("MARKET_PARSER_V2_DATA_DIR", base_dir / "data")).resolve(),
            logs_path=Path(os.getenv("MARKET_PARSER_V2_LOG_DIR", base_dir / "logs")).resolve(),
            secrets_path=Path(os.getenv("MARKET_PARSER_V2_SECRETS_DIR", base_dir / "secrets")).resolve(),
            cookies_path=Path(os.getenv("MARKET_PARSER_V2_COOKIES_DIR", base_dir / "cookies")).resolve(),
            raw_archives_path=Path(
                os.getenv("MARKET_PARSER_V2_RAW_ARCHIVES_DIR", base_dir / "raw_archives")
            ).resolve(),
            temp_path=Path(os.getenv("MARKET_PARSER_V2_TEMP_DIR", base_dir / "temp")).resolve(),
            export_path=Path(os.getenv("MARKET_PARSER_V2_EXPORT_DIR", base_dir / "exports")).resolve(),
        )
        return cls(paths=paths, secrets=SecretPathConfig.from_env(), default_schema_version=SCHEMA_VERSION)

    @classmethod
    def with_export_root(cls, export_root: Path) -> "ParserConfig":
        base = export_root.resolve().parent
        paths = RuntimePaths(
            code_path=base,
            data_path=base / "data",
            logs_path=base / "logs",
            secrets_path=base / "secrets",
            cookies_path=base / "cookies",
            raw_archives_path=base / "raw_archives",
            temp_path=base / "temp",
            export_path=export_root.resolve(),
        )
        from market_parser_v2.core.constants import SCHEMA_VERSION

        return cls(paths=paths, secrets=SecretPathConfig(), default_schema_version=SCHEMA_VERSION)

    def ensure_runtime_dirs(self, *, include_sensitive_dirs: bool = False) -> None:
        for path in self.paths.non_sensitive_runtime_dirs():
            path.mkdir(parents=True, exist_ok=True)
        if include_sensitive_dirs:
            self.paths.secrets_path.mkdir(parents=True, exist_ok=True)
            self.paths.cookies_path.mkdir(parents=True, exist_ok=True)


def _optional_path(value: str | None) -> Path | None:
    if not value:
        return None
    return Path(value).expanduser().resolve()
