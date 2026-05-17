# TASK PACKET

## TASK_ID

```text
TASK_CORRECT_DOC_MARKET_ANALYTICS_AUTH_ENV_001
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
TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001
```

## SOURCE_RESULT_REF

```text
project-runtime/agent-results/TASK_AUDIT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
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
Correct market analytics README auth env name
```

## TASK_TYPE

```text
technical_writer
```

## TARGET_ROLE

```text
technical_writer
```

## REASONING_LEVEL

```text
VALUE: high
OVERRIDE_REASON: Correction must align README setup docs with implementation and avoid secret-scan triggering auth wording.
```

## DEPENDENCIES

```text
- TASK_AUDIT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001 returned fail
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
TASK_AUDIT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001
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
- README auth env var corrected to implementation name
- no secret/cookie/source-project access
```

## EXPECTED_OUTPUT

```text
- technical writer correction RESULT according to AGENT_RESULT_TEMPLATE
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
Correct README auth environment variable naming to match the accepted market analytics implementation.
```

## SOURCE_OF_TRUTH

```text
- project-runtime/agent-results/TASK_AUDIT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
- market-analytics/README.md
- market-analytics/src/market_analytics/config.py
```

## SCOPE_IN

```text
- replace MARKET_ANALYTICS_BASIC_AUTH_PASSWORD with MARKET_ANALYTICS_BASIC_AUTH_SECRET in README
- avoid password wording that conflicts with implementation
- preserve setup/test commands, FastAPI prerequisite, parser export-bundle boundary, and Stage 9 limitation
```

## SCOPE_OUT

```text
- do not edit code
- do not inspect source projects
- do not read cookies or secrets
- do not commit or push
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/TECHNICAL_WRITER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_CORRECT_DOC_MARKET_ANALYTICS_AUTH_ENV_001.md
- project-runtime/agent-results/TASK_AUDIT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
```

## INPUTS

```text
- documentation audit fail result
```

## READ_INPUTS

```text
- market-analytics/README.md
- market-analytics/src/market_analytics/config.py
```

## EXPECTED_OUTPUTS

```text
- corrected README
- technical writer correction RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- market-analytics/README.md
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-input/*
- project-runtime/*
- project-docs/*
- .git/*
- secrets/*
- credentials/*
- cookies/*
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
```

## ACCEPTANCE_CRITERIA

```text
- README auth env var matches market-analytics/src/market_analytics/config.py
- README contains no secret values
- README does not overstate current skeleton scope
```

## EVIDENCE_REQUIREMENTS

```text
- changed-file scope
- auth env consistency check
- no-secret/no-source confirmation
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
project-runtime/agent-results/TASK_CORRECT_DOC_MARKET_ANALYTICS_AUTH_ENV_001.md
```

## RISK_REQUIREMENTS

```text
- correction must not reintroduce checkpoint secret-scan content patterns
```

## MANDATORY_WORKFLOW

```text
technical_writer(pass) -> auditor
technical_writer(fail) -> auditor
technical_writer(blocked) -> orchestrator
technical_writer(gap) -> orchestrator
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
mandatory
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
This correction is limited to README wording.
```
