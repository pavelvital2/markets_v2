# ARCH_DATA_QUALITY_MODEL_001

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

Define the initial data-quality model for parser runs, export bundles, analytics import, and UI warnings.

## Required Status Surfaces

Parser and analytics must preserve quality at these levels:

- run;
- component;
- query;
- product/SERP row;
- seller row;
- bridge row;
- export bundle;
- analytics import.

## Run Statuses

The Data Quality Dashboard must show:

```text
success
partial
failed
```

The user-facing usability status for analytics must be one of:

```text
valid_for_reports
partial_use_with_warning
invalid_for_reports
```

Audited source-contract evidence confirms source row/run statuses including:

```text
success
empty
error
dry_run
partial
failed
not_ready
```

Provider migration must map source statuses into V2 run, component, row, export,
and analytics-import quality states without hiding partial data.

## Required Quality Signals

The system must record:

- partial runs;
- errors per component;
- missing pages;
- empty products;
- missing seller id;
- duplicate product positions;
- unexpected CSV columns;
- schema version mismatch;
- checksum mismatch;
- stale latest export.

## Ozon-Specific Quality Constraints

Ozon collection must treat frontend and anti-bot behavior as unstable:

- pagination state is opaque;
- `items.length` must be used instead of a permanent page-size constant;
- empty pages or anti-bot responses must stop the run or produce partial/failure status;
- seller enrichment is slow and block-sensitive and must support progress/resume.
- compatibility fields `nmId` and `supplier_id` must not be used without
  `source_system=ozon` provider context.

## WB-Specific Quality Constraints

WB migration must normalize V1 `source_system=wildberries` to V2
`source_system=wb`. Any output retaining `wildberries` in common marts or
export bundles is invalid for reports.

WB source details that remain unresolved by audited results, such as exact
SQLite schema columns or generated CSV samples, must be treated as limitations
or research dependencies if implementation needs them.

## Dashboard Requirements

The Data Quality Dashboard must show:

- `run_id`;
- run timestamp;
- marketplace;
- run status;
- successful and failed components;
- processed queries;
- pages/portions;
- products;
- enriched sellers;
- errors;
- partially collected queries;
- missing pages;
- report usability;
- `data_confidence_level`.

## Confidence Formula Boundary

The TZ requires `data_confidence_level`, but this design does not define a numeric formula. Formula definition requires a bounded design or owner decision task before it is used as a management fact.

Until that decision exists, provider migration may pass through quality signals
and usability statuses but must not invent a numeric confidence formula.

## Import Quality Behavior

Analytics import must:

- validate manifest and checksums;
- persist quality status from the bundle;
- preserve warnings and errors;
- surface partial data warnings in UI and Excel;
- reject or quarantine invalid bundles.
