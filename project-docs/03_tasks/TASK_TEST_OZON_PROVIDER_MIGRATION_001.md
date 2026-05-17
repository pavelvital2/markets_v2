# TASK PACKET

## TASK_ID

```text
TASK_TEST_OZON_PROVIDER_MIGRATION_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
testing
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
project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
```

## ATTEMPT_NO

```text
1
```

## FAILURE_TYPE

```text
none
```

## TASK_TITLE

```text
Test Ozon provider migration
```

## TASK_TYPE

```text
tester
```

## TARGET_ROLE

```text
tester
```

## REASONING_LEVEL

```text
VALUE: maximum
OVERRIDE_REASON: Testing covers browser-derived extraction behavior, anti-bot/empty states, cookie safety, and raw artifact exclusion.
```

## DEPENDENCIES

```text
- TASK_AUDIT_OZON_PROVIDER_MIGRATION_001 pass
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
NONE
```

## FORBIDDEN_SOURCES

```text
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
- cookies/*
- browser-profile/*
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
Verify Ozon provider migration behavior with sanitized fixtures or mocked browser responses.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_TEST_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
```

## SCOPE_IN

```text
- run available Ozon provider tests
- verify webSuggestions* first 5 behavior and dedupe
- verify tileGrid* extraction and absolute_position
- verify opaque nextPage handling without synthesized tokens
- verify items.length is used instead of a permanent page-size constant
- verify seller enrichment handles product-card state, missing sellers, progress, and resume
- verify anti-bot or empty responses produce partial/failure data-quality status
- verify cookie, HAR, browser profile, raw sensitive artifact, and log exclusion
```

## SCOPE_OUT

```text
- do not modify implementation
- do not inspect source projects directly
- do not run live scraping
- do not require cookies or secrets
- do not define formulas or thresholds
- do not commit or push
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/TESTER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_TEST_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
```

## INPUTS

```text
- audit RESULT for TASK_AUDIT_OZON_PROVIDER_MIGRATION_001
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
```

## EXPECTED_OUTPUTS

```text
- tester RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
NONE
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-input/*
- project-docs/*
- project-runtime/*
- .git/*
- secrets/*
- credentials/*
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
```

## ACCEPTANCE_CRITERIA

```text
- Ozon provider contract tests pass or limitations are explicit
- Ozon compatibility ids are provider-scoped and normalized in common marts/export
- Ozon anti-bot/empty/missing seller cases preserve partial/failure quality
- export validation proves forbidden raw/cookie/HAR/browser-profile artifacts are excluded
- no live marketplace access or secret is required
```

## EVIDENCE_REQUIREMENTS

```text
- commands run and results
- passed/failed test list
- explicit untested gaps if any
- confirmation that no source projects, cookies, browser profiles, or secrets were accessed
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
project-runtime/agent-results/TASK_TEST_OZON_PROVIDER_MIGRATION_001.md
```

## RISK_REQUIREMENTS

```text
- live Ozon behavior and current widget shape are not proven by default synthetic tests
```

## MANDATORY_WORKFLOW

```text
tester(pass) -> orchestrator
tester(fail) -> developer
tester(blocked) -> orchestrator
tester(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
orchestrator
```

## NEXT_ROLE_ON_FAIL

```text
developer
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
none
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
NONE
```
