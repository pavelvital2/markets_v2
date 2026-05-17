# TASK PACKET

## TASK_ID

```text
TASK_DEV_MARKET_PARSER_V2_SKELETON_001
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
Create market-parser-v2 skeleton
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
OVERRIDE_REASON: NONE
```

## DEPENDENCIES

```text
- TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001 pass
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
TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001
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
Create the clean parser skeleton for market-parser-v2 without migrating provider logic from source projects.
```

## SOURCE_OF_TRUTH

```text
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
```

## SCOPE_IN

```text
- create new clean parser project skeleton if it does not already exist
- create common core package/module layout
- create provider abstraction for wb, ozon, all
- create config boundary for data/log/secret paths
- create run_id and schema_version placeholders
- create contract validation skeleton
- create export bundle layout skeleton
- create CLI/API skeleton without live scraping
- create tests skeleton using synthetic sanitized fixtures only
```

## SCOPE_OUT

```text
- do not inspect or modify source projects
- do not migrate WB provider logic
- do not migrate Ozon provider logic
- do not run live scraping
- do not require real cookies
- do not implement analytics UI
- do not implement Decision Layer formulas
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/DEVELOPER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
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
- parser skeleton files
- synthetic tests or test placeholders appropriate to selected stack
- developer RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- market-parser-v2/*
- project-docs/05_testing/*
```

## FORBIDDEN_FILE_CHANGES

```text
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
- agent-system/*
- project-input/*
- project-runtime/*
- .git/*
- secrets/*
- credentials/*
- cookies/*
```

## ACCEPTANCE_CRITERIA

```text
- skeleton has separate common core and provider boundary
- provider registry can represent wb, ozon, and all without live network access
- no source provider logic is copied or migrated
- config supports separate code, data, logs, secrets/cookies, raw archives, and temp paths
- contract validation skeleton references schema_version and provider identity
- export skeleton models latest.json, manifest.json, bundle.tar.gz, and checksums.sha256
- tests do not require live marketplace access or secrets
- developer RESULT lists changed files and commands
```

## EVIDENCE_REQUIREMENTS

```text
- file list for skeleton
- command results for lint/test/init checks if available
- confirmation that no source projects were modified
- confirmation that no secrets/cookies were created or logged
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
project-runtime/agent-results/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
```

## RISK_REQUIREMENTS

```text
- stack-specific skeleton tests may be limited if no project tooling exists yet
- source provider behavior is intentionally excluded until audited source-contract research is accepted
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
This task is a skeleton task only. Provider migration waits for audited source-contract research and design continuation.
```
