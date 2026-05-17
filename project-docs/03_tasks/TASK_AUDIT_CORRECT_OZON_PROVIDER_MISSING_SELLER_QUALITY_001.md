# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001
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
TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001
```

## SOURCE_RESULT_REF

```text
project-runtime/agent-results/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
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
Audit Ozon missing seller quality correction
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
OVERRIDE_REASON: Audit verifies row-level quality propagation for Ozon missing seller enrichment and focused/full test evidence.
```

## DEPENDENCIES

```text
- TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001 returned pass
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
TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001
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
- /home/pavel/projects/parser_ozon/*
- /home/pavel/projects/wb-parser-v1/*
- raw Ozon outputs, raw fixtures, HAR files, cookies, browser profiles, and generated private data
- secrets/*
- credentials/*
```

## EXPECTED_EVIDENCE

```text
- changed-file scope check
- row-level missing seller quality propagation evidence
- focused and full unittest evidence
- cookie/secret/raw artifact exposure check
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
Audit the correction for Ozon missing seller row-level quality propagation before returning to the main Ozon provider audit/test flow.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_AUDIT_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-docs/03_tasks/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-runtime/agent-results/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
```

## SCOPE_IN

```text
- verify correction changed only market-parser-v2/*
- verify missing or blocked seller enrichment downgrades affected provider/common/export product rows from valid_for_reports to partial_use_with_warning or another contract-appropriate non-success quality status
- verify fully enriched rows remain valid_for_reports
- verify source_system=ozon and provider-scoped IDs remain preserved
- verify focused and full unit tests pass
```

## SCOPE_OUT

```text
- do not modify implementation
- do not inspect parser_ozon or wb-parser-v1
- do not run live scraping
- do not read cookies, secrets, raw Ozon outputs, HAR files, or browser profiles
- do not commit or push
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_AUDIT_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-docs/03_tasks/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-runtime/agent-results/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
```

## INPUTS

```text
- developer correction RESULT
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
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
- /home/pavel/projects/parser_ozon/*
- /home/pavel/projects/wb-parser-v1/*
```

## ACCEPTANCE_CRITERIA

```text
- correction scope is limited to market-parser-v2/*
- missing/blocked seller rows are not valid_for_reports in provider/common/export products
- fully enriched rows remain valid_for_reports
- focused and full tests pass
- no forbidden source or secret/raw artifact access is used
```

## EVIDENCE_REQUIREMENTS

```text
- CHANGED_FILES_SCOPE_STATUS
- REPOSITORY_IDENTITY_STATUS
- CORRECTION_EVIDENCE_STATUS
- TEST_STATUS
- SECRET_EXPOSURE_STATUS
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
project-runtime/agent-results/TASK_AUDIT_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
```

## RISK_REQUIREMENTS

```text
- audit must ensure fully enriched rows are not degraded
```

## MANDATORY_WORKFLOW

```text
auditor(pass) -> auditor
auditor(fail) -> orchestrator
auditor(blocked) -> orchestrator
auditor(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
auditor
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
On pass, return to the main Ozon provider migration audit/test flow.
```
