# Bootstrap Design Intake 001

## Purpose

Record the first bounded design intake for Market Intelligence Platform from
the owner source brief only.

## Source Of Truth

- `project-input/TZ.md`

## Product Boundary

The product consists of two new independent projects:

- `market-parser-v2`: provider-aware external market parser for WB and Ozon.
- `market-analytics`: analytics application that imports stable parser export
  bundles and presents Market Intelligence views.

Existing projects are read-only factual sources:

- `/home/pavel/projects/wb-parser-v1`
- `/home/pavel/projects/parser_ozon`
- `/home/pavel/projects/parser_ozon/docs/ozon_parser/`

## Confirmed Design Constraints From Source Brief

- Parser and analytics are separate projects.
- Parser must expose a stable analytics export bundle instead of requiring
  analytics to read parser internals.
- WB and Ozon identifiers must never be joined without `marketplace` or
  `source_system`.
- Parser outputs must include run lineage, quality status, reports, latest
  mirrors, checksums, and schema versioning where applicable.
- Analytics MVP must include overview, query, product, seller, marketplace
  comparison, data quality, history at imported-run level, Excel export, and
  authentication.
- Own-store data, product matching, and Decision Layer are future contours and
  must not be represented as confirmed MVP calculations.
- Exact profitability, margin, competitor sales, conversion, ad efficiency, and
  supply economics are out of scope until confirmed source systems exist.
- Cookies, API keys, auth tokens, raw secrets, and unsanitized HAR/fixtures must
  not enter Git, logs, UI, or export bundles.

## Immediate Design Gap

The source brief explicitly requires factual confirmation of existing WB and
Ozon parser fields, commands, outputs, tests, checkpoints, state, reports, and
error/status behavior before data contracts and implementation task breakdown
can be designed safely.

This is a research dependency, not an owner-decision gap, because the missing
facts are available from allowed local source projects named in the brief.

## Downstream Work Artifact Classification

- `project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`
  - Classification: DISPATCHABLE TASK_PACKET
  - Purpose: bounded research dependency for source project discovery.
- `project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md`
  - Classification: DISPATCHABLE TASK_PACKET
  - Purpose: bounded design continuation after audited research passes.

## Bootstrap Continuation

```text
BOOTSTRAP_CONTINUATION_STATUS: downstream_task_packet
BOOTSTRAP_CONTINUATION_REF: project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
```
