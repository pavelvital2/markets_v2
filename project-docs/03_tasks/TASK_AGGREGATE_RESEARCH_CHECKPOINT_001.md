# TASK PACKET

## TASK_ID

```text
TASK_AGGREGATE_RESEARCH_CHECKPOINT_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
correction
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
project-runtime/agent-results/TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001_PASS.md
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
Aggregate research checkpoint scope
```

## TASK_TYPE

```text
release_manager
```

## TARGET_ROLE

```text
release_manager
```

## REASONING_LEVEL

```text
VALUE: maximum
OVERRIDE_REASON: NONE
```

## DEPENDENCIES

```text
- TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001 returned pass
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
- checkpoint preflight receipt
- secret scan status
```

## EXPECTED_OUTPUT

```text
- local-only Git checkpoint for accepted research artifacts
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
Provide explicit aggregate checkpoint scope for accepted source discovery research report, audit records, and orchestrator-owned runtime records.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_AGGREGATE_RESEARCH_CHECKPOINT_001.md
- project-runtime/agent-results/TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001_PASS.md
```

## SCOPE_IN

```text
- validate aggregate changed-file scope for accepted research artifacts
- allow orchestrator-owned runtime records needed to preserve deterministic state
- create a local-only checkpoint when preflight passes
```

## SCOPE_OUT

```text
- do not modify agent-system
- do not modify project-input
- do not modify project-archive
- do not push
- do not dispatch design continuation before checkpoint succeeds
```

## REQUIRED_DOCS

```text
- project-docs/03_tasks/TASK_AGGREGATE_RESEARCH_CHECKPOINT_001.md
- agent-system/02_runtime/POST_AUDIT_GIT_CHECKPOINT.md
- agent-system/09_validators/GIT_CHECKPOINT_VALIDATION_RULES.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
```

## INPUTS

```text
- accepted research result and audit pass
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
```

## EXPECTED_OUTPUTS

```text
- checkpoint preflight receipt
- local commit when preflight passes
- runtime state updated by orchestrator
```

## ALLOWED_FILE_CHANGES

```text
- project-docs/03_tasks/TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_AGGREGATE_RESEARCH_CHECKPOINT_001.md
- project-docs/07_reports/TASK_RESEARCH_SOURCE_DISCOVERY_001_RESULT.md
- project-runtime/AGENT_RESULTS_LOG.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
- project-runtime/ORCHESTRATOR_EVENTS_LOG.md
- project-runtime/PROJECT_STATE.md
- project-runtime/STATUS_SUMMARY.md
- project-runtime/TASK_REGISTRY.md
- project-runtime/ACCEPTED_ARTIFACTS.md
- project-runtime/agent-results/*
- project-runtime/checkpoints/*
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-input/*
- project-archive/*
- .git/*
- .env
- .env.*
- secrets/*
- credentials/*
- data/*
- logs/*
- cookies/*
- raw/*
- raw-archives/*
```

## ACCEPTANCE_CRITERIA

```text
- checkpoint preflight passes with CHECKPOINT_ELIGIBILITY_STATUS eligible
- secret scan passes
- local commit records accepted files
- push is not attempted because PUSH_ALLOWED is false
```

## EVIDENCE_REQUIREMENTS

```text
- checkpoint receipt path
- git commit hash
- validation command results
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
project-runtime/checkpoints/CHECKPOINT_ELIGIBILITY_TASK_AGGREGATE_RESEARCH_CHECKPOINT_001_1.md
```

## RISK_REQUIREMENTS

```text
- aggregate checkpoint must not hide unauthorized profile-agent changes
```

## MANDATORY_WORKFLOW

```text
orchestrator checkpoint only after auditor pass
```

## NEXT_ROLE_ON_PASS

```text
orchestrator
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
none
```

## TESTING_REQUIREMENTS

```text
none
```

## DOCUMENTATION_REQUIREMENTS

```text
none
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
agent-system/02_runtime/POST_AUDIT_GIT_CHECKPOINT.md
```

## RESULT_FORMAT

```text
agent-system/03_templates/CHECKPOINT_ELIGIBILITY_TEMPLATE.md
```

## TERMINAL_CONDITIONS

```text
NONE
```

## NOTES

```text
This packet is a checkpoint-scope descriptor for orchestrator-owned preflight and local checkpoint only. It is not a profile-agent implementation task and does not grant push authority.
```
