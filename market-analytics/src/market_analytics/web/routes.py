from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse

from market_analytics.auth import require_basic_auth
from market_analytics.registry import registry

router = APIRouter(dependencies=[Depends(require_basic_auth)])

_TEMPLATE_PATH = Path(__file__).parent / "templates" / "overview.html"


@router.get("/", response_class=HTMLResponse)
@router.get("/overview", response_class=HTMLResponse)
def overview_page() -> HTMLResponse:
    latest = registry.latest()
    html = _TEMPLATE_PATH.read_text(encoding="utf-8")
    html = html.replace("{{ latest_run }}", latest.identity.run_id if latest else "No imports")
    html = html.replace(
        "{{ latest_status }}",
        latest.status.value if latest else "No imported run registry entries",
    )
    html = html.replace(
        "{{ marketplace }}",
        latest.identity.provider.marketplace.value if latest else "both",
    )
    html = html.replace(
        "{{ source_system }}",
        latest.identity.provider.source_system.value if latest else "none",
    )
    html = html.replace(
        "{{ warning }}",
        "Partial data warning" if latest and latest.warnings else "No partial data warning",
    )
    html = html.replace(
        "{{ error_count }}",
        str(len(latest.errors) if latest else 0),
    )
    return HTMLResponse(html)
