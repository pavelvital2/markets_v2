# TASK PACKET

## TASK_ID

```text
TASK_BOOTSTRAP_DESIGNER_001
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
1
```

## FAILURE_TYPE

```text
none
```

## TASK_TITLE

```text
Bootstrap intake for design
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
- bootstrap validation passed
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
NONE
```

## REQUESTED_BY_TASK

```text
NONE
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
Give the first profile agent one bounded bootstrap intake task using the owner
source input and universal package governance.
```

## SOURCE_OF_TRUTH

```text
- project-input/TZ.md
- agent-system/07_lifecycle/BOOTSTRAP_STAGE.md
```

## REQUIRED_DOCS

```text
- project-input/TZ.md
- agent-system/01_roles/DESIGNER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/07_lifecycle/BOOTSTRAP_STAGE.md
```

## INPUTS

```text
- owner-provided source input
- current runtime state
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
```

## SCOPE_IN

```text
- read only the REQUIRED_DOCS and READ_INPUTS listed in this packet;
- perform the first bounded intake task for the assigned role;
- return RESULT using AGENT_RESULT_TEMPLATE;
- identify gaps or blockers instead of resolving ambiguity by assumption.
```

## SCOPE_OUT

```text
- do not edit bootstrap task packets;
- do not edit project-runtime files;
- do not edit agent-system files;
- do not perform audit, Git checkpoint, deployment, or final acceptance;
- do not expand scope beyond first intake for the assigned role.
```

## EXPECTED_OUTPUTS

```text
- RESULT according to agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- BOOTSTRAP_CONTINUATION_STATUS: downstream_task_packet | gap | blocked | wait_for_owner
- BOOTSTRAP_CONTINUATION_REF: path or route reference
```

## ALLOWED_FILE_CHANGES

```text
- project-docs/01_architecture/*
- project-docs/03_tasks/*
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-runtime/*
- project-archive/*
- project-input/*
- .git/*
- .env
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- RESULT uses agent-system/03_templates/AGENT_RESULT_TEMPLATE.md;
- changed files, if any, are within ALLOWED_FILE_CHANGES;
- gaps or blockers are reported instead of guessed;
- bootstrap output cannot be accepted unless it contains a valid downstream
  dispatchable TASK_PACKET, explicit GAP, explicit BLOCKED route, or explicit
  wait_for_owner route;
- when research or design continuation is needed, the designer must create a
  full schema-valid downstream research/design continuation task packet or
  return GAP/BLOCKED/wait_for_owner;
- no forbidden file changes are made;
- no profile agent commits or pushes.
```

## EVIDENCE_REQUIREMENTS

```text
- list read documents;
- list changed files or NONE;
- provide scope and forbidden-change verification.
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
project-runtime/agent-results/TASK_BOOTSTRAP_DESIGNER_001.md
```

## RISK_REQUIREMENTS

```text
- incomplete owner input;
- ambiguous requirements;
- insufficient design readiness.
```

## MANDATORY_WORKFLOW

```text
designer(pass) -> auditor
blocked -> orchestrator
gap -> orchestrator
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
optional
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
Created by orchestrator during bootstrap. This packet is for bootstrap intake
only and must not introduce project-specific implementation terms into
universal package governance.
```
