# market-analytics

Clean Stage 6 analytics application skeleton for importing sanitized parser
export bundles and serving authenticated placeholder API/web surfaces.

This repository area is an accepted skeleton only. Stage 9 Market Intelligence
MVP work is not dispatchable from the current design baseline, and this package
does not implement dashboards, analytics formulas, own-store logic, product or
seller matching, marketplace comparison, Excel export, or a decision layer.

## Import Boundary

- Imports only parser export bundle files:
  - `manifest.json`
  - `bundle.tar.gz`
  - `checksums.sha256`
- Treats parser output as an external bundle contract.
- Does not import parser packages, parser modules, provider internals, source
  project folders, parser runtime state, checkpoints, or internal databases.
- Preserves `run_id`, `marketplace`, and `source_system` for every imported run.
- Keeps provider identifiers scoped by `marketplace`/`source_system`.
- Rejects invalid provider identity, unsupported schema versions, checksum
  mismatches, missing required marts for usable bundles, and secret-like bundle
  files.
- Does not scrape marketplaces.
- Does not create or log cookies, credentials, tokens, or other secrets.

## Local Skeleton Commands

Install runtime dependencies before creating the FastAPI app or serving API/web
routes. `fastapi` and `uvicorn[standard]` are declared in `pyproject.toml`.

```bash
cd market-analytics
python -m venv .venv
. .venv/bin/activate
python -m pip install -e .
```

Run the synthetic export-bundle validation tests:

```bash
cd market-analytics
PYTHONPATH=src python -m unittest discover -s tests
```

The basic auth placeholder reads credentials from environment configuration.
Set both values locally before using API/web routes; do not commit them to the
repository:

```bash
export MARKET_ANALYTICS_BASIC_AUTH_USERNAME=<user>
export MARKET_ANALYTICS_BASIC_AUTH_SECRET=<set in local environment>
```

No default username or auth secret is provided.

The web/API routes are placeholder surfaces for the accepted skeleton. The
overview route is not a completed analytics dashboard.
