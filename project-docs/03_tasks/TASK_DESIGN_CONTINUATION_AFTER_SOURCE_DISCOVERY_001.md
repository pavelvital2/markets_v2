# TASK PACKET

## TASK_ID

```text
TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001
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
Audited pass RESULT for TASK_RESEARCH_SOURCE_DISCOVERY_001
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
Design continuation after source discovery
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
OVERRIDE_REASON: Contract and task decomposition must use audited source discovery facts.
```

## DEPENDENCIES

```text
- TASK_RESEARCH_SOURCE_DISCOVERY_001 audit pass
```

## DEPENDENCY_STATUS

```text
pending
```

## REQUESTED_BY_ROLE

```text
designer
```

## REQUESTED_BY_TASK

```text
TASK_BOOTSTRAP_DESIGNER_001
```

## RESEARCH_QUESTION_ID

```text
RQ_SOURCE_DISCOVERY_001
```

## RESEARCH_PURPOSE

```text
Use audited source discovery to continue bounded architecture and task decomposition.
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
Create bounded design documentation and initial implementation/audit task decomposition for Market Intelligence Platform using the source brief and audited research result.
```

## SOURCE_OF_TRUTH

```text
- project-input/TZ.md
- audited RESULT for TASK_RESEARCH_SOURCE_DISCOVERY_001
```

## REQUIRED_DOCS

```text
- project-input/TZ.md
- agent-system/01_roles/DESIGNER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
```

## INPUTS

```text
- audited source discovery result
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
```

## SCOPE_IN

```text
- design bounded project documentation structure;
- create initial architecture documents for parser, analytics, data contracts, export contract, quality model, security constraints, runtime outline, and MVP boundaries as separate bounded documents;
- create first implementation task packets only where facts are confirmed by audited research;
- create research or owner GAP tasks where facts remain unconfirmed;
- define mandatory audit gates, testing flow, and technical writer handoffs.
```

## SCOPE_OUT

```text
- do not write code;
- do not test implementation;
- do not inspect source projects directly unless a new audited research task allows it;
- do not invent business rules missing from TZ or audited research;
- do not dispatch developer directly after design;
- do not commit or push.
```

## EXPECTED_OUTPUTS

```text
- RESULT according to AGENT_RESULT_TEMPLATE
- bounded architecture documents under project-docs/01_architecture/
- dispatchable task packets or non-dispatchable task proposals under project-docs/03_tasks/
- explicit downstream artifact classification
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
- .env
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- design uses only TZ and audited research facts;
- downstream task-like artifacts are classified as DISPATCHABLE TASK_PACKET or NON_DISPATCHABLE TASK_PROPOSAL;
- every dispatchable task packet has bounded scope, minimal REQUIRED_DOCS, acceptance criteria, audit requirements, and next role;
- mandatory designer -> auditor transition is preserved;
- gaps are reported instead of guessed.
```

## EVIDENCE_REQUIREMENTS

```text
- list read documents;
- list changed files;
- include artifact classification;
- include scope and forbidden-change verification.
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
project-runtime/agent-results/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## RISK_REQUIREMENTS

```text
- audited research may expose unresolved source gaps;
- contract design may require additional owner decisions;
- oversized documentation must be avoided.
```

## MANDATORY_WORKFLOW

```text
designer(pass) -> auditor
blocked -> orchestrator
gap -> orchestrator
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
Classification: DISPATCHABLE TASK_PACKET. This task must be dispatched only after TASK_RESEARCH_SOURCE_DISCOVERY_001 has an audited pass result.
```
