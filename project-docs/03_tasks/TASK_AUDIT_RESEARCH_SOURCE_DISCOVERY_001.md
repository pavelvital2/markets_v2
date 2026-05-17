# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001
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
project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
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
Audit source discovery research result
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
OVERRIDE_REASON: Research result controls design continuation evidence.
```

## DEPENDENCIES

```text
- TASK_RESEARCH_SOURCE_DISCOVERY_001 returned pass
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
requirements_analyst
```

## REQUESTED_BY_TASK

```text
TASK_RESEARCH_SOURCE_DISCOVERY_001
```

## RESEARCH_QUESTION_ID

```text
RQ_SOURCE_DISCOVERY_001
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
- bounded source compliance
- research result template compliance
- secret exposure check
- changed file scope check
```

## EXPECTED_OUTPUT

```text
- audit RESULT according to AGENT_RESULT_TEMPLATE
```

## RETURN_TO_REQUESTER_AFTER_AUDIT_PASS

```text
yes
```

## RETURN_TO_ROLE_AFTER_AUDIT_PASS

```text
designer
```

## RETURN_TASK_AFTER_AUDIT_PASS

```text
project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## PURPOSE

```text
Independently audit the bounded source discovery research result before design continuation may use it.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/07_reports/TASK_RESEARCH_SOURCE_DISCOVERY_001_RESULT.md
```

## SCOPE_IN

```text
- audit research RESULT against TASK_RESEARCH_SOURCE_DISCOVERY_001
- verify bounded source compliance and forbidden-source avoidance
- verify research result fields and evidence matrix
- verify no secret values were copied
- verify changed files are within ALLOWED_FILE_CHANGES
```

## SCOPE_OUT

```text
- do not correct research output
- do not expand research
- do not read forbidden source files
- do not edit files
- do not commit or push
```

## REQUIRED_DOCS

```text
- project-docs/03_tasks/TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/07_reports/TASK_RESEARCH_SOURCE_DISCOVERY_001_RESULT.md
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
```

## INPUTS

```text
- research RESULT
- research report artifact
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
```

## EXPECTED_OUTPUTS

```text
- RESULT according to AGENT_RESULT_TEMPLATE
- mandatory audit evidence statuses from AUDITOR.md
- research compliance decision
```

## ALLOWED_FILE_CHANGES

```text
NONE
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-runtime/*
- project-docs/*
- project-input/*
- project-archive/*
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
- .git/*
- .env
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- auditor returns pass, fail, blocked, or gap
- auditor includes mandatory audit evidence statuses
- auditor verifies research result does not use forbidden sources or copy secret values
- auditor makes no file changes
```

## EVIDENCE_REQUIREMENTS

```text
- list read documents
- list checks performed
- include CHANGED_FILES_SCOPE_STATUS, SECRET_EXPOSURE_STATUS, EVIDENCE_STATUS, and REASONING_LEVEL_COMPLIANCE
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
project-runtime/agent-results/TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001.md
```

## RISK_REQUIREMENTS

```text
- research may have copied unsupported facts from non-allowed sources
- research may require source-specific caveats before design continuation
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
none
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
Research output must not influence design continuation until this audit returns pass.
```
