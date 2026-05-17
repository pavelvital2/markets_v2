# TESTING_FLOW_001

## Artifact Type

Testing design document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md`

Source-contract updates use only audited research RESULTS. No source project
files were inspected for this design continuation.

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

Provider tasks require tests for:

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

## Parser Contract/Export/Quality Testing

`TASK_TEST_PARSER_CONTRACT_EXPORT_QUALITY_001` must verify:

- required common mart columns and `schema_version`;
- valid and invalid provider identities;
- WB/Ozon compatibility id mappings;
- manifest required fields;
- checksum mismatch handling;
- forbidden bundle content detection;
- partial/failure data-quality summaries.

## WB Provider Migration Testing

`TASK_TEST_WB_PROVIDER_MIGRATION_001` must verify with synthetic or mocked
inputs:

- `source_system=wildberries` source defaults normalize to `wb`;
- WB `nmId` and supplier fields map to common aliases;
- suggest/filter/SERP/sellers outputs pass V2 contract validation;
- run reports, checkpoints, latest mirrors, and export integration are present;
- no WB/Ozon identifier join works without provider context.

## Ozon Provider Migration Testing

`TASK_TEST_OZON_PROVIDER_MIGRATION_001` must verify with sanitized fixtures or
mocked inputs:

- first 5 `webSuggestions*` behavior and dedupe;
- `tileGrid*` extraction and `absolute_position`;
- opaque `nextPage` handling without synthesized tokens;
- `items.length` is used instead of a permanent page-size constant;
- seller enrichment handles product-card state, missing sellers, progress, and resume;
- anti-bot or empty responses produce partial/failure quality status;
- no cookies, hardcoded cookie fallback, HAR, browser profile, or raw sensitive
  artifact enters export or logs.

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
