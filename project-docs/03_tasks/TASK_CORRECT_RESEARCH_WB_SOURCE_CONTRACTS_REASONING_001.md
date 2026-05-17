# TASK PACKET

## TASK_ID

```text
TASK_CORRECT_RESEARCH_WB_SOURCE_CONTRACTS_REASONING_001
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
TASK_RESEARCH_WB_SOURCE_CONTRACTS_001
```

## SOURCE_RESULT_REF

```text
project-runtime/agent-results/TASK_AUDIT_RESEARCH_WB_SOURCE_CONTRACTS_001.md
```

## ATTEMPT_NO

```text
1
```

## FAILURE_TYPE

```text
governance
```

## TASK_TITLE

```text
Correct WB source research reasoning compliance
```

## TASK_TYPE

```text
requirements_analyst
```

## TARGET_ROLE

```text
requirements_analyst
```

## REASONING_LEVEL

```text
VALUE: maximum
OVERRIDE_REASON: Original WB research dispatch used insufficient reasoning level for requirements_analyst role default.
```

## DEPENDENCIES

```text
- TASK_AUDIT_RESEARCH_WB_SOURCE_CONTRACTS_001 returned blocked
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
TASK_AUDIT_RESEARCH_WB_SOURCE_CONTRACTS_001
```

## RESEARCH_QUESTION_ID

```text
RQ_WB_SOURCE_CONTRACTS_001
```

## RESEARCH_PURPOSE

```text
Re-run and independently verify WB source-contract research with maximum reasoning compliance.
```

## RESEARCH_QUESTIONS

```text
- What are the exact WB output fields for suggest, filter, serp/products, sellers, bridges, reports, and export files?
- What CLI commands and configs exist and which are relevant to market-parser-v2?
- How are run_id, SQLite state, checkpoints, latest mirrors, statuses, and error reporting represented?
- What tests exist and which behavior do they prove?
- What source_system value is actually emitted and where must it be normalized to TZ-required wb?
- Which source files or behaviors are unsafe to copy directly and require adaptation?
```

## ALLOWED_SOURCES

```text
- /home/pavel/projects/wb-parser-v1/README.md
- /home/pavel/projects/wb-parser-v1/ARCHITECTURE.md
- /home/pavel/projects/wb-parser-v1/PROJECT_STATE.md
- /home/pavel/projects/wb-parser-v1/DEVELOPMENT_STAGES.md
- /home/pavel/projects/wb-parser-v1/app/suggest/alpha.py
- /home/pavel/projects/wb-parser-v1/app/filter/engine.py
- /home/pavel/projects/wb-parser-v1/app/serp/engine.py
- /home/pavel/projects/wb-parser-v1/app/sellers/engine.py
- /home/pavel/projects/wb-parser-v1/app/common/paths.py
- /home/pavel/projects/wb-parser-v1/app/common/csv_io.py
- /home/pavel/projects/wb-parser-v1/app/common/runner.py
- /home/pavel/projects/wb-parser-v1/state/run_reports/latest.json
```

## FORBIDDEN_SOURCES

```text
- live WB scraping
- cookies
- secrets
- credentials
- files outside ALLOWED_SOURCES unless a new task allows them
```

## EXPECTED_EVIDENCE

```text
- independent check of existing WB research report against allowed sources
- field lists with source file evidence
- command/config inventory
- state/checkpoint/report summary
- tests inventory
- risks and gaps
- secret exposure check limited to allowed files
- explicit reasoning-level evidence in RESULT
```

## EXPECTED_OUTPUT

```text
- corrected WB research report
- corrected research RESULT according to AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE fields
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
Produce an audit-eligible WB source-contract research result by repeating and verifying the original research under maximum reasoning compliance.
```

## SOURCE_OF_TRUTH

```text
- project-docs/03_tasks/TASK_CORRECT_RESEARCH_WB_SOURCE_CONTRACTS_REASONING_001.md
- project-docs/03_tasks/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_AUDIT_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
```

## SCOPE_IN

```text
- inspect only ALLOWED_SOURCES
- verify or correct the existing WB source-contract research report
- verify or correct the existing WB research RESULT
- preserve valid findings and explicitly mark limitations
```

## SCOPE_OUT

```text
- do not edit WB source project
- do not run live scraping
- do not inspect cookies, secrets, or credentials
- do not modify design or implementation docs
- do not commit or push
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/REQUIREMENTS_ANALYST.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_CORRECT_RESEARCH_WB_SOURCE_CONTRACTS_REASONING_001.md
- project-docs/03_tasks/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-runtime/agent-results/TASK_AUDIT_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/07_reports/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001_RESULT.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
```

## INPUTS

```text
- blocked audit result
- original WB research result and report
```

## READ_INPUTS

```text
NONE
```

## EXPECTED_OUTPUTS

```text
- corrected research RESULT according to AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE fields
- corrected detailed report where needed
```

## ALLOWED_FILE_CHANGES

```text
- project-docs/07_reports/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001_RESULT.md
- project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
```

## FORBIDDEN_FILE_CHANGES

```text
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
- agent-system/*
- project-input/*
- project-docs/01_architecture/*
- project-docs/02_stages/*
- project-docs/03_tasks/*
- project-docs/04_audits/*
- project-docs/05_testing/*
- project-docs/06_runtime/*
- project-runtime/* except project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
- .git/*
- secrets/*
- credentials/*
- cookies/*
```

## ACCEPTANCE_CRITERIA

```text
- corrected result records maximum/xhigh reasoning evidence
- sources remain limited to REQUIRED_DOCS and ALLOWED_SOURCES
- no forbidden sources or secret values are copied
- changed files are limited to ALLOWED_FILE_CHANGES
- unresolved source facts remain explicit limitations
```

## EVIDENCE_REQUIREMENTS

```text
- validation of source boundaries
- changed file list
- forbidden path verification
- secret exposure check
- reasoning-level evidence
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
project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md
```

## RISK_REQUIREMENTS

```text
- correction could alter research facts; any changes must be evidence-backed
```

## MANDATORY_WORKFLOW

```text
requirements_analyst(pass) -> auditor
requirements_analyst(fail) -> auditor
requirements_analyst(blocked) -> orchestrator
requirements_analyst(gap) -> orchestrator
```

## NEXT_ROLE_ON_PASS

```text
auditor
```

## NEXT_ROLE_ON_FAIL

```text
auditor
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
This correction exists only because the original dispatch was below the resolved requirements_analyst reasoning default.
```
