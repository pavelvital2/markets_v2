# ARCH_DATA_QUALITY_MODEL_001

## Artifact Type

Architecture document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`

No source project files were inspected for this document.

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

## Import Quality Behavior

Analytics import must:

- validate manifest and checksums;
- persist quality status from the bundle;
- preserve warnings and errors;
- surface partial data warnings in UI and Excel;
- reject or quarantine invalid bundles.

