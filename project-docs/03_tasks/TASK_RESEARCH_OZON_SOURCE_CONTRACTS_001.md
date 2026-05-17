# TASK PACKET

## TASK_ID

```text
TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
research_dependency
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
Research Ozon source contracts for market-parser-v2
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
VALUE: high
OVERRIDE_REASON: NONE
```

## DEPENDENCIES

```text
- TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001 pass
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
TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001
```

## RESEARCH_QUESTION_ID

```text
RQ_OZON_SOURCE_CONTRACTS_001
```

## RESEARCH_PURPOSE

```text
Confirm Ozon prototype fields, browser flow, extraction rules, tests, outputs, and migration constraints needed for provider implementation tasks.
```

## RESEARCH_QUESTIONS

```text
- What are the exact Ozon suggest, products/SERP, seller, and bridge output fields?
- Which scripts implement collection and what inputs/configs do they require?
- How do extractors parse widgetStates and product-card seller state?
- What tests exist and what behavior do they prove?
- Which WB-shaped output assumptions are compatibility-only?
- What runtime infrastructure is missing compared with WB and must be implemented in market-parser-v2?
- What anti-bot, cookie, fixture, and secret-handling risks are present?
```

## ALLOWED_SOURCES

```text
- /home/pavel/projects/parser_ozon/package.json
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_suggest.js
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_products.js
- /home/pavel/projects/parser_ozon/scripts/enrich_ozon_sellers.js
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_network.js
- /home/pavel/projects/parser_ozon/ozon_parser/extractor.py
- /home/pavel/projects/parser_ozon/ozon_parser/suggest_extractor.py
- /home/pavel/projects/parser_ozon/tests/test_ozon_extractor.py
- /home/pavel/projects/parser_ozon/tests/test_ozon_suggest_extractor.py
- /home/pavel/projects/parser_ozon/docs/ozon_parser/*
```

## FORBIDDEN_SOURCES

```text
- live Ozon scraping
- cookies
- secrets
- credentials
- browser profiles
- files outside ALLOWED_SOURCES unless a new task allows them
```

## EXPECTED_EVIDENCE

```text
- field lists with source file evidence
- script/config inventory
- extractor behavior summary
- tests inventory
- docs-vs-code mismatches
- risks and gaps
- secret exposure check limited to allowed files
```

## EXPECTED_OUTPUT

```text
- research RESULT according to AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE fields
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
Research Ozon source contracts needed for market-parser-v2 provider implementation design without editing or running the source project.
```

## SOURCE_OF_TRUTH

```text
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## SCOPE_IN

```text
- inspect only ALLOWED_SOURCES
- collect Ozon field-level contracts
- identify runtime and migration constraints
- report unresolved gaps
```

## SCOPE_OUT

```text
- do not edit Ozon source project
- do not run live scraping
- do not inspect cookies, secrets, credentials, or browser profiles
- do not design implementation tasks beyond research implications
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/REQUIREMENTS_ANALYST.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
```

## INPUTS

```text
NONE
```

## READ_INPUTS

```text
NONE
```

## EXPECTED_OUTPUTS

```text
- research RESULT according to AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE fields
```

## ALLOWED_FILE_CHANGES

```text
- project-docs/07_reports/*
- project-runtime/agent-results/*
```

## FORBIDDEN_FILE_CHANGES

```text
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
- agent-system/*
- project-input/*
- .git/*
- secrets/*
- credentials/*
- cookies/*
```

## ACCEPTANCE_CRITERIA

```text
- all findings cite allowed source paths
- exact fields are listed or explicitly marked unresolved
- no source project files are changed
- no secrets are copied into result
- research implications identify what design/implementation can safely do next
```

## EVIDENCE_REQUIREMENTS

```text
- allowed source paths cited for every finding
- script, config, extractor, and test inventory
- docs-vs-code mismatch summary
- secret exposure check limited to allowed files
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
project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## RISK_REQUIREMENTS

```text
- unresolved source facts must be reported as gaps or research limitations
- browser profile, cookie, and anti-bot risks must not be converted into implementation assumptions
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
Research output must not influence implementation design until an independent auditor returns pass.
```
