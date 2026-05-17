# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_RESEARCH_SOURCE_DISCOVERY_001
ACTION_TYPE: create_agent
TARGET_ROLE: requirements_analyst
TASK_ID: TASK_RESEARCH_SOURCE_DISCOVERY_001
TASK_PACKET: project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
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
- agent-system/01_roles/REQUIREMENTS_ANALYST.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
REQUIRED_PROJECT_DOCS:
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
EXPECTED_RESULT:
- research RESULT according to AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE
INSTRUCTION_FOR_ORCHESTRATOR: Dispatch exactly one requirements_analyst research dependency task with reasoning_effort xhigh.
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
- agent-system/01_roles/REQUIREMENTS_ANALYST.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
```

## REQUIRED_PROJECT_DOCS

```text
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
```

## EXPECTED_RESULT

```text
- research RESULT according to AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE
```

## Instruction for orchestrator

```text
Dispatch exactly one requirements_analyst research dependency task with reasoning_effort xhigh.
```
