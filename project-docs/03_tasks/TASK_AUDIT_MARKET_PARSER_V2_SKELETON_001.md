# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_MARKET_PARSER_V2_SKELETON_001
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
project-runtime/agent-results/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
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
Audit market-parser-v2 skeleton
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
OVERRIDE_REASON: Audit covers skeleton boundaries, source-project isolation, provider registry, config separation, export skeleton, and test evidence.
```

## DEPENDENCIES

```text
- TASK_DEV_MARKET_PARSER_V2_SKELETON_001 returned pass or fail
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
TASK_DEV_MARKET_PARSER_V2_SKELETON_001
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
- skeleton boundary evidence
- provider registry/config/export evidence
- source-project isolation check
- security/secret exposure check
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
Audit the clean market-parser-v2 skeleton before it can become an accepted implementation baseline for downstream parser contract and provider migration tasks.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/04_audits/AUDIT_GATES_001.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
```

## SCOPE_IN

```text
- verify developer changed only allowed files
- verify source projects were not read or modified
- verify skeleton respects parser/analytics boundary
- verify common core and provider boundary exist
- verify provider registry can represent wb, ozon, and all without live network access
- verify config/secrets/data/log/raw/temp path separation exists
- verify run_id and schema_version placeholders exist
- verify contract validation and export bundle skeleton exist
- verify CLI/API skeleton does not run live scraping
- verify synthetic tests or limitations are reported
```

## SCOPE_OUT

```text
- do not modify implementation
- do not run live scraping
- do not inspect source projects directly
- do not migrate WB or Ozon provider logic
- do not commit or push
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_AUDIT_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/04_audits/AUDIT_GATES_001.md
- project-runtime/agent-results/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
```

## INPUTS

```text
- developer RESULT for TASK_DEV_MARKET_PARSER_V2_SKELETON_001
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- market-parser-v2/*
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
- skeleton satisfies Gate C in AUDIT_GATES_001
- skeleton satisfies TASK_DEV_MARKET_PARSER_V2_SKELETON_001 acceptance criteria
- forbidden path and secret checks pass
- tests are sufficient for synthetic skeleton behavior or limitations are explicit
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
- TEST_STATUS
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
project-runtime/agent-results/TASK_AUDIT_MARKET_PARSER_V2_SKELETON_001.md
```

## RISK_REQUIREMENTS

```text
- skeleton tests may pass while provider-specific behavior remains intentionally unimplemented
```

## MANDATORY_WORKFLOW

```text
auditor(pass) -> orchestrator
auditor(fail) -> orchestrator
auditor(blocked) -> orchestrator
auditor(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
orchestrator
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
On audit pass, orchestrator must checkpoint the accepted skeleton implementation before downstream contract/export/provider tasks.
```
