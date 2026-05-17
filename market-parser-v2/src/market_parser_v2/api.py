"""Read-only API skeleton for analytics export access.

The API boundary is intentionally minimal and does not start scraping jobs.
"""

from __future__ import annotations

import json
from http.server import SimpleHTTPRequestHandler
from pathlib import Path
from typing import Any


def route_manifest() -> dict[str, Any]:
    """Describe planned read-only API routes without binding a server."""

    return {
        "routes": [
            {
                "method": "GET",
                "path": "/analytics-export/latest.json",
                "description": "Read the latest export pointer.",
            },
            {
                "method": "GET",
                "path": "/analytics-export/{marketplace}/{run_id}/manifest.json",
                "description": "Read a run export manifest.",
            },
            {
                "method": "GET",
                "path": "/analytics-export/{marketplace}/{run_id}/bundle.tar.gz",
                "description": "Download the analytics-only export bundle.",
            },
            {
                "method": "GET",
                "path": "/analytics-export/{marketplace}/{run_id}/checksums.sha256",
                "description": "Read checksums for analytics-import files.",
            },
        ],
        "write_routes": [],
        "live_scraping_routes": [],
    }


class ReadOnlyExportHandler(SimpleHTTPRequestHandler):
    """HTTP handler skeleton constrained to export files under a root path."""

    export_root: Path = Path("exports")

    def do_POST(self) -> None:  # noqa: N802 - stdlib handler API
        self.send_response(405)
        self.end_headers()

    def do_PUT(self) -> None:  # noqa: N802 - stdlib handler API
        self.send_response(405)
        self.end_headers()

    def do_DELETE(self) -> None:  # noqa: N802 - stdlib handler API
        self.send_response(405)
        self.end_headers()

    def do_GET(self) -> None:  # noqa: N802 - stdlib handler API
        if self.path == "/__routes__":
            payload = json.dumps(route_manifest(), sort_keys=True).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)
            return
        super().do_GET()
