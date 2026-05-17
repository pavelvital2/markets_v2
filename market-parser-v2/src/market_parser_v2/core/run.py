"""Run identity and context helpers."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import uuid4

from market_parser_v2.core.constants import SCHEMA_VERSION


def new_run_id() -> str:
    timestamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%SZ")
    return f"run_{timestamp}_{uuid4().hex[:12]}"


@dataclass(frozen=True)
class RunContext:
    run_id: str
    marketplace: str
    source_system: str
    schema_version: str = SCHEMA_VERSION
