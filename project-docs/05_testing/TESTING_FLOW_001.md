# TESTING_FLOW_001

## Artifact Type

Testing design document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`

No source project files were inspected for this document.

## Purpose

Define testing flow for parser, analytics, export/import, UI, and runtime behavior.

## Current Design Task

No implementation testing is required for `TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001`.

## Parser Skeleton Testing

Required for parser skeleton:

- project can install or initialize in its selected environment;
- CLI/API skeleton commands exist without live scraping;
- provider registry recognizes `wb`, `ozon`, and `all`;
- contract validation skeleton can report pass/fail on synthetic sanitized fixtures;
- export skeleton can produce a placeholder manifest/checksum layout without secrets;
- tests do not require real cookies or live marketplace access.

## Source Contract Research Testing

Research tasks do not implement tests. They must inventory existing tests from source projects where allowed and report their relevance.

## Provider Migration Testing

Future provider tasks require tests for:

- suggest extraction;
- filter behavior where applicable;
- SERP extraction;
- seller enrichment;
- checkpoint/resume;
- latest mirrors;
- run reports;
- contract validation;
- partial/failure statuses.

Live scraping must not be required for default test runs unless a task explicitly allows it.

## Analytics Skeleton Testing

Required for analytics skeleton:

- application initializes;
- health endpoint works if implemented;
- manifest validator handles valid and invalid synthetic manifests;
- checksum validator detects mismatch;
- import registry preserves run and provider identity;
- auth placeholder protects non-public surfaces where implemented;
- tests do not require real parser output or secrets.

## MVP Testing

Future MVP tester tasks must cover:

- overview dashboard;
- query analytics;
- product analytics;
- seller analytics;
- marketplace comparison;
- data-quality dashboard;
- filters and search;
- partial-data warnings;
- Excel exports and sheets.

## Technical Writer Trigger

Technical writer runs after tester pass when documentation is required by a task packet. Technical writer must not replace developer, tester, or auditor verification.

