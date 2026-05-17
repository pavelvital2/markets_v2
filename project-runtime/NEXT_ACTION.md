# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_PARSER_CONTRACT_EXPORT_QUALITY_CHECKPOINT_001
ACTION_TYPE: checkpoint
TARGET_ROLE: orchestrator
TASK_ID: TASK_AGGREGATE_PARSER_CONTRACT_EXPORT_QUALITY_CHECKPOINT_001
TASK_PACKET: project-docs/03_tasks/TASK_AGGREGATE_PARSER_CONTRACT_EXPORT_QUALITY_CHECKPOINT_001.md
DEPENDENCY_STATUS: ready
BLOCKED_BY: NONE
ACTION_SEMANTIC: normal
WORKSPACE_IDENTITY_REQUIRED: yes
REPOSITORY_LOCK_REQUIRED: yes
CHECKPOINT_POLICY: push_after_local_commit
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
- project-docs/03_tasks/TASK_AGGREGATE_PARSER_CONTRACT_EXPORT_QUALITY_CHECKPOINT_001.md
- project-runtime/agent-results/TASK_TEST_PARSER_CONTRACT_EXPORT_QUALITY_001.md
EXPECTED_RESULT:
- checkpoint preflight receipt, local commit, and push to origin main when preflight passes
INSTRUCTION_FOR_ORCHESTRATOR: Run checkpoint_preflight with include-untracked and push-requested yes, commit locally if it passes, then push origin main.
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
- project-docs/03_tasks/TASK_AGGREGATE_PARSER_CONTRACT_EXPORT_QUALITY_CHECKPOINT_001.md
- project-runtime/agent-results/TASK_TEST_PARSER_CONTRACT_EXPORT_QUALITY_001.md
```

## EXPECTED_RESULT

```text
- checkpoint preflight receipt, local commit, and push to origin main when preflight passes
```

## Instruction for orchestrator

```text
Run checkpoint_preflight with include-untracked and push-requested yes, commit locally if it passes, then push origin main.
```
