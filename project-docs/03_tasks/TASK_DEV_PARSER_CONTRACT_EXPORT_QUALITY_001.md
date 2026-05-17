# TASK PACKET

## TASK_ID

```text
TASK_DEV_PARSER_CONTRACT_EXPORT_QUALITY_001
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
NONE
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
Implement parser contract export and quality enforcement
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
OVERRIDE_REASON: Provider-aware schema, export, data-quality, and security boundaries are cross-cutting parser contracts.
```

## DEPENDENCIES

```text
- TASK_DEV_MARKET_PARSER_V2_SKELETON_001 audit pass
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
Implement common parser schema, export, data-quality, and forbidden-artifact enforcement needed before provider migration completion.
```

## SOURCE_OF_TRUTH

```text
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
```

## SCOPE_IN

```text
- implement V2 common mart schema definitions for queries, products, sellers, and seller-query-product bridge
- implement provider identity validation for wb and ozon
- implement schema_version validation and unsupported-version rejection/quarantine behavior
- implement compatibility mapping helpers for nmId/supplier_id into provider-neutral ids
- implement export manifest, bundle layout, latest pointer, and checksums enforcement
- implement forbidden bundle content detection for cookies, tokens, HAR, browser profiles, raw sensitive fragments, and logs
- implement data-quality status mapping and summaries for run/component/row/export levels
- add synthetic tests or fixtures that do not require live marketplace access or secrets
```

## SCOPE_OUT

```text
- do not migrate WB provider collection logic
- do not migrate Ozon provider collection logic
- do not inspect or modify source projects
- do not run live scraping
- do not define score formulas or owner thresholds
- do not implement analytics UI
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/DEVELOPER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_DEV_PARSER_CONTRACT_EXPORT_QUALITY_001.md
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
NONE
```

## READ_INPUTS

```text
NONE
```

## EXPECTED_OUTPUTS

```text
- parser contract/export/data-quality implementation in market-parser-v2
- synthetic tests or fixtures
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
- common schemas include marketplace, source_system, run_id, schema_version, and data_quality_status where required
- provider identities other than wb and ozon are rejected or quarantined
- compatibility mapping cannot join WB/Ozon ids without provider context
- export manifest and checksums are generated and validated
- forbidden artifacts are excluded from export bundles
- partial/failure status is preserved in data-quality summaries
- tests do not require live scraping or secrets
```

## EVIDENCE_REQUIREMENTS

```text
- changed file list
- test command results or explicit limitation
- export validation evidence using synthetic data
- forbidden artifact check evidence
- confirmation that source projects were not read or modified
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
project-runtime/agent-results/TASK_DEV_PARSER_CONTRACT_EXPORT_QUALITY_001.md
```

## RISK_REQUIREMENTS

```text
- skeleton implementation may require adapting paths to the selected stack
- exact provider collection behavior remains out of scope for this common task
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
Provider migration tasks should depend on this task passing audit/testing.
```

