# ARCH_MARKET_ANALYTICS_001

## Artifact Type

Architecture document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`

No source project files were inspected for this document.

## Purpose

Define the bounded architecture for `market-analytics`, the new analytics application for external WB/Ozon market intelligence.

## Product Boundary

`market-analytics` is a separate application created from scratch. It imports parser export bundles, stores run history, validates data quality, serves web/API analytics, and creates Excel exports.

It must not scrape WB/Ozon directly and must not read internal parser folders in production mode.

## Recommended Technical Shape

The TZ recommends:

```text
Python + FastAPI + PostgreSQL + web UI + worker/scheduler + systemd + Nginx
```

An alternative stack is allowed only if it covers import, history, API, UI, Excel export, authorization, and operations requirements.

## Core Domains

The MVP analytics domain is external Market Intelligence:

- imported run registry;
- marketplace/source-system aware entities;
- query analytics;
- product analytics;
- seller analytics;
- WB/Ozon comparison by comparable query/query group;
- data quality dashboard;
- Excel export;
- basic admin settings for sources/imports/schedules/errors/users/export/signal thresholds.

Future domains are architectural placeholders only:

- Own Store Intelligence;
- Product Matching;
- Decision Layer.

## Import Boundary

Analytics must import only stable parser export bundles:

```text
latest.json
{marketplace}/{run_id}/manifest.json
{marketplace}/{run_id}/bundle.tar.gz
{marketplace}/{run_id}/checksums.sha256
```

Import must:

- validate manifest structure;
- validate checksums;
- persist `run_id`;
- preserve `marketplace` and `source_system`;
- store import status;
- mark data quality;
- warn users about partial data;
- reject or quarantine invalid bundles.

## History Boundary

Analytics must preserve all imported runs, not only latest data. History and dynamics are based on run comparisons.

Required historical views include:

- position changes;
- price changes;
- rating changes;
- review-count changes;
- new/lost products;
- new/lost sellers;
- seller visibility changes;
- query result-size changes;
- price-corridor changes;
- competition changes by query.

## API Functional Coverage

Minimum coverage from the TZ:

```text
GET /analytics/overview
GET /analytics/runs
GET /analytics/data-quality
GET /analytics/queries
GET /analytics/queries/{query_id}
GET /analytics/products
GET /analytics/products/{product_id}
GET /analytics/sellers
GET /analytics/sellers/{seller_id}
GET /analytics/marketplaces/compare
GET /analytics/signals
GET /analytics/export
```

Exact paths may change during API design if functional coverage is preserved.

## UI Boundary

The first screen must be a management dashboard, not one large table.

Required dashboard content:

- marketplace switcher: WB, Ozon, both;
- analysis period;
- last update date;
- latest parser run status;
- query/product/seller counts;
- collection error count;
- completeness/partial data indicator;
- top queries;
- top sellers by visibility;
- top products by visibility;
- price summaries;
- rating and review summaries;
- market opportunities;
- data-quality problems.

## Excel Export Boundary

Excel export is mandatory. Exports must include generation date, marketplace, period, run reference, data source description, filters where applicable, and partial-data warnings.

Minimum export sets are defined in the TZ and must be implemented through bounded export tasks after skeleton and import contracts are accepted.

## Metric Formula Boundary

The TZ names scores such as `visibility_score`, `competition_score`, `opportunity_score`, `price_index`, and `data_confidence_level`.

This document does not define formulas for those scores. Formula work must be a bounded design or owner-decision task before the metrics are used as management facts.

