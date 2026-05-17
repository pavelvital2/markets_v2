# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_LOCAL_CHECKPOINT_COMMIT_001
ACTION_TYPE: update_state
TARGET_ROLE: orchestrator
TASK_ID: TASK_AGGREGATE_BOOTSTRAP_CHECKPOINT_001
TASK_PACKET: NONE
DEPENDENCY_STATUS: ready
BLOCKED_BY: NONE
ACTION_SEMANTIC: normal
WORKSPACE_IDENTITY_REQUIRED: yes
REPOSITORY_LOCK_REQUIRED: yes
CHECKPOINT_POLICY: local_only
CHECKPOINT_PREFLIGHT_REQUIRED: yes
CHECKPOINT_RECEIPT_REQUIRED: yes
CHECKPOINT_RECEIPT_REF: project-runtime/checkpoints/CHECKPOINT_ELIGIBILITY_TASK_AGGREGATE_BOOTSTRAP_CHECKPOINT_001_1.md
REQUESTER_RETURN_CONTEXT: NONE
BLOCKING_OR_RESUME_CONTEXT:
NONE
REQUIRED_UNIVERSAL_DOCS:
- agent-system/02_runtime/POST_AUDIT_GIT_CHECKPOINT.md
- agent-system/09_validators/GIT_CHECKPOINT_VALIDATION_RULES.md
REQUIRED_PROJECT_DOCS:
- project-runtime/checkpoints/CHECKPOINT_ELIGIBILITY_TASK_AGGREGATE_BOOTSTRAP_CHECKPOINT_001_1.md
EXPECTED_RESULT:
- local checkpoint commit
INSTRUCTION_FOR_ORCHESTRATOR: Commit accepted aggregate bootstrap checkpoint files locally; do not push.
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
- agent-system/02_runtime/POST_AUDIT_GIT_CHECKPOINT.md
- agent-system/09_validators/GIT_CHECKPOINT_VALIDATION_RULES.md
```

## REQUIRED_PROJECT_DOCS

```text
- project-runtime/checkpoints/CHECKPOINT_ELIGIBILITY_TASK_AGGREGATE_BOOTSTRAP_CHECKPOINT_001_1.md
```

## EXPECTED_RESULT

```text
- local checkpoint commit
```

## Instruction for orchestrator

```text
Commit accepted aggregate bootstrap checkpoint files locally; do not push.
```
