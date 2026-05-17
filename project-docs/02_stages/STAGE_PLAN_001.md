# STAGE_PLAN_001

## Artifact Type

Stage plan. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md`

Source-contract updates use only audited research RESULTS. No source project
files were inspected for this design continuation.

## Purpose

Define bounded implementation stages and workflow gates for Market Intelligence Platform.

## Stage 1: Source Discovery

Status: completed by audited dependency.

Accepted high-level facts:

- WB V1 operational staged parser exists.
- Ozon working Playwright/Chromium prototype exists.
- Ozon lacks WB-style runtime infrastructure.

Historical note from the first design baseline: field-level facts were
unresolved before source-contract research. Field-level provider facts used for
migration are now bounded by `ARCH_PROVIDER_SOURCE_CONTRACTS_001.md` and the
audited source-contract RESULTS.

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

Mandatory audit task for this stage:

- `TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001`

No developer/provider migration task may run before this audit passes.

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

## Stage 7: Common Parser Contract, Export, and Quality Enforcement

Dispatchable after parser skeleton audit pass and Stage 5 design-continuation
audit pass:

- `TASK_DEV_PARSER_CONTRACT_EXPORT_QUALITY_001`
- `TASK_AUDIT_PARSER_CONTRACT_EXPORT_QUALITY_001`
- `TASK_TEST_PARSER_CONTRACT_EXPORT_QUALITY_001`

Expected result:

- V2 schema definitions for common marts and bridge;
- provider identity validation;
- source compatibility mapping helpers;
- manifest/checksum/export validation;
- data-quality status mapping;
- secret/raw artifact exclusion checks.

## Stage 8: Provider Migration

Dispatchable after Stage 7 implementation passes audit/testing and provider
dependencies are ready:

- `TASK_DEV_WB_PROVIDER_MIGRATION_001`
- `TASK_AUDIT_WB_PROVIDER_MIGRATION_001`
- `TASK_TEST_WB_PROVIDER_MIGRATION_001`
- `TASK_DEV_OZON_PROVIDER_MIGRATION_001`
- `TASK_AUDIT_OZON_PROVIDER_MIGRATION_001`
- `TASK_TEST_OZON_PROVIDER_MIGRATION_001`

Expected result:

- WB provider behind V2 provider abstraction;
- Ozon provider behind V2 provider abstraction;
- run reports, checkpoints, latest mirrors, and export integration per provider;
- no source project mutation;
- no live scraping required by default tests;
- partial/failure quality behavior for Ozon unstable frontend and anti-bot cases.

## Stage 9: Market Intelligence MVP

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
