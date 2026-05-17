# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_DEV_WB_PROVIDER_MIGRATION_001
ACTION_TYPE: create_agent
TARGET_ROLE: developer
TASK_ID: TASK_DEV_WB_PROVIDER_MIGRATION_001
TASK_PACKET: project-docs/03_tasks/TASK_DEV_WB_PROVIDER_MIGRATION_001.md
DEPENDENCY_STATUS: ready
BLOCKED_BY: NONE
ACTION_SEMANTIC: normal
WORKSPACE_IDENTITY_REQUIRED: yes
REPOSITORY_LOCK_REQUIRED: yes
CHECKPOINT_POLICY: forbidden
CHECKPOINT_PREFLIGHT_REQUIRED: no
CHECKPOINT_RECEIPT_REQUIRED: no
CHECKPOINT_RECEIPT_REF: project-runtime/checkpoints/CHECKPOINT_ELIGIBILITY_TASK_AGGREGATE_PARSER_CONTRACT_EXPORT_QUALITY_CHECKPOINT_001_1.md
REQUESTER_RETURN_CONTEXT: NONE
BLOCKING_OR_RESUME_CONTEXT:
NONE
REQUIRED_UNIVERSAL_DOCS:
- agent-system/01_roles/DEVELOPER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
REQUIRED_PROJECT_DOCS:
- project-docs/03_tasks/TASK_DEV_WB_PROVIDER_MIGRATION_001.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
EXPECTED_RESULT:
- developer RESULT according to AGENT_RESULT_TEMPLATE
INSTRUCTION_FOR_ORCHESTRATOR: Dispatch exactly one developer task with reasoning_effort high.
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
- agent-system/01_roles/DEVELOPER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
```

## REQUIRED_PROJECT_DOCS

```text
- project-docs/03_tasks/TASK_DEV_WB_PROVIDER_MIGRATION_001.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
```

## EXPECTED_RESULT

```text
- developer RESULT according to AGENT_RESULT_TEMPLATE
```

## Instruction for orchestrator

```text
Dispatch exactly one developer task with reasoning_effort high.
```
