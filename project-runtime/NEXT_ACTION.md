# NEXT_ACTION

## Next action

Required structured fields:

```text
ACTION_ID: NEXT_MARKET_ANALYTICS_SKELETON_CHECKPOINT_001
ACTION_TYPE: checkpoint
TARGET_ROLE: release_manager
TASK_ID: TASK_AGGREGATE_MARKET_ANALYTICS_SKELETON_CHECKPOINT_001
TASK_PACKET: project-docs/03_tasks/TASK_AGGREGATE_MARKET_ANALYTICS_SKELETON_CHECKPOINT_001.md
DEPENDENCY_STATUS: ready
BLOCKED_BY: NONE
ACTION_SEMANTIC: normal
WORKSPACE_IDENTITY_REQUIRED: yes
REPOSITORY_LOCK_REQUIRED: yes
CHECKPOINT_POLICY: required
CHECKPOINT_PREFLIGHT_REQUIRED: yes
CHECKPOINT_RECEIPT_REQUIRED: yes
CHECKPOINT_RECEIPT_REF: project-runtime/checkpoints/CHECKPOINT_ELIGIBILITY_TASK_AGGREGATE_MARKET_ANALYTICS_SKELETON_CHECKPOINT_001_1.md
REQUESTER_RETURN_CONTEXT: NONE
BLOCKING_OR_RESUME_CONTEXT:
NONE
REQUIRED_UNIVERSAL_DOCS:
- agent-system/02_runtime/POST_AUDIT_GIT_CHECKPOINT.md
- agent-system/09_validators/GIT_CHECKPOINT_VALIDATION_RULES.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
REQUIRED_PROJECT_DOCS:
- project-docs/03_tasks/TASK_AGGREGATE_MARKET_ANALYTICS_SKELETON_CHECKPOINT_001.md
- project-runtime/agent-results/TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001.md
EXPECTED_RESULT:
- checkpoint preflight receipt
- checkpoint commit pushed to origin main
INSTRUCTION_FOR_ORCHESTRATOR: Run checkpoint preflight with include-untracked and push-requested yes, commit accepted market analytics skeleton bundle, then push origin main.
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
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
```

## REQUIRED_PROJECT_DOCS

```text
- project-docs/03_tasks/TASK_AGGREGATE_MARKET_ANALYTICS_SKELETON_CHECKPOINT_001.md
- project-runtime/agent-results/TASK_AUDIT_MARKET_ANALYTICS_SKELETON_001.md
```

## EXPECTED_RESULT

```text
- checkpoint preflight receipt
- checkpoint commit pushed to origin main
```

## Instruction for orchestrator

```text
Run checkpoint preflight with include-untracked and push-requested yes, commit accepted market analytics skeleton bundle, then push origin main.
```
