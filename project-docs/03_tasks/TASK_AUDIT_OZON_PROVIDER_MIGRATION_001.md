# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_OZON_PROVIDER_MIGRATION_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
audit
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
project-runtime/agent-results/TASK_DEV_OZON_PROVIDER_MIGRATION_001.md
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
Audit Ozon provider migration
```

## TASK_TYPE

```text
auditor
```

## TARGET_ROLE

```text
auditor
```

## REASONING_LEVEL

```text
VALUE: maximum
OVERRIDE_REASON: Audit covers browser/cookie safety, raw artifact exclusion, anti-bot states, source scope, and provider contract mapping.
```

## DEPENDENCIES

```text
- TASK_DEV_OZON_PROVIDER_MIGRATION_001 returned pass or fail
```

## DEPENDENCY_STATUS

```text
pending
```

## REQUESTED_BY_ROLE

```text
developer
```

## REQUESTED_BY_TASK

```text
TASK_DEV_OZON_PROVIDER_MIGRATION_001
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
NONE
```

## EXPECTED_EVIDENCE

```text
- changed-file scope check
- Ozon provider contract evidence
- source-project mutation check
- cookie/secret/raw artifact exposure check
- test evidence review
```

## EXPECTED_OUTPUT

```text
- auditor RESULT according to AGENT_RESULT_TEMPLATE
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
Audit Ozon provider migration before tester verification.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_DEV_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## SCOPE_IN

```text
- verify developer changed only allowed files
- verify parser_ozon was not modified
- verify source scope and forbidden raw/cookie/HAR access
- verify Ozon compatibility ids map to common aliases under source_system=ozon
- verify suggest, products, pagination, absolute_position, seller enrichment, progress/resume, and partial/failure statuses
- verify cookie configuration has no hardcoded local fallback
- verify export excludes raw sensitive artifacts
- verify tests or limitations are reported
```

## SCOPE_OUT

```text
- do not modify implementation
- do not run live scraping
- do not migrate WB provider logic
- do not define formulas or thresholds
- do not commit or push
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
- project-docs/03_tasks/TASK_DEV_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## INPUTS

```text
- developer RESULT for TASK_DEV_OZON_PROVIDER_MIGRATION_001
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_DEV_OZON_PROVIDER_MIGRATION_001.md
```

## EXPECTED_OUTPUTS

```text
- auditor RESULT according to AGENT_RESULT_TEMPLATE
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
- Ozon implementation satisfies architecture and audited research constraints
- no forbidden source project or raw/private data mutation occurred
- cookie and raw artifact security constraints are enforced
- partial/failure quality behavior is preserved
- audit RESULT includes mandatory audit evidence labels
```

## EVIDENCE_REQUIREMENTS

```text
- CHANGED_FILES_SCOPE_STATUS
- TASK_PACKET_SCHEMA_STATUS
- REPOSITORY_IDENTITY_STATUS
- FORBIDDEN_PATH_STATUS
- RUNTIME_MUTATION_STATUS
- EVIDENCE_STATUS
- SECRET_EXPOSURE_STATUS
- REASONING_LEVEL_COMPLIANCE
- VALIDATED_TASK_PACKETS
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
project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
```

## RISK_REQUIREMENTS

```text
- Ozon provider may require follow-up research if implementation exposed unaudited live-widget or raw-sensitivity facts
```

## MANDATORY_WORKFLOW

```text
auditor(pass) -> tester
auditor(fail) -> orchestrator
auditor(blocked) -> orchestrator
auditor(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
tester
```

## NEXT_ROLE_ON_FAIL

```text
orchestrator
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
none
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
On audit pass, orchestrator may dispatch TASK_TEST_OZON_PROVIDER_MIGRATION_001.
```

