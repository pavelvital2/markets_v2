# TASK PACKET

## TASK_ID

```text
TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001
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
TASK_AUDIT_BOOTSTRAP_DESIGNER_001
```

## SOURCE_RESULT_REF

```text
project-runtime/agent-results/TASK_AUDIT_BOOTSTRAP_DESIGNER_001.md
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
Correct downstream task packet governance sections
```

## TASK_TYPE

```text
designer
```

## TARGET_ROLE

```text
designer
```

## REASONING_LEVEL

```text
VALUE: maximum
OVERRIDE_REASON: NONE
```

## DEPENDENCIES

```text
- TASK_AUDIT_BOOTSTRAP_DESIGNER_001 returned fail
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
TASK_AUDIT_BOOTSTRAP_DESIGNER_001
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
- validator passes for corrected downstream task packets
```

## EXPECTED_OUTPUT

```text
- corrected downstream task packets
- RESULT according to AGENT_RESULT_TEMPLATE
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
Correct only the governance-schema omissions identified by the audit failure in the two downstream designer task packets.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
- project-runtime/agent-results/TASK_AUDIT_BOOTSTRAP_DESIGNER_001.md
- agent-system/03_templates/TASK_PACKET_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
```

## SCOPE_IN

```text
- add missing FILESYSTEM_GOVERNANCE section to project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- add missing RUNTIME_GOVERNANCE section to project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- add missing FILESYSTEM_GOVERNANCE section to project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- add missing RUNTIME_GOVERNANCE section to project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- preserve task intent and avoid unrelated design changes
```

## SCOPE_OUT

```text
- do not change architecture intake content
- do not create new project task packets
- do not edit agent-system, project-runtime, project-input, or Git metadata
- do not dispatch agents
- do not commit or push
```

## REQUIRED_DOCS

```text
- project-docs/03_tasks/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
- project-runtime/agent-results/TASK_AUDIT_BOOTSTRAP_DESIGNER_001.md
- agent-system/01_roles/DESIGNER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/TASK_PACKET_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## INPUTS

```text
- audit fail result
- two invalid downstream task packets
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
```

## EXPECTED_OUTPUTS

```text
- corrected project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- corrected project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-runtime/*
- project-input/*
- project-archive/*
- .git/*
- .env
- secrets/*
- credentials/*
- project-docs/01_architecture/*
- project-docs/03_tasks/TASK_AUDIT_BOOTSTRAP_DESIGNER_001.md
- project-docs/03_tasks/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
```

## ACCEPTANCE_CRITERIA

```text
- both corrected downstream task packets contain FILESYSTEM_GOVERNANCE and RUNTIME_GOVERNANCE sections
- both corrected downstream task packets pass validate_task_packet.py
- no unrelated files are changed
- RESULT reports changed files and validator evidence
```

## EVIDENCE_REQUIREMENTS

```text
- validator command and result for each corrected task packet
- changed file list
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
project-runtime/agent-results/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md
```

## RISK_REQUIREMENTS

```text
- correction could unintentionally alter task intent
```

## MANDATORY_WORKFLOW

```text
designer(pass) -> auditor
designer(fail) -> orchestrator
designer(blocked) -> orchestrator
designer(gap) -> orchestrator
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
This correction is limited to schema/governance sections missing from two downstream task packets.
```
