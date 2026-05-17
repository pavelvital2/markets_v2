# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001
ACTION_TYPE: create_agent
TARGET_ROLE: technical_writer
TASK_ID: TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001
TASK_PACKET: project-docs/03_tasks/TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
DEPENDENCY_STATUS: ready
BLOCKED_BY: NONE
ACTION_SEMANTIC: normal
WORKSPACE_IDENTITY_REQUIRED: yes
REPOSITORY_LOCK_REQUIRED: yes
CHECKPOINT_POLICY: forbidden
CHECKPOINT_PREFLIGHT_REQUIRED: no
CHECKPOINT_RECEIPT_REQUIRED: no
CHECKPOINT_RECEIPT_REF: project-runtime/checkpoints/CHECKPOINT_ELIGIBILITY_TASK_AGGREGATE_MARKET_ANALYTICS_SKELETON_CHECKPOINT_001_1.md
REQUESTER_RETURN_CONTEXT: NONE
BLOCKING_OR_RESUME_CONTEXT:
NONE
REQUIRED_UNIVERSAL_DOCS:
- agent-system/01_roles/TECHNICAL_WRITER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
REQUIRED_PROJECT_DOCS:
- project-docs/03_tasks/TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
- project-docs/02_stages/STAGE_PLAN_001.md
- project-runtime/agent-results/TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001.md
EXPECTED_RESULT:
- technical writer RESULT according to AGENT_RESULT_TEMPLATE
INSTRUCTION_FOR_ORCHESTRATOR: Dispatch exactly one technical_writer task with reasoning_effort high.
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
- agent-system/01_roles/TECHNICAL_WRITER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
```

## REQUIRED_PROJECT_DOCS

```text
- project-docs/03_tasks/TASK_DOC_MARKET_ANALYTICS_SKELETON_HANDOFF_001.md
- project-docs/02_stages/STAGE_PLAN_001.md
- project-runtime/agent-results/TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001.md
```

## EXPECTED_RESULT

```text
- technical writer RESULT according to AGENT_RESULT_TEMPLATE
```

## Instruction for orchestrator

```text
Dispatch exactly one technical_writer task with reasoning_effort high.
```
