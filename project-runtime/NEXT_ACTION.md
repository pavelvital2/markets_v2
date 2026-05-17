# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001
ACTION_TYPE: create_agent
TARGET_ROLE: designer
TASK_ID: TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001
TASK_PACKET: project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
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
- agent-system/03_templates/TASK_PACKET_TEMPLATE.md
- agent-system/03_templates/TASK_PROPOSAL_TEMPLATE.md
REQUIRED_PROJECT_DOCS:
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
EXPECTED_RESULT:
- design continuation RESULT according to AGENT_RESULT_TEMPLATE
INSTRUCTION_FOR_ORCHESTRATOR: Dispatch exactly one designer task with reasoning_effort xhigh.
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
- agent-system/03_templates/TASK_PACKET_TEMPLATE.md
- agent-system/03_templates/TASK_PROPOSAL_TEMPLATE.md
```

## REQUIRED_PROJECT_DOCS

```text
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## EXPECTED_RESULT

```text
- design continuation RESULT according to AGENT_RESULT_TEMPLATE
```

## Instruction for orchestrator

```text
Dispatch exactly one designer task with reasoning_effort xhigh.
```
