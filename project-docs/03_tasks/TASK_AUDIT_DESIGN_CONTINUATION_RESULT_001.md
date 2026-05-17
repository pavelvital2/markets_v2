# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001
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
project-runtime/agent-results/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
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
Audit design continuation result
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
VALUE: maximum
OVERRIDE_REASON: Design continuation created downstream task-like artifacts.
```

## DEPENDENCIES

```text
- TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001 returned pass
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
- changed-file scope check
- downstream task packet/proposal schema validation
- reasoning-level compliance check
```

## EXPECTED_OUTPUT

```text
- audit RESULT according to AGENT_RESULT_TEMPLATE
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
Independently audit the design continuation output and downstream task-like artifacts.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- project-runtime/agent-results/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## SCOPE_IN

```text
- audit design continuation RESULT against the source task packet
- verify changed-file scope
- validate every changed TASK_*.md and TASK_PROPOSAL*.md artifact
- verify mandatory designer to auditor workflow
- return pass, fail, blocked, or gap
```

## SCOPE_OUT

```text
- do not fix design output
- do not edit files
- do not commit or push
- do not dispatch downstream developer or research tasks
```

## REQUIRED_DOCS

```text
- project-docs/03_tasks/TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- project-runtime/agent-results/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/TASK_PROPOSAL_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_MARKET_ANALYTICS_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/01_architecture/ARCH_MVP_BOUNDARIES_001.md
- project-docs/02_stages/STAGE_PLAN_001.md
- project-docs/03_tasks/TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
- project-docs/03_tasks/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
- project-docs/03_tasks/TASK_PROPOSAL_OWNER_DECISIONS_001.md
- project-docs/04_audits/AUDIT_GATES_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
```

## INPUTS

```text
- design continuation RESULT
- orchestrator validation evidence: downstream task packets/proposal currently fail schema validation
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
```

## EXPECTED_OUTPUTS

```text
- RESULT according to AGENT_RESULT_TEMPLATE
- mandatory audit evidence statuses from AUDITOR.md
- VALIDATED_TASK_PACKETS list
```

## ALLOWED_FILE_CHANGES

```text
NONE
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-runtime/*
- project-docs/*
- project-input/*
- project-archive/*
- .git/*
- .env
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- auditor returns pass, fail, blocked, or gap
- auditor includes mandatory audit evidence statuses
- changed task-like artifacts are classified and validated
- auditor makes no file changes
```

## EVIDENCE_REQUIREMENTS

```text
- list read documents
- list validation commands or manual checks
- include changed-file scope status
- include downstream task/proposal schema status
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
project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001.md
```

## RISK_REQUIREMENTS

```text
- downstream task-like artifacts may be malformed
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
agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
```

## TERMINAL_CONDITIONS

```text
NONE
```

## NOTES

```text
Audit must fail or block if dispatchable downstream task packets are schema-invalid.
```
