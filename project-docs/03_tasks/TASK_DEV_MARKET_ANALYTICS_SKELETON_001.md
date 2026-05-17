# TASK PACKET

## TASK_ID

```text
TASK_DEV_MARKET_ANALYTICS_SKELETON_001
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
Create market-analytics skeleton
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
Create the clean analytics application skeleton around parser export bundle import and run registry boundaries.
```

## SOURCE_OF_TRUTH

```text
- project-docs/01_architecture/ARCH_MARKET_ANALYTICS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
```

## SCOPE_IN

```text
- create new clean analytics project skeleton if it does not already exist
- create backend/API skeleton
- create import worker/scheduler placeholder
- create imported run registry placeholder
- create manifest and checksum validation skeleton
- create provider-aware data model placeholders preserving marketplace/source_system/run_id
- create basic auth placeholder
- create web UI skeleton for overview route only
- create tests skeleton with synthetic bundles only
```

## SCOPE_OUT

```text
- do not scrape WB/Ozon
- do not read parser internal folders as production integration
- do not implement full dashboards
- do not implement Excel export beyond placeholder wiring unless trivial
- do not define score formulas
- do not implement own-store, product matching, or Decision Layer
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/DEVELOPER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
- project-docs/01_architecture/ARCH_MARKET_ANALYTICS_001.md
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
- analytics skeleton files
- synthetic import validation tests or placeholders appropriate to selected stack
- developer RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- market-analytics/*
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
- analytics skeleton is separate from parser skeleton
- importer boundary is export bundle based
- manifest/checksum validation skeleton exists
- run registry placeholders preserve run_id, marketplace, and source_system
- auth placeholder exists for web/API surfaces
- tests do not require real parser output or secrets
- developer RESULT lists changed files and commands
```

## EVIDENCE_REQUIREMENTS

```text
- file list for skeleton
- command results for lint/test/init checks if available
- confirmation that analytics does not scrape marketplaces
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
project-runtime/agent-results/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
```

## RISK_REQUIREMENTS

```text
- stack-specific skeleton tests may be limited if no project tooling exists yet
- full analytics implementation waits for accepted provider contracts and importer behavior
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
Full analytics implementation waits for accepted provider contracts and importer behavior.
```
