# TASK PACKET

## TASK_ID

```text
TASK_RESEARCH_SOURCE_DISCOVERY_001
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
RESULT for TASK_BOOTSTRAP_DESIGNER_001
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
Source discovery for WB and Ozon parser facts
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
OVERRIDE_REASON: Source discovery determines downstream contracts and implementation boundaries.
```

## DEPENDENCIES

```text
- TASK_BOOTSTRAP_DESIGNER_001 audit pass
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
Confirm factual contracts, commands, outputs, state, tests, and operational behavior from the existing WB and Ozon parser projects before design continuation.
```

## RESEARCH_QUESTIONS

```text
1. What are the confirmed WB parser components, commands, input/output paths, CSV/JSON fields, run reports, latest mirrors, checkpoints, statuses, and tests?
2. What are the confirmed Ozon parser scripts, extraction flow, Playwright/Chromium requirements, input/output paths, fields, seller enrichment behavior, docs/code/output differences, statuses, and tests?
3. Which fields and behaviors are confirmed, which are assumptions, and which remain gaps or risks for parser and analytics contracts?
4. Which source outputs can provide sanitized sample data for downstream contract design without exposing secrets, cookies, tokens, or sensitive fixtures?
```

## ALLOWED_SOURCES

```text
- project-input/TZ.md
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
- cookies
- credentials
- secrets
- API keys
- auth tokens
- unsanitized HAR files
- browser profile data
- unrelated source project files not listed in ALLOWED_SOURCES
```

## EXPECTED_EVIDENCE

```text
- File references and concise findings for each allowed source inspected.
- Confirmed field lists for WB outputs observed in code/docs/reports.
- Confirmed field lists for Ozon outputs observed in code/docs/tests.
- Docs-vs-code-vs-output mismatch list for Ozon where applicable.
- Command/test inventory without executing network collection unless separately authorized.
- Secret exposure check summary confirming no secret values were copied into the research result.
```

## EXPECTED_OUTPUT

```text
Research RESULT using AGENT_RESULT_TEMPLATE plus RESEARCH_RESULT_TEMPLATE fields, including confirmed facts, assumptions, gaps, risks, and implications for design continuation.
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
project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## PURPOSE

```text
Produce audited factual evidence required before designing data contracts, export contracts, implementation stages, and bounded development tasks.
```

## SOURCE_OF_TRUTH

```text
- project-input/TZ.md
- listed allowed source project files
```

## REQUIRED_DOCS

```text
- project-input/TZ.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
```

## INPUTS

```text
- Existing WB parser source project
- Existing Ozon parser source project
- Ozon parser documentation
```

## READ_INPUTS

```text
- Allowed source files listed in ALLOWED_SOURCES
```

## SCOPE_IN

```text
- inspect only allowed source files;
- inventory confirmed WB parser contracts, flows, outputs, state, reports, commands, tests, and risks;
- inventory confirmed Ozon parser contracts, flows, outputs, browser/session requirements, seller enrichment, commands, tests, and risks;
- classify findings as confirmed, assumption, gap, or risk;
- identify sanitized sample data candidates without copying secrets;
- return research result for audit.
```

## SCOPE_OUT

```text
- do not edit source projects;
- do not run live scraping against WB or Ozon;
- do not copy cookies, credentials, tokens, browser profile data, or unsanitized HAR content;
- do not design final contracts;
- do not create implementation tasks;
- do not commit or push.
```

## EXPECTED_OUTPUTS

```text
- RESULT according to AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE
- confirmed source discovery matrix
- list of design implications for TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001
```

## ALLOWED_FILE_CHANGES

```text
- project-docs/07_reports/*
```

## FORBIDDEN_FILE_CHANGES

```text
- agent-system/*
- project-runtime/*
- project-input/*
- /home/pavel/projects/wb-parser-v1/*
- /home/pavel/projects/parser_ozon/*
- .git/*
- .env
- secrets/*
- credentials/*
```

## ACCEPTANCE_CRITERIA

```text
- research result separates confirmed facts from assumptions, gaps, and risks;
- all findings are traceable to allowed source files;
- no forbidden sources are used;
- no secret values are copied;
- downstream design implications are explicit;
- research result is ready for mandatory audit.
```

## EVIDENCE_REQUIREMENTS

```text
- list read documents;
- list commands run;
- cite file paths for every material finding;
- include forbidden-source and secret-exposure checks.
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
project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
```

## RISK_REQUIREMENTS

```text
- source code and documentation may diverge;
- sample data may be missing or unsafe to copy;
- Ozon frontend behavior may have changed since prior prototype evidence;
- WB/Ozon output fields may require separate confirmed/assumption classification.
```

## MANDATORY_WORKFLOW

```text
requirements_analyst(pass) -> auditor
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
agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
```

## TERMINAL_CONDITIONS

```text
NONE
```

## NOTES

```text
Classification: DISPATCHABLE TASK_PACKET. This task is the bootstrap continuation route.
```
