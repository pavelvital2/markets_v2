# market-analytics

Clean analytics application skeleton for importing sanitized parser export
bundles and serving authenticated analytics API/web surfaces.

## Boundaries

- Imports only parser export bundles:
  - `manifest.json`
  - `bundle.tar.gz`
  - `checksums.sha256`
- Preserves `run_id`, `marketplace`, and `source_system` for every imported run.
- Keeps provider identifiers scoped by `marketplace`/`source_system`.
- Rejects invalid provider identity, unsupported schema versions, checksum
  mismatches, missing required marts for usable bundles, and secret-like bundle
  files.
- Does not scrape marketplaces.
- Does not read parser internal folders as a production integration.
- Does not create or log cookies, credentials, tokens, or other secrets.

## Local Skeleton Commands

```bash
cd market-analytics
PYTHONPATH=src python -m unittest discover -s tests
```

FastAPI runtime dependencies are declared in `pyproject.toml`. The basic auth
placeholder requires both environment variables before API/web routes can be
used:

```bash
MARKET_ANALYTICS_BASIC_AUTH_USERNAME=<user>
MARKET_ANALYTICS_BASIC_AUTH_SECRET=<set in local environment>
```

No default password is provided.
