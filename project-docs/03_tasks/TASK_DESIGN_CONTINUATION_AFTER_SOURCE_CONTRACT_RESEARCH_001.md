# TASK PACKET

## TASK_ID

```text
TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
design_continuation
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
Design continuation after WB and Ozon source contract research
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
OVERRIDE_REASON: Source-contract research must be integrated without guessing unresolved provider facts.
```

## DEPENDENCIES

```text
- TASK_RESEARCH_WB_SOURCE_CONTRACTS_001 audit pass
- TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001 audit pass
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
Use audited WB and Ozon source-contract research to finalize data contracts and create provider migration task packets.
```

## SOURCE_OF_TRUTH

```text
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## SCOPE_IN

```text
- finalize WB field contracts
- finalize Ozon field contracts
- update data contract architecture where needed
- update export contract architecture where needed
- create provider migration task packets
- create audit and testing task packets for provider migration
- report owner gaps where formulas or business thresholds remain undefined
```

## SCOPE_OUT

```text
- do not write code
- do not inspect source projects directly
- do not use unaudited research
- do not dispatch developer directly after design
- do not invent score formulas
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/DESIGNER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/TASK_PACKET_TEMPLATE.md
- agent-system/03_templates/TASK_PROPOSAL_TEMPLATE.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## INPUTS

```text
- audited WB source contract research result
- audited Ozon source contract research result
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## EXPECTED_OUTPUTS

```text
- updated bounded architecture docs if needed
- dispatchable provider migration task packets
- non-dispatchable owner proposals where needed
- RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- project-docs/01_architecture/*
- project-docs/02_stages/*
- project-docs/03_tasks/*
- project-docs/04_audits/*
- project-docs/05_testing/*
- project-docs/06_runtime/*
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-runtime/*
- project-input/*
- .git/*
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- finalized contracts cite audited research facts
- unresolved facts are converted to research dependencies or gaps
- provider migration task packets are bounded
- mandatory designer -> auditor transition is preserved
- no implementation is performed
```

## EVIDENCE_REQUIREMENTS

```text
- audited research result references used for each finalized contract change
- changed file list
- downstream task/proposal validation evidence
- gap or research dependency evidence for unresolved facts
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
project-runtime/agent-results/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
```

## RISK_REQUIREMENTS

```text
- correction or continuation must not convert unaudited source facts into implementation requirements
- owner formula and threshold decisions must remain gaps if still undefined
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
optional
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
This design continuation is blocked until both source-contract research tasks pass independent audit.
```
