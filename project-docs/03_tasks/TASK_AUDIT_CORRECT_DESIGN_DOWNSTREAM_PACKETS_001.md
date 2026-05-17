# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001
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
project-runtime/agent-results/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
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
Audit correction of downstream task packets
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
OVERRIDE_REASON: NONE
```

## DEPENDENCIES

```text
- TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001 result is available
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
designer
```

## REQUESTED_BY_TASK

```text
TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001
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
- corrected task packet schema validation
- correction changed-file scope check
```

## EXPECTED_OUTPUT

```text
- audit RESULT according to AGENT_RESULT_TEMPLATE
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
Independently audit the correction that made the two downstream task packets schema-valid.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_AUDIT_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
- project-docs/03_tasks/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
- project-runtime/agent-results/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
```

## SCOPE_IN

```text
- audit correction RESULT against TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001
- validate project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- validate project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- verify correction changed only allowed files
```

## SCOPE_OUT

```text
- do not fix files
- do not edit project docs
- do not edit project-runtime files
- do not commit or push
```

## REQUIRED_DOCS

```text
- project-docs/03_tasks/TASK_AUDIT_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
- project-docs/03_tasks/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
- project-runtime/agent-results/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## INPUTS

```text
- correction RESULT
- corrected downstream task packets
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
```

## EXPECTED_OUTPUTS

```text
- RESULT according to agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- mandatory audit evidence statuses from AUDITOR.md
- VALIDATED_TASK_PACKETS list for corrected TASK_*.md files
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
- .git/*
- .env
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- auditor returns pass, fail, blocked, or gap
- auditor includes mandatory audit evidence statuses
- auditor validates both corrected downstream task packets
- auditor makes no file changes
```

## EVIDENCE_REQUIREMENTS

```text
- validation commands and results
- changed file scope status
- forbidden path verification
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
project-runtime/agent-results/TASK_AUDIT_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
```

## RISK_REQUIREMENTS

```text
- correction may have altered task intent while fixing schema
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
Audit-only task; do not correct checked files.
```
