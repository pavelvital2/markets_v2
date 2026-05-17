# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001
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
project-runtime/agent-results/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
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
Audit market analytics skeleton
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
VALUE: high
OVERRIDE_REASON: Audit covers analytics/parser boundary, export bundle import, manifest/checksum validation, run registry identity fields, auth placeholder, and synthetic tests.
```

## DEPENDENCIES

```text
- TASK_DEV_MARKET_ANALYTICS_SKELETON_001 returned pass or fail
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
developer
```

## REQUESTED_BY_TASK

```text
TASK_DEV_MARKET_ANALYTICS_SKELETON_001
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
- changed-file scope check
- analytics/parser boundary evidence
- export bundle import boundary evidence
- manifest/checksum validation evidence
- run registry identity fields evidence
- auth placeholder evidence
- synthetic test evidence
- security/secret exposure check
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
Audit the clean market analytics skeleton before it can become an accepted implementation baseline.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
- project-docs/04_audits/AUDIT_GATES_001.md
- project-docs/01_architecture/ARCH_MARKET_ANALYTICS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
```

## SCOPE_IN

```text
- verify developer changed only allowed files
- verify analytics does not scrape marketplaces
- verify import reads only parser export bundle boundary
- verify manifest/checksum validation skeleton exists
- verify run registry placeholders preserve run_id, marketplace, and source_system
- verify provider-aware data model placeholders exist
- verify auth placeholder exists and has no default secrets
- verify overview route UI skeleton exists only
- verify tests use synthetic bundles only
- verify limitations around missing FastAPI dependency are reported
```

## SCOPE_OUT

```text
- do not modify implementation
- do not run live scraping
- do not inspect source projects directly
- do not implement analytics features
- do not commit or push
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
- project-docs/04_audits/AUDIT_GATES_001.md
- project-docs/01_architecture/ARCH_MARKET_ANALYTICS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
```

## INPUTS

```text
- developer RESULT for TASK_DEV_MARKET_ANALYTICS_SKELETON_001
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
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
- cookies/*
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
```

## ACCEPTANCE_CRITERIA

```text
- changed-file scope is limited to market-analytics/* or allowed testing docs
- analytics skeleton is separate from parser skeleton
- importer boundary is export bundle based
- manifest/checksum validation skeleton exists
- run registry placeholders preserve run_id, marketplace, and source_system
- auth placeholder exists without default credentials
- tests use synthetic bundles only and do not require secrets or real parser output
- no marketplace scraping exists
```

## EVIDENCE_REQUIREMENTS

```text
- CHANGED_FILES_SCOPE_STATUS
- REPOSITORY_IDENTITY_STATUS
- ANALYTICS_BOUNDARY_STATUS
- IMPORTER_CONTRACT_STATUS
- AUTH_SECRET_STATUS
- TEST_STATUS
- FORBIDDEN_PATH_STATUS
- REASONING_LEVEL_COMPLIANCE
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
project-runtime/agent-results/TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001.md
```

## RISK_REQUIREMENTS

```text
- audit must distinguish missing optional runtime dependencies from skeleton correctness
```

## MANDATORY_WORKFLOW

```text
auditor(pass) -> orchestrator
auditor(fail) -> developer
auditor(blocked) -> orchestrator
auditor(gap) -> orchestrator
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
On audit pass, route accepted analytics skeleton to aggregate checkpoint.
```
