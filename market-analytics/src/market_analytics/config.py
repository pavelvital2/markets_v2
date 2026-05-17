from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class Settings:
    app_name: str = "market-analytics"
    supported_schema_versions: tuple[str, ...] = ("analytics-export-v1",)
    auth_username: str | None = None
    auth_secret: str | None = None

    @property
    def auth_configured(self) -> bool:
        return bool(self.auth_username and self.auth_secret)


def load_settings() -> Settings:
    return Settings(
        auth_username=os.getenv("MARKET_ANALYTICS_BASIC_AUTH_USERNAME"),
        auth_secret=os.getenv("MARKET_ANALYTICS_BASIC_AUTH_SECRET"),
    )
