# AUDIT_GATES_001

## Artifact Type

Audit design document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`

No source project files were inspected for this document.

## Purpose

Define mandatory audit gates for the initial project decomposition.

## Gate A: Design Continuation Audit

Task packet:

```text
project-docs/03_tasks/TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

Auditor must verify:

- design used only allowed docs and audited result;
- changed paths are within current task `ALLOWED_FILE_CHANGES`;
- no forbidden files were modified;
- downstream task-like artifacts are explicitly classified;
- dispatchable task packets are bounded and contain required fields;
- no developer is recommended directly before design audit;
- gaps are reported instead of guessed.

## Gate B: Research Dependency Audits

Future research tasks:

- `TASK_RESEARCH_WB_SOURCE_CONTRACTS_001`
- `TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001`

Each research result must be audited before it can influence design or implementation.

## Gate C: Parser Skeleton Audit

After `TASK_DEV_MARKET_PARSER_V2_SKELETON_001`, auditor must verify:

- no source project was modified;
- skeleton respects parser/analytics boundary;
- config/secrets/data/log paths are separated;
- provider identity rules are present;
- export skeleton does not include forbidden files;
- tests skeleton exists where required by the task.

## Gate D: Analytics Skeleton Audit

After `TASK_DEV_MARKET_ANALYTICS_SKELETON_001`, auditor must verify:

- analytics does not scrape marketplaces;
- import reads only export bundle boundary;
- manifest/checksum validation skeleton exists;
- run registry preserves `run_id`, `marketplace`, and `source_system`;
- auth placeholder exists;
- tests skeleton exists where required by the task.

## Gate E: Contract Continuation Audit

After `TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001`, auditor must verify:

- finalized contracts cite audited research;
- unresolved fields are marked as gaps or optional;
- implementation packets are bounded;
- provider migration tasks do not rely on unverified assumptions.

## Gate F: MVP Implementation Audits

Future MVP implementation tasks require audits for:

- API behavior;
- UI behavior;
- data quality warnings;
- Excel export;
- history and dynamics;
- security constraints;
- runtime exposure.

