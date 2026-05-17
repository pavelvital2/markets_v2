# TASK PACKET

## TASK_ID

```text
TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
correction
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
TASK_DEV_OZON_PROVIDER_MIGRATION_001
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
audit
```

## TASK_TITLE

```text
Correct Ozon missing seller quality propagation
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
VALUE: maximum
OVERRIDE_REASON: Correction touches Ozon provider quality semantics, common mart validity, export behavior, and audit-blocking partial/failure status propagation.
```

## DEPENDENCIES

```text
- TASK_AUDIT_OZON_PROVIDER_MIGRATION_001 returned fail
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
auditor
```

## REQUESTED_BY_TASK

```text
TASK_AUDIT_OZON_PROVIDER_MIGRATION_001
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
- row-level missing seller quality propagation evidence
- focused test evidence
- full market-parser-v2 unittest evidence
- no secret/raw artifact exposure evidence
```

## EXPECTED_OUTPUT

```text
- developer correction RESULT according to AGENT_RESULT_TEMPLATE
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
Correct the audit-blocking Ozon defect where missing or blocked seller enrichment does not propagate partial/failure quality to affected product rows and common mart rows.
```

## SOURCE_OF_TRUTH

```text
- project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
- project-docs/03_tasks/TASK_DEV_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
```

## SCOPE_IN

```text
- update Ozon provider logic so missing or blocked seller enrichment downgrades affected product rows and common mart rows from valid_for_reports to partial or another contract-appropriate non-success quality status
- preserve source_system=ozon and provider-scoped nmId/supplier mappings
- add or update focused tests proving product/common mart row quality degrades when external_seller_id is missing after enrichment
- keep export bundle free of raw/cookie/HAR/browser-profile artifacts
- run focused Ozon tests and full market-parser-v2 unit tests
```

## SCOPE_OUT

```text
- do not inspect parser_ozon source project
- do not inspect wb-parser-v1 source project
- do not run live scraping
- do not read cookies, secrets, raw Ozon outputs, HAR files, or browser profiles
- do not commit or push
- do not dispatch downstream
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/DEVELOPER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
```

## INPUTS

```text
- audit fail result for TASK_AUDIT_OZON_PROVIDER_MIGRATION_001
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_AUDIT_OZON_PROVIDER_MIGRATION_001.md
```

## EXPECTED_OUTPUTS

```text
- corrected implementation
- focused tests
- developer RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- market-parser-v2/*
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
- data/*
- logs/*
- cookies/*
- browser-profile/*
- node_modules/*
- /home/pavel/projects/parser_ozon/*
- /home/pavel/projects/wb-parser-v1/*
```

## ACCEPTANCE_CRITERIA

```text
- missing or blocked seller enrichment degrades affected product/common mart row quality from valid_for_reports
- focused tests fail on the prior behavior and pass after correction
- full market-parser-v2 unittest suite passes
- no forbidden source project, cookie, secret, raw output, HAR, or browser-profile access is used
```

## EVIDENCE_REQUIREMENTS

```text
- focused test command output
- full unittest command output
- changed-file scope
- explicit no-source/no-secret/no-live-scraping confirmation
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
project-runtime/agent-results/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
```

## RISK_REQUIREMENTS

```text
- quality downgrade must not break valid fully enriched Ozon rows
```

## MANDATORY_WORKFLOW

```text
developer(pass) -> auditor
developer(fail) -> orchestrator
developer(blocked) -> orchestrator
developer(gap) -> orchestrator
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
This correction is limited to current market-parser-v2 implementation and tests; no source-project reread is required.
```
