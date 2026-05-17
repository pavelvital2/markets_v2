# TASK PACKET

## TASK_ID

```text
TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001
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
TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001
```

## SOURCE_RESULT_REF

```text
project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001.md
```

## ATTEMPT_NO

```text
1
```

## FAILURE_TYPE

```text
audit
```

## TASK_TITLE

```text
Correct design continuation task artifacts
```

## TASK_TYPE

```text
designer
```

## TARGET_ROLE

```text
designer
```

## REASONING_LEVEL

```text
VALUE: maximum
OVERRIDE_REASON: Correction must produce schema-valid downstream task/proposal artifacts.
```

## DEPENDENCIES

```text
- TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001 returned fail
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
auditor
```

## REQUESTED_BY_TASK

```text
TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001
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
- validate_task_packet.py passes for every corrected TASK_PACKET
- proposal schema validation passes for TASK_PROPOSAL_OWNER_DECISIONS_001
```

## EXPECTED_OUTPUT

```text
- corrected downstream task/proposal artifacts
- RESULT according to AGENT_RESULT_TEMPLATE
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
Correct only the schema-invalid downstream task/proposal artifacts from design continuation while preserving their design intent.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
- project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001.md
- agent-system/03_templates/TASK_PACKET_TEMPLATE.md
- agent-system/03_templates/TASK_PROPOSAL_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
```

## SCOPE_IN

```text
- correct six downstream TASK_PACKET files so each conforms to TASK_PACKET_TEMPLATE
- correct TASK_PROPOSAL_OWNER_DECISIONS_001 so it conforms to TASK_PROPOSAL_TEMPLATE and remains non-dispatchable
- preserve design intent and do not add implementation work
```

## SCOPE_OUT

```text
- do not edit architecture/stage/audit/testing/runtime docs
- do not edit project-runtime, agent-system, project-input, source projects, or Git metadata
- do not commit or push
- do not dispatch downstream tasks
```

## REQUIRED_DOCS

```text
- project-docs/03_tasks/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
- project-runtime/agent-results/TASK_AUDIT_DESIGN_CONTINUATION_RESULT_001.md
- agent-system/01_roles/DESIGNER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/TASK_PACKET_TEMPLATE.md
- agent-system/03_templates/TASK_PROPOSAL_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
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
- audit fail result
- schema-invalid downstream task/proposal artifacts
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
```

## EXPECTED_OUTPUTS

```text
- corrected downstream task/proposal artifacts
- RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- project-docs/03_tasks/TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_PARSER_V2_SKELETON_001.md
- project-docs/03_tasks/TASK_DEV_MARKET_ANALYTICS_SKELETON_001.md
- project-docs/03_tasks/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
- project-docs/03_tasks/TASK_PROPOSAL_OWNER_DECISIONS_001.md
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-runtime/*
- project-input/*
- project-archive/*
- .git/*
- .env
- secrets/*
- credentials/*
- project-docs/01_architecture/*
- project-docs/02_stages/*
- project-docs/04_audits/*
- project-docs/05_testing/*
- project-docs/06_runtime/*
- project-docs/03_tasks/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
```

## ACCEPTANCE_CRITERIA

```text
- all six TASK_PACKET files pass validate_task_packet.py
- TASK_PROPOSAL_OWNER_DECISIONS_001 passes proposal schema validation and remains non-dispatchable
- no unrelated files are changed
- RESULT reports validator evidence
```

## EVIDENCE_REQUIREMENTS

```text
- validation command results
- changed file list
- forbidden path verification
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
project-runtime/agent-results/TASK_CORRECT_DESIGN_CONTINUATION_ARTIFACTS_001.md
```

## RISK_REQUIREMENTS

```text
- correction could alter task intent while fixing schema
```

## MANDATORY_WORKFLOW

```text
designer(pass) -> auditor
designer(fail) -> orchestrator
designer(blocked) -> orchestrator
designer(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
auditor
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
This correction is limited to task/proposal schema compliance.
```
