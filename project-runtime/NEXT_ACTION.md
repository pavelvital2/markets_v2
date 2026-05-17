# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_SOURCE_CONTRACT_DESIGN_CHECKPOINT_001
ACTION_TYPE: checkpoint
TARGET_ROLE: orchestrator
TASK_ID: TASK_AGGREGATE_SOURCE_CONTRACT_DESIGN_CHECKPOINT_001
TASK_PACKET: project-docs/03_tasks/TASK_AGGREGATE_SOURCE_CONTRACT_DESIGN_CHECKPOINT_001.md
DEPENDENCY_STATUS: ready
BLOCKED_BY: NONE
ACTION_SEMANTIC: normal
WORKSPACE_IDENTITY_REQUIRED: yes
REPOSITORY_LOCK_REQUIRED: yes
CHECKPOINT_POLICY: local_only
CHECKPOINT_PREFLIGHT_REQUIRED: yes
CHECKPOINT_RECEIPT_REQUIRED: yes
CHECKPOINT_RECEIPT_REF: NONE
REQUESTER_RETURN_CONTEXT: NONE
BLOCKING_OR_RESUME_CONTEXT:
NONE
REQUIRED_UNIVERSAL_DOCS:
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
- agent-system/09_validators/SECRET_SCAN_RULES.md
- agent-system/09_validators/GIT_CHECKPOINT_VALIDATION_RULES.md
REQUIRED_PROJECT_DOCS:
- project-docs/03_tasks/TASK_AGGREGATE_SOURCE_CONTRACT_DESIGN_CHECKPOINT_001.md
- project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
EXPECTED_RESULT:
- checkpoint preflight receipt and local-only commit when preflight passes
INSTRUCTION_FOR_ORCHESTRATOR: Run checkpoint_preflight with include-untracked and push-requested no, then commit locally if it passes.
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
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
- agent-system/09_validators/SECRET_SCAN_RULES.md
- agent-system/09_validators/GIT_CHECKPOINT_VALIDATION_RULES.md
```

## REQUIRED_PROJECT_DOCS

```text
- project-docs/03_tasks/TASK_AGGREGATE_SOURCE_CONTRACT_DESIGN_CHECKPOINT_001.md
- project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
```

## EXPECTED_RESULT

```text
- checkpoint preflight receipt and local-only commit when preflight passes
```

## Instruction for orchestrator

```text
Run checkpoint_preflight with include-untracked and push-requested no, then commit locally if it passes.
```
