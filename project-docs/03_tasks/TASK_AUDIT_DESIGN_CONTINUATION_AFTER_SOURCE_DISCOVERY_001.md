# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
audit
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
NONE
```

## ATTEMPT_NO

```text
NONE
```

## FAILURE_TYPE

```text
none
```

## TASK_TITLE

```text
Audit design continuation after source discovery
```

## TASK_TYPE

```text
auditor
```

## TARGET_ROLE

```text
auditor
```

## REASONING_LEVEL

```text
VALUE: high
OVERRIDE_REASON: NONE
```

## DEPENDENCIES

```text
- TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001 result
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
designer
```

## REQUESTED_BY_TASK

```text
TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001
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
NONE
```

## EXPECTED_OUTPUT

```text
NONE
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
Audit the bounded design documentation and downstream task-like artifacts produced by TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- project-input/TZ.md
- project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
```

## SCOPE_IN

```text
- verify changed-file scope
- verify forbidden paths were not changed
- verify design used only TZ and audited research result
- verify downstream artifact classification
- verify dispatchable task packet boundedness and required fields
- verify non-dispatchable proposals are not usable as NEXT_ACTION task packets
- verify mandatory designer -> auditor transition is preserved
- verify gaps and research dependencies are not guessed over
```

## SCOPE_OUT

```text
- do not audit source projects directly
- do not run implementation tests
- do not modify design artifacts
- do not dispatch developer directly
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/TASK_PACKET_TEMPLATE.md
- agent-system/03_templates/TASK_PROPOSAL_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- project-input/TZ.md
- project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_MARKET_ANALYTICS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/01_architecture/ARCH_MVP_BOUNDARIES_001.md
- project-docs/02_stages/STAGE_PLAN_001.md
- project-docs/04_audits/AUDIT_GATES_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
- project-docs/03_tasks/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
- project-docs/03_tasks/TASK_PROPOSAL_OWNER_DECISIONS_001.md
```

## INPUTS

```text
- designer RESULT for TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001
```

## READ_INPUTS

```text
- designer RESULT for TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001
```

## EXPECTED_OUTPUTS

```text
- auditor RESULT according to AGENT_RESULT_TEMPLATE
- VALIDATED_TASK_PACKETS evidence for every changed task-like artifact
```

## ALLOWED_FILE_CHANGES

```text
- project-runtime/agent-results/*
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-input/*
- project-docs/01_architecture/*
- project-docs/02_stages/*
- project-docs/03_tasks/*
- project-docs/04_audits/*
- project-docs/05_testing/*
- project-docs/06_runtime/*
- project-runtime/* except project-runtime/agent-results/*
- .git/*
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- design evidence lists read documents and changed files
- all changed paths are within the design task ALLOWED_FILE_CHANGES
- no forbidden path mutation is found
- downstream task-like artifacts have explicit TASK_PACKET or TASK_PROPOSAL classification
- dispatchable task packets pass TASK_PACKET schema validation
- non-dispatchable proposal passes TASK_PROPOSAL schema validation and cannot be referenced by NEXT_ACTION
- final next action preserves auditor gate before developer work
```

## EVIDENCE_REQUIREMENTS

```text
- CHANGED_FILES_SCOPE_STATUS
- FORBIDDEN_PATH_STATUS
- RUNTIME_MUTATION_STATUS
- EVIDENCE_STATUS
- SECRET_EXPOSURE_STATUS
- REASONING_LEVEL_COMPLIANCE
- VALIDATED_TASK_PACKETS
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
project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## RISK_REQUIREMENTS

```text
- schema-invalid downstream artifacts must fail audit
- unaudited research or guessed gaps must fail audit
```

## MANDATORY_WORKFLOW

```text
auditor(pass) -> orchestrator
auditor(fail) -> orchestrator
auditor(blocked) -> orchestrator
auditor(gap) -> orchestrator
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
mandatory
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
agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
```

## TERMINAL_CONDITIONS

```text
NONE
```

## NOTES

```text
This task must be dispatched before any developer task created by the design continuation.
```
