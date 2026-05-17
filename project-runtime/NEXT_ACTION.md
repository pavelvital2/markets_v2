# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_BOOTSTRAP_DESIGNER_001
ACTION_TYPE: create_agent
TARGET_ROLE: designer
TASK_ID: TASK_BOOTSTRAP_DESIGNER_001
TASK_PACKET: project-runtime/bootstrap/TASK_BOOTSTRAP_DESIGNER_001.md
DEPENDENCY_STATUS: ready
BLOCKED_BY: NONE
ACTION_SEMANTIC: normal
WORKSPACE_IDENTITY_REQUIRED: yes
REPOSITORY_LOCK_REQUIRED: yes
CHECKPOINT_POLICY: forbidden
CHECKPOINT_PREFLIGHT_REQUIRED: no
CHECKPOINT_RECEIPT_REQUIRED: no
CHECKPOINT_RECEIPT_REF: NONE
REQUESTER_RETURN_CONTEXT: NONE
BLOCKING_OR_RESUME_CONTEXT:
NONE
REQUIRED_UNIVERSAL_DOCS:
- agent-system/01_roles/DESIGNER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/07_lifecycle/BOOTSTRAP_STAGE.md
REQUIRED_PROJECT_DOCS:
- project-input/TZ.md
EXPECTED_RESULT:
- RESULT according to agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
INSTRUCTION_FOR_ORCHESTRATOR: Dispatch exactly one designer bootstrap task.
```

## Requester return context

```text
NONE
```

## Blocking or resume context

```text
NONE
```

## REQUIRED_UNIVERSAL_DOCS

```text
- agent-system/01_roles/DESIGNER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/07_lifecycle/BOOTSTRAP_STAGE.md
```

## REQUIRED_PROJECT_DOCS

```text
- project-input/TZ.md
```

## EXPECTED_RESULT

```text
- RESULT according to agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
```

## Instruction for orchestrator

```text
Dispatch exactly one designer bootstrap task.
```
