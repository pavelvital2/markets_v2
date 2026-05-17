# ARCH_MARKET_PARSER_V2_001

## Artifact Type

Architecture document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md`

Source-contract updates use only audited research RESULTS. No source project
files were inspected for this design continuation.

## Purpose

Define the bounded architecture for `market-parser-v2`, the new clean parser for external WB and Ozon market data.

## Product Boundary

`market-parser-v2` collects and prepares external marketplace data only. It must not become the analytics application and must not contain Decision Layer business recommendations.

The parser must be provider-aware:

- common core: run orchestration, config, state, reports, logging, checkpoints, validation, export;
- WB provider: WB collection and normalization;
- Ozon provider: Ozon collection and normalization.

The parser must support marketplace execution for:

- `wb`;
- `ozon`;
- `all`.

## Confirmed Source Facts

The audited research result confirms these high-level facts:

- WB V1 is an operational staged parser with CLI, SQLite state, checkpoints, latest mirrors, run reports, Web UI, and CSV contracts.
- Ozon is a working Playwright/Chromium prototype with WB-shaped outputs.
- Ozon does not have WB-style runtime infrastructure.
- No live scraping was run by the research task.
- WB source-system defaults may differ from the TZ requirement: research reported a risk that WB code defaults appear as `wildberries`, while TZ requires `wb`.

The audited WB/Ozon source-contract results now provide enough evidence to
design provider migration tasks for confirmed data contracts, runtime gaps,
export boundaries, and security constraints. Final source-contract mappings are
bounded in `ARCH_PROVIDER_SOURCE_CONTRACTS_001.md`.

Still unresolved and not safe to guess:

- score formulas and thresholds;
- exact generated CSV samples outside audited results;
- WB test/config/SQLite internals outside audited results;
- current live Ozon frontend shape;
- raw Ozon response/HTML sensitivity before sanitization.

## Pipeline Boundary

Allowed pipeline shape:

```text
suggest -> filter -> serp -> sellers -> export
```

Components are enabled only where they are confirmed for a provider. A provider may implement a component differently, but it must write provider-specific raw/staging data and normalized common marts.

## Storage Layers

The parser must separate:

- raw provider data;
- staging provider data;
- normalized marts;
- run reports;
- checkpoints;
- latest mirrors;
- analytics export bundles.

Code, data, logs, secrets, cookies, raw archives, and temporary files must be stored separately. Data, logs, cookies, secrets, raw archives, and temporary files must not be committed.

## Run Identity

Every collection run must have a stable `run_id`. All persisted rows and reports that belong to a run must preserve this value.

The parser must maintain latest mirrors for convenience, but analytics must treat `run_id` history as canonical and must not depend only on latest files.

## Provider Identity

Provider identity is mandatory for all cross-provider records.

Required values:

```text
source_system = wb
source_system = ozon
```

WB and Ozon identifiers are local to their marketplace. WB `nmId` and Ozon product identifiers must never be joined without `source_system` or `marketplace`.

Recommended keys:

```text
source_system + external_product_id
source_system + external_seller_id
source_system + query
```

If an intermediate compatibility field named `nmId` is ever used for Ozon data, it must be documented as a compatibility field only and must not be treated as WB `nmId`.

## WB Provider Boundary

WB provider migration must use the audited WB source-contract result as the
contract evidence. V2 must normalize V1 `source_system=wildberries` to
`source_system=wb`, add V2-only `marketplace`, `schema_version`, provider-neutral
identifier aliases, and `data_quality_status`, and preserve run-scoped outputs,
latest mirrors, reports, checkpoints, and CSV compatibility where required.

## Ozon Provider Boundary

Ozon provider implementation must treat the browser/runtime behavior as provider-specific.

The TZ requires:

- Chromium/browser session for suggest;
- extraction from `widgetStates["webSuggestions-*"]`;
- only first 5 dropdown suggestions as search queries;
- opaque pagination state for SERP;
- product grid extraction from `widgetStates["tileGridDesktop-*"]`;
- absolute positions for analytics compatibility;
- seller enrichment from product card HTML state;
- configurable throttle/concurrency;
- partial/failure status for anti-bot or empty page behavior.

The audited Ozon source-contract result confirms field-level prototype
contracts, extraction behavior, tests, missing runtime infrastructure, and
security risks. V2 must treat WB-shaped fields such as `nmId` and `supplier_id`
as compatibility fields only and must normalize them to provider-aware common
aliases.

## Export Responsibility

`market-parser-v2` must produce a stable analytics export bundle. `market-analytics` must not read internal parser folders directly in production mode.

Export details are bounded in `ARCH_EXPORT_CONTRACT_001.md`.

## Non-Goals

The parser must not implement:

- exact profit;
- exact margin;
- factual revenue;
- competitor sales;
- ad efficiency;
- card conversion;
- exact cost price;
- supply economics;
- own-store ingestion;
- product master matching;
- Decision Layer recommendations.

These require confirmed future data sources and separate tasks.

## Required Follow-Up

- audit of this source-contract design continuation;
- common parser contract/export/data-quality implementation task;
- bounded WB provider migration task;
- bounded Ozon provider migration task;
- audit and testing tasks for each implementation task;
- owner/design proposal for unresolved formulas, thresholds, and partial-data policy.
