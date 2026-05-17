# market-parser-v2

Clean skeleton for the marketplace parser V2 boundary.

This project intentionally contains no migrated WB or Ozon scraping logic. The
current implementation is limited to common runtime contracts, provider
registration, path configuration, validation scaffolding, export-bundle layout,
and offline synthetic tests.

## Boundaries

- Common core: config, run identity, provider registry, contract validation,
  data-quality placeholders, export layout, CLI/API skeleton.
- Providers: `wb` and `ozon` placeholders only.
- Marketplace selector: `wb`, `ozon`, or `all`.
- Network access: not used by this skeleton.
- Secrets/cookies: represented by paths only; contents are never read, logged,
  committed, or exported.

## Local Checks

```bash
PYTHONPATH=src python -m unittest discover -s tests
PYTHONPATH=src python -m market_parser_v2.cli providers
PYTHONPATH=src python -m market_parser_v2.cli plan --marketplace all
```

## Export Layout

The export skeleton models the accepted analytics boundary:

```text
latest.json
{marketplace}/{run_id}/manifest.json
{marketplace}/{run_id}/bundle.tar.gz
{marketplace}/{run_id}/checksums.sha256
```

The bundle contains analytics-only placeholder files:

```text
marts/queries.csv
marts/products.csv
marts/sellers.csv
marts/seller_query_product_bridge.csv
quality/data_quality_summary.json
metadata/contract.json
```
