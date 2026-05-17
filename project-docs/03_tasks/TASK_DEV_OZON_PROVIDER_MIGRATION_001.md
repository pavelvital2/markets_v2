# TASK PACKET

## TASK_ID

```text
TASK_DEV_OZON_PROVIDER_MIGRATION_001
```

## TASK_STATUS

```text
active
```

## TASK_KIND

```text
normal
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
NONE
```

## FAILURE_TYPE

```text
none
```

## TASK_TITLE

```text
Migrate Ozon provider into market-parser-v2
```

## TASK_TYPE

```text
developer
```

## TARGET_ROLE

```text
developer
```

## REASONING_LEVEL

```text
VALUE: maximum
OVERRIDE_REASON: Ozon provider migration includes browser behavior, anti-bot states, cookies, raw-response safety, and runtime infrastructure gaps.
```

## DEPENDENCIES

```text
- TASK_DEV_MARKET_PARSER_V2_SKELETON_001 audit pass
- TASK_TEST_PARSER_CONTRACT_EXPORT_QUALITY_001 pass
- TASK_AUDIT_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001 pass
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
TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001
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
- /home/pavel/projects/parser_ozon/* outside ALLOWED_SOURCES
- /home/pavel/projects/wb-parser-v1/*
- raw Ozon outputs, raw fixtures, HAR files, cookies, browser profiles, and generated private data
- secrets/*
- credentials/*
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
Implement the Ozon provider in market-parser-v2 using audited Ozon source-contract evidence and V2 common contracts.
```

## SOURCE_OF_TRUTH

```text
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## SCOPE_IN

```text
- implement Ozon provider suggest, products/SERP, sellers, and export integration behind the V2 provider abstraction
- implement browser/session boundaries without hardcoded local cookie fallback
- use OZON_COOKIE_FILE or equivalent env/path cookie configuration without logging cookie content
- implement webSuggestions* suggest extraction with first 5 dropdown suggestions and dedupe behavior
- implement tileGrid* product extraction with opaque nextPage handling and actual items.length
- compute absolute_position from observed item order
- map Ozon compatibility nmId to external_product_id and supplier_id to external_seller_id under source_system=ozon
- implement product-card state seller enrichment with document-only loading, blocked non-document resources, progress, and resume
- integrate run reports, checkpoints/resume, latest mirrors, validation, data-quality statuses, and export bundle behavior
- add tests using sanitized fixtures or mocked browser responses without live marketplace access
```

## SCOPE_OUT

```text
- do not modify parser_ozon
- do not read Ozon source files outside ALLOWED_SOURCES
- do not read raw Ozon private outputs, HAR files, cookies, browser profiles, or generated private data
- do not migrate WB provider logic
- do not run live scraping unless a future task explicitly allows it
- do not define analytics formulas or thresholds
- do not guess current live Ozon widget behavior beyond audited evidence
```

## REQUIRED_DOCS

```text
- agent-system/01_roles/DEVELOPER.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_DEV_OZON_PROVIDER_MIGRATION_001.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md
- project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- project-docs/06_runtime/RUNTIME_OUTLINE_001.md
- project-docs/05_testing/TESTING_FLOW_001.md
```

## INPUTS

```text
- audited Ozon source-contract research RESULT
```

## READ_INPUTS

```text
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
```

## EXPECTED_OUTPUTS

```text
- Ozon provider implementation in market-parser-v2
- tests for Ozon provider contract behavior
- developer RESULT according to AGENT_RESULT_TEMPLATE
```

## ALLOWED_FILE_CHANGES

```text
- market-parser-v2/*
```

## FORBIDDEN_FILE_CHANGES

```text
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
- agent-system/*
- project-input/*
- project-runtime/*
- project-docs/*
- .git/*
- secrets/*
- credentials/*
- cookies/*
- browser-profile/*
- data/*
- logs/*
```

## ACCEPTANCE_CRITERIA

```text
- Ozon provider runs through V2 provider abstraction without requiring WB code
- Ozon compatibility ids are normalized to provider-neutral aliases under source_system=ozon
- Ozon suggest/products/sellers behavior follows audited extraction constraints
- anti-bot, empty page, missing seller, and blocked enrichment cases produce partial/failure quality statuses
- cookie configuration is env/path based and no hardcoded local fallback remains
- export bundle excludes raw sensitive fragments, HAR files, cookies, browser profiles, and logs
- tests do not require live scraping or secrets
- unresolved Ozon live-widget/raw-sensitivity facts are reported as gaps or research dependencies, not guessed
```

## EVIDENCE_REQUIREMENTS

```text
- changed file list
- test command results or explicit limitation
- Ozon contract validation evidence
- export forbidden-artifact evidence
- confirmation that parser_ozon was not modified
- confirmation that no cookies/secrets/raw private data were read, created, logged, or exported
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
project-runtime/agent-results/TASK_DEV_OZON_PROVIDER_MIGRATION_001.md
```

## RISK_REQUIREMENTS

```text
- live Ozon frontend shape as of execution time is not proven by default tests
- sanitized fixtures may not cover every anti-bot state
- browser behavior may require follow-up runtime hardening
```

## MANDATORY_WORKFLOW

```text
developer(pass) -> auditor
developer(fail) -> auditor
developer(blocked) -> orchestrator
developer(gap) -> orchestrator
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
mandatory
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
Direct Ozon source inspection is limited to ALLOWED_SOURCES and must not create new source-contract requirements beyond audited research evidence.
```

