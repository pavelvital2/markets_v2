# TASK PACKET

## TASK_ID

```text
TASK_TEST_WB_PROVIDER_MIGRATION_001
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
project-runtime/agent-results/TASK_AUDIT_WB_PROVIDER_MIGRATION_001.md
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
Test WB provider migration
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
VALUE: high
OVERRIDE_REASON: Testing must verify provider migration, contract validation, and export/data-quality behavior without live scraping.
```

## DEPENDENCIES

```text
- TASK_AUDIT_WB_PROVIDER_MIGRATION_001 pass
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
Verify WB provider migration behavior with synthetic or mocked inputs.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_TEST_WB_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
```

## SCOPE_IN

```text
- run available WB provider tests
- verify source_system wildberries normalizes to wb
- verify nmId and supplier field mapping to common aliases
- verify suggest/filter/SERP/sellers outputs pass V2 contract validation
- verify run reports, checkpoints, latest mirrors, and export integration
- verify cross-provider joins require provider context
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
- project-docs/03_tasks/TASK_TEST_WB_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
```

## INPUTS

```text
- audit RESULT for TASK_AUDIT_WB_PROVIDER_MIGRATION_001
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_AUDIT_WB_PROVIDER_MIGRATION_001.md
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
- WB provider contract tests pass or limitations are explicit
- WB source identity normalizes to wb
- provider-neutral ids are present in common marts/export
- export validation passes with synthetic WB data
- no live marketplace access or secret is required
```

## EVIDENCE_REQUIREMENTS

```text
- commands run and results
- passed/failed test list
- explicit untested gaps if any
- confirmation that no source projects or secrets were accessed
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
project-runtime/agent-results/TASK_TEST_WB_PROVIDER_MIGRATION_001.md
```

## RISK_REQUIREMENTS

```text
- live WB behavior is not proven by default synthetic tests
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
