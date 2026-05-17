# TASK PACKET

## TASK_ID

```text
TASK_AUDIT_RESEARCH_OZON_SOURCE_CONTRACTS_001
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
project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
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
Audit Ozon source contract research
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
OVERRIDE_REASON: Research dependency audit must verify bounded source use, secret exposure, and reasoning compliance.
```

## DEPENDENCIES

```text
- TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001 returned pass
```

## DEPENDENCY_STATUS

```text
ready
```

## REQUESTED_BY_ROLE

```text
requirements_analyst
```

## REQUESTED_BY_TASK

```text
TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001
```

## RESEARCH_QUESTION_ID

```text
RQ_OZON_SOURCE_CONTRACTS_001
```

## RESEARCH_PURPOSE

```text
Audit Ozon source-contract research for bounded-source compliance, evidence quality, secret exposure, and reasoning compliance.
```

## RESEARCH_QUESTIONS

```text
- Did the research use only REQUIRED_DOCS and ALLOWED_SOURCES?
- Are forbidden sources excluded?
- Does the RESULT satisfy AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE fields?
- Are changed files within the research task ALLOWED_FILE_CHANGES?
- Are no secret values exposed?
- Is requirements_analyst maximum reasoning compliance traceable?
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
- bounded-source compliance check
- secret exposure check
- research result template check
- reasoning-level compliance check
```

## EXPECTED_OUTPUT

```text
- audit RESULT according to AGENT_RESULT_TEMPLATE
```

## RETURN_TO_REQUESTER_AFTER_AUDIT_PASS

```text
yes
```

## RETURN_TO_ROLE_AFTER_AUDIT_PASS

```text
designer
```

## RETURN_TASK_AFTER_AUDIT_PASS

```text
project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md
```

## PURPOSE

```text
Independently audit the Ozon source-contract research result before it may be used by designer continuation.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_AUDIT_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-docs/07_reports/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001_RESULT.md
```

## SCOPE_IN

```text
- audit research RESULT against source task packet
- verify changed-file scope
- verify bounded-source compliance
- verify no copied secret values
- verify research evidence and unresolved findings are adequate
- verify reasoning-level compliance from runtime dispatch evidence
- return pass, fail, blocked, or gap
```

## SCOPE_OUT

```text
- do not inspect source projects directly beyond the research report/result evidence
- do not fix research output
- do not edit files
- do not commit or push
- do not dispatch designer continuation
```

## REQUIRED_DOCS

```text
- project-docs/03_tasks/TASK_AUDIT_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-docs/07_reports/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001_RESULT.md
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
- agent-system/09_validators/SECRET_SCAN_RULES.md
- agent-system/09_validators/REASONING_LEVEL_VALIDATION_RULES.md
```

## INPUTS

```text
- Ozon research RESULT
- Ozon research report
```

## READ_INPUTS

```text
- project-runtime/PROJECT_STATE.md
- project-runtime/CURRENT_GATE.md
- project-runtime/NEXT_ACTION.md
- project-runtime/ORCHESTRATOR_EVENTS_LOG.md
```

## EXPECTED_OUTPUTS

```text
- RESULT according to AGENT_RESULT_TEMPLATE
- mandatory audit evidence statuses from AUDITOR.md
```

## ALLOWED_FILE_CHANGES

```text
NONE
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-input/*
- project-docs/*
- project-runtime/*
- project-archive/*
- .git/*
- .env
- .env.*
- secrets/*
- credentials/*
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
```

## ACCEPTANCE_CRITERIA

```text
- research RESULT conforms to AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE fields
- research changed files are limited to TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001 ALLOWED_FILE_CHANGES
- report sources are within task REQUIRED_DOCS and ALLOWED_SOURCES
- no forbidden source content or secret values are copied
- reasoning-level compliance is traceable to xhigh dispatch evidence
```

## EVIDENCE_REQUIREMENTS

```text
- CHANGED_FILES_SCOPE_STATUS
- TASK_PACKET_SCHEMA_STATUS
- REPOSITORY_IDENTITY_STATUS
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
project-runtime/agent-results/TASK_AUDIT_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## RISK_REQUIREMENTS

```text
- research may have copied forbidden source details or secret values
- source limitations may be underreported
```

## MANDATORY_WORKFLOW

```text
auditor(pass) -> designer
auditor(fail) -> orchestrator
auditor(blocked) -> orchestrator
auditor(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
designer
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
This audit does not authorize designer continuation until orchestrator records the result.
```
