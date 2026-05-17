# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001
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
project-runtime/agent-results/TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
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
Audit market analytics skeleton handoff docs
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
OVERRIDE_REASON: Audit checks developer-facing setup docs for correctness, no-secret wording, and scope boundaries.
```

## DEPENDENCIES

```text
- TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001 returned pass or fail
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
technical_writer
```

## REQUESTED_BY_TASK

```text
TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001
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
- README setup correctness check
- auth env var consistency check
- Stage 9 limitation check
- no-secret/no-source check
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
Audit the market analytics skeleton handoff documentation before checkpoint.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
- project-runtime/agent-results/TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
- project-runtime/agent-results/TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001.md
- market-analytics/README.md
- market-analytics/pyproject.toml
- market-analytics/src/market_analytics/config.py
```

## SCOPE_IN

```text
- verify README matches implemented auth env var names
- verify README setup/test commands are accurate for current skeleton
- verify README documents FastAPI dependency prerequisite
- verify README preserves parser export bundle boundary
- verify README does not overstate Stage 9/MVP/dashboard/formula implementation
- verify no secrets/cookies/source project paths were introduced
```

## SCOPE_OUT

```text
- do not modify documentation
- do not inspect source projects
- do not read cookies or secrets
- do not commit or push
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_AUDIT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
- project-docs/03_tasks/TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
- project-runtime/agent-results/TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
- project-runtime/agent-results/TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001.md
```

## INPUTS

```text
- technical writer RESULT
```

## READ_INPUTS

```text
- market-analytics/README.md
- market-analytics/pyproject.toml
- market-analytics/src/market_analytics/config.py
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
- README is consistent with implemented auth configuration
- README accurately describes current skeleton and setup limitations
- README does not imply live scraping, full dashboards, formulas, own-store logic, product matching, or decision layer are implemented
- README does not include secrets, cookies, or credentials
```

## EVIDENCE_REQUIREMENTS

```text
- CHANGED_FILES_SCOPE_STATUS
- DOC_ACCURACY_STATUS
- AUTH_ENV_CONSISTENCY_STATUS
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
project-runtime/agent-results/TASK_AUDIT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
```

## RISK_REQUIREMENTS

```text
- audit must catch documentation that references obsolete or unsafe auth env names
```

## MANDATORY_WORKFLOW

```text
auditor(pass) -> orchestrator
auditor(fail) -> technical_writer
auditor(blocked) -> orchestrator
auditor(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
orchestrator
```

## NEXT_ROLE_ON_FAIL

```text
technical_writer
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
On pass, route documentation handoff to checkpoint; on fail, route bounded README correction.
```
