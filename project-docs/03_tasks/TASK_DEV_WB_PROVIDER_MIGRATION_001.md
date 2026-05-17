# TASK PACKET

## TASK_ID

```text
TASK_DEV_WB_PROVIDER_MIGRATION_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
normal
```

## SUPERSEDES

```text
NONE
```

## SUPERSEDED_BY

```text
NONE
```

## CORRECTION_OF

```text
NONE
```

## SOURCE_RESULT_REF

```text
project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
```

## ATTEMPT_NO

```text
NONE
```

## FAILURE_TYPE

```text
none
```

## TASK_TITLE

```text
Migrate WB provider into market-parser-v2
```

## TASK_TYPE

```text
developer
```

## TARGET_ROLE

```text
developer
```

## REASONING_LEVEL

```text
VALUE: high
OVERRIDE_REASON: Provider migration must preserve audited source contracts while normalizing identifiers and quality/export behavior.
```

## DEPENDENCIES

```text
- TASK_DEV_MARKET_PARSER_V2_SKELETON_001 audit pass
- TASK_TEST_PARSER_CONTRACT_EXPORT_QUALITY_001 pass
- TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001 pass
```

## DEPENDENCY_STATUS

```text
pending
```

## REQUESTED_BY_ROLE

```text
designer
```

## REQUESTED_BY_TASK

```text
TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001
```

## RESEARCH_QUESTION_ID

```text
NONE
```

## RESEARCH_PURPOSE

```text
NONE
```

## RESEARCH_QUESTIONS

```text
NONE
```

## ALLOWED_SOURCES

```text
- /home/pavel/projects/wb-parser-v1/README.md
- /home/pavel/projects/wb-parser-v1/ARCHITECTURE.md
- /home/pavel/projects/wb-parser-v1/PROJECT_STATE.md
- /home/pavel/projects/wb-parser-v1/DEVELOPMENT_STAGES.md
- /home/pavel/projects/wb-parser-v1/app/suggest/alpha.py
- /home/pavel/projects/wb-parser-v1/app/filter/engine.py
- /home/pavel/projects/wb-parser-v1/app/serp/engine.py
- /home/pavel/projects/wb-parser-v1/app/sellers/engine.py
- /home/pavel/projects/wb-parser-v1/app/common/paths.py
- /home/pavel/projects/wb-parser-v1/app/common/csv_io.py
- /home/pavel/projects/wb-parser-v1/app/common/runner.py
- /home/pavel/projects/wb-parser-v1/state/run_reports/latest.json
```

## FORBIDDEN_SOURCES

```text
- /home/pavel/projects/wb-parser-v1/* outside ALLOWED_SOURCES
- /home/pavel/projects/parser_ozon/*
- WB generated data files outside the audited latest report sample
- cookies/*
- secrets/*
- credentials/*
```

## EXPECTED_EVIDENCE

```text
NONE
```

## EXPECTED_OUTPUT

```text
NONE
```

## RETURN_TO_REQUESTER_AFTER_AUDIT_PASS

```text
no
```

## RETURN_TO_ROLE_AFTER_AUDIT_PASS

```text
none
```

## RETURN_TASK_AFTER_AUDIT_PASS

```text
NONE
```

## PURPOSE

```text
Implement the WB provider in market-parser-v2 using audited WB source-contract evidence and V2 common contracts.
```

## SOURCE_OF_TRUTH

```text
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
```

## SCOPE_IN

```text
- implement WB provider components for suggest, filter, serp, sellers, and export integration behind the V2 provider abstraction
- preserve provider-specific raw/staging outputs and write common normalized marts
- normalize source_system from wildberries to wb in common marts and export
- add marketplace, schema_version, data_quality_status, and provider-neutral identifiers
- map WB nmId to external_product_id and WB supplier fields to external_seller_id/seller_name
- integrate WB run reports, checkpoints/resume, latest mirrors, and status/error reporting with V2 common runtime
- preserve CSV utf-8-sig and semicolon delimiter where WB compatibility is required
- add tests using synthetic, fixture, or mocked data without live marketplace access
```

## SCOPE_OUT

```text
- do not modify wb-parser-v1
- do not read WB source files outside ALLOWED_SOURCES
- do not migrate Ozon provider logic
- do not run live scraping unless a future task explicitly allows it
- do not require cookies or secrets
- do not define analytics formulas or thresholds
- do not guess unresolved WB SQLite/config/test/generated-output facts
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/DEVELOPER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_DEV_WB_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
```

## INPUTS

```text
- audited WB source-contract research RESULT
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
```

## EXPECTED_OUTPUTS

```text
- WB provider implementation in market-parser-v2
- tests for WB provider contract behavior
- developer RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- market-parser-v2/*
```

## FORBIDDEN_FILE_CHANGES

```text
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
- agent-system/*
- project-input/*
- project-runtime/*
- project-docs/*
- .git/*
- secrets/*
- credentials/*
- cookies/*
- data/*
- logs/*
```

## ACCEPTANCE_CRITERIA

```text
- WB provider runs through V2 provider abstraction without requiring Ozon code
- common marts/export use source_system=wb and provider-neutral identifiers
- WB compatibility fields do not leak into cross-provider joins without provider context
- run reports, checkpoints, latest mirrors, and data-quality statuses are integrated
- export bundle validates through V2 contract/export checks
- tests do not require live scraping or secrets
- unresolved WB source facts are reported as gaps or research dependencies, not guessed
```

## EVIDENCE_REQUIREMENTS

```text
- changed file list
- test command results or explicit limitation
- WB contract validation evidence
- export validation evidence
- confirmation that wb-parser-v1 was not modified
- confirmation that no secrets/cookies were used or logged
```

## SETUP_HOOKS

```text
NONE
```

## LAUNCH_HOOKS

```text
NONE
```

## RESULT_PATH

```text
project-runtime/agent-results/TASK_DEV_WB_PROVIDER_MIGRATION_001.md
```

## RISK_REQUIREMENTS

```text
- WB exact SQLite/config/test/generated-output facts remain unresolved outside audited results
- live marketplace behavior is not proven by default tests
```

## MANDATORY_WORKFLOW

```text
developer(pass) -> auditor
developer(fail) -> auditor
developer(blocked) -> orchestrator
developer(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
auditor
```

## NEXT_ROLE_ON_FAIL

```text
auditor
```

## NEXT_ROLE_ON_BLOCKED

```text
orchestrator
```

## NEXT_ROLE_ON_GAP

```text
orchestrator
```

## AUDIT_REQUIREMENTS

```text
mandatory
```

## TESTING_REQUIREMENTS

```text
mandatory
```

## DOCUMENTATION_REQUIREMENTS

```text
none
```

## FILESYSTEM_GOVERNANCE

```text
agent-system/02_runtime/FILESYSTEM_GOVERNANCE.md
```

## RUNTIME_GOVERNANCE

```text
agent-system/02_runtime/ORCHESTRATOR_RUNTIME_LOOP.md
agent-system/04_state/RUNTIME_STATE_SCHEMA.md
agent-system/02_runtime/STATE_TRANSITION_RULES.md
agent-system/02_runtime/GOVERNANCE_AUTHORITY.md
agent-system/02_runtime/ACCEPTED_STATE_LOCKING.md
```

## RESULT_FORMAT

```text
agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
```

## TERMINAL_CONDITIONS

```text
NONE
```

## NOTES

```text
Direct WB source inspection is limited to ALLOWED_SOURCES and must not create new source-contract requirements beyond audited research evidence.
```

