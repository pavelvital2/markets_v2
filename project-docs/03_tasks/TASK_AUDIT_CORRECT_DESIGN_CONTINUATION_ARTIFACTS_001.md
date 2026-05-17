# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001
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
TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001
```

## SOURCE_RESULT_REF

```text
project-runtime/agent-results/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
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
Audit corrected design continuation artifacts
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
OVERRIDE_REASON: Correction after failed audit must verify task/proposal schema and changed-file scope.
```

## DEPENDENCIES

```text
- TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001 returned pass
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
TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001
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
- changed-file scope check against TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001
- dispatch validation for every corrected TASK_PACKET
- schema validation for TASK_PROPOSAL_OWNER_DECISIONS_001
- forbidden path and runtime mutation checks
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
Independently audit the correction result and verify the corrected downstream task/proposal artifacts are schema-valid and scope-compliant.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_AUDIT_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
- project-docs/03_tasks/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
- project-runtime/agent-results/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
- project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001.md
```

## SCOPE_IN

```text
- audit correction RESULT against the correction task packet
- verify changed-file scope and forbidden path compliance
- validate six corrected dispatchable TASK_PACKET files
- validate corrected TASK_PROPOSAL_OWNER_DECISIONS_001 as non-dispatchable proposal
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
- project-docs/03_tasks/TASK_AUDIT_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
- project-docs/03_tasks/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
- project-runtime/agent-results/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
- project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001.md
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/TASK_PROPOSAL_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
- project-docs/03_tasks/TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
- project-docs/03_tasks/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
- project-docs/03_tasks/TASK_PROPOSAL_OWNER_DECISIONS_001.md
```

## INPUTS

```text
- correction RESULT
- corrected downstream task/proposal artifacts
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
- project-input/*
- project-archive/*
- project-docs/*
- .git/*
- .env
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- correction RESULT conforms to AGENT_RESULT_TEMPLATE
- all six corrected TASK_PACKET files pass dispatch validation
- TASK_PROPOSAL_OWNER_DECISIONS_001 passes proposal schema validation and remains non-dispatchable
- correction changed files are limited to its ALLOWED_FILE_CHANGES
- no forbidden files are changed by the auditor
```

## EVIDENCE_REQUIREMENTS

```text
- validation command results
- changed-file scope check
- forbidden path check
- runtime mutation check
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
project-runtime/agent-results/TASK_AUDIT_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
```

## RISK_REQUIREMENTS

```text
- corrected packets may pass schema while still depending on pending audit/research gates
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
This audit is limited to correction evidence and corrected task/proposal schema compliance.
```
