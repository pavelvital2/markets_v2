# STAGE_PLAN_001

## Artifact Type

Stage plan. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`

No source project files were inspected for this document.

## Purpose

Define bounded implementation stages and workflow gates for Market Intelligence Platform.

## Stage 1: Source Discovery

Status: completed by audited dependency.

Accepted high-level facts:

- WB V1 operational staged parser exists.
- Ozon working Playwright/Chromium prototype exists.
- Ozon lacks WB-style runtime infrastructure.

Field-level facts remain unresolved in this design task because the detailed research report was not in the allowed read set.

## Stage 2: Design Baseline

Outputs:

- bounded architecture docs;
- runtime outline;
- audit gates;
- testing flow;
- initial dispatchable task packets;
- non-dispatchable owner proposal for unresolved business/formula decisions.

Mandatory next role after this design task:

```text
auditor
```

## Stage 3: Parser Skeleton

Dispatchable after design audit pass:

- `TASK_DEV_MARKET_PARSER_V2_SKELETON_001`

Expected result:

- clean parser project skeleton;
- common core placeholders;
- provider abstraction;
- config boundary;
- data path separation;
- CLI/API skeleton;
- contract validation skeleton;
- export bundle skeleton;
- tests skeleton.

Provider migration is out of scope for this stage.

## Stage 4: Source Contract Research

Dispatchable after design audit pass:

- `TASK_RESEARCH_WB_SOURCE_CONTRACTS_001`
- `TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001`

Expected result:

- exact source fields;
- sample-output contract details;
- source commands;
- state/checkpoint details;
- source tests;
- risks and gaps.

Both research tasks require mandatory audit.

## Stage 5: Contract Design Continuation

Dispatchable after both source-contract research tasks pass audit:

- `TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001`

Expected result:

- finalized WB contract;
- finalized Ozon contract;
- implementation packets for provider migration;
- audit and testing updates if needed.

## Stage 6: Analytics Skeleton

Dispatchable after design audit pass:

- `TASK_DEV_MARKET_ANALYTICS_SKELETON_001`

Expected result:

- clean analytics project skeleton;
- backend/API skeleton;
- import registry placeholders;
- manifest/checksum validation skeleton;
- auth placeholder;
- web skeleton;
- tests skeleton.

Full UI analytics implementation waits for accepted contracts and importer behavior.

## Stage 7: Provider Migration and Export

Not dispatchable from this design baseline. Requires Stage 4 and Stage 5 results.

Expected future work:

- WB provider migration;
- Ozon provider migration;
- run reports;
- checkpoints;
- latest mirrors;
- export bundle implementation.

## Stage 8: Market Intelligence MVP

Not dispatchable from this design baseline.

Expected future work:

- overview dashboard;
- query analytics;
- product analytics;
- seller analytics;
- marketplace comparison;
- data-quality dashboard;
- Excel export.

## Technical Writer Handoffs

Technical writer handoff is required after:

- accepted parser skeleton if developer-facing setup docs are created;
- accepted analytics skeleton if developer-facing setup docs are created;
- accepted MVP UI/API implementation before owner-facing usage;
- accepted runtime hardening before production use.

Technical writer must not run before the relevant developer/tester/auditor flow is complete.

