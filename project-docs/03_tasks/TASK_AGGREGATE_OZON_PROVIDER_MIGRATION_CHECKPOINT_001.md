# TASK PACKET

## TASK_ID

```text
TASK_AGGREGATE_OZON_PROVIDER_MIGRATION_CHECKPOINT_001
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
project-runtime/agent-results/TASK_TEST_OZON_PROVIDER_MIGRATION_001.md
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
Aggregate Ozon provider migration checkpoint scope
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
OVERRIDE_REASON: Aggregate checkpoint covers accepted Ozon provider migration implementation, correction, audit/test records, and orchestrator-owned runtime route records.
```

## DEPENDENCIES

```text
- TASK_TEST_OZON_PROVIDER_MIGRATION_001 returned pass
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
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
```

## EXPECTED_EVIDENCE

```text
- checkpoint preflight receipt
- secret scan status
- local checkpoint commit hash
- push status to origin main
```

## EXPECTED_OUTPUT

```text
- Git checkpoint for accepted Ozon provider migration implementation and runtime records
- push to origin main after local checkpoint
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
Provide explicit aggregate checkpoint scope for accepted Ozon provider migration implementation, correction, audit/test results, and orchestrator-owned runtime records.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_AGGREGATE_OZON_PROVIDER_MIGRATION_CHECKPOINT_001.md
- project-runtime/agent-results/TASK_TEST_OZON_PROVIDER_MIGRATION_001.md
```

## SCOPE_IN

```text
- validate changed-file scope for accepted Ozon provider migration bundle
- allow orchestrator-owned runtime records needed to preserve deterministic state
- create checkpoint when preflight passes
- push checkpoint to origin main because project owner authorized push after local checkpoint
```

## SCOPE_OUT

```text
- do not modify agent-system
- do not modify project-input
- do not modify project-archive
- do not inspect source projects directly
- do not read cookies or secrets
```

## REQUIRED_DOCS

```text
- project-docs/03_tasks/TASK_AGGREGATE_OZON_PROVIDER_MIGRATION_CHECKPOINT_001.md
- agent-system/02_runtime/POST_AUDIT_GIT_CHECKPOINT.md
- agent-system/09_validators/GIT_CHECKPOINT_VALIDATION_RULES.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
```

## INPUTS

```text
- accepted Ozon provider migration test pass
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
- push to origin main
- runtime state updated by orchestrator
```

## ALLOWED_FILE_CHANGES

```text
- market-parser-v2/*
- project-docs/03_tasks/TASK_AGGREGATE_OZON_PROVIDER_MIGRATION_CHECKPOINT_001.md
- project-docs/03_tasks/TASK_AUDIT_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-docs/03_tasks/TASK_CORRECT_OZON_PROVIDER_MISSING_SELLER_QUALITY_001.md
- project-runtime/ACCEPTED_ARTIFACTS.md
- project-runtime/AGENT_RESULTS_LOG.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
- project-runtime/ORCHESTRATOR_EVENTS_LOG.md
- project-runtime/PROJECT_STATE.md
- project-runtime/STATUS_SUMMARY.md
- project-runtime/TASK_REGISTRY.md
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
- browser-profile/*
- node_modules/*
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
```

## ACCEPTANCE_CRITERIA

```text
- checkpoint preflight passes with include-untracked
- no forbidden paths are present in changed files
- secret scan passes
- checkpoint commit is created
- checkpoint commit is pushed to origin main
```

## EVIDENCE_REQUIREMENTS

```text
- checkpoint preflight receipt
- git status before commit
- commit hash after local checkpoint
- push status after checkpoint
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
project-runtime/checkpoints/CHECKPOINT_ELIGIBILITY_TASK_AGGREGATE_OZON_PROVIDER_MIGRATION_CHECKPOINT_001_1.md
```

## RISK_REQUIREMENTS

```text
- aggregate checkpoint may accidentally include unrelated dirty files if preflight scope is too broad
```

## MANDATORY_WORKFLOW

```text
release_manager(pass) -> orchestrator
release_manager(fail) -> orchestrator
release_manager(blocked) -> orchestrator
release_manager(gap) -> orchestrator
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
Push is allowed by repository lock and owner instruction after local checkpoint.
```
