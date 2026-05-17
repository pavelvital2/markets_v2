RESULT:
STATUS: pass

ROLE:
requirements_analyst

TASK:
TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001

SUMMARY:
Collected Ozon field-level contracts, script/config inventory, extractor behavior, tests, docs-vs-code mismatches, security risks, and migration constraints from allowed Ozon sources only. Detailed report is `project-docs/07_reports/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001_RESULT.md`. Reasoning evidence: requirements_analyst role default/recommended level is maximum, and dispatch evidence requested xhigh/maximum despite packet `VALUE: high`.

READ_DOCS:
- agent-system/01_roles/REQUIREMENTS_ANALYST.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- /home/pavel/projects/parser_ozon/package.json
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_suggest.js
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_products.js
- /home/pavel/projects/parser_ozon/scripts/enrich_ozon_sellers.js
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_network.js
- /home/pavel/projects/parser_ozon/ozon_parser/extractor.py
- /home/pavel/projects/parser_ozon/ozon_parser/suggest_extractor.py
- /home/pavel/projects/parser_ozon/tests/test_ozon_extractor.py
- /home/pavel/projects/parser_ozon/tests/test_ozon_suggest_extractor.py
- /home/pavel/projects/parser_ozon/docs/ozon_parser/README.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/ENDPOINTS_AND_EXTRACTION.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/OPERATIONS.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/UNIFIED_HANDOFF.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/endpoint_analysis.md

READ_INPUTS:
- NONE

CHANGED_FILES:
- project-docs/07_reports/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001_RESULT.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md

CREATED_FILES:
- project-docs/07_reports/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001_RESULT.md
- project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md

DELETED_FILES:
- NONE

COMMANDS_RUN:
- `sed -n` on task packet - read TASK_ID, REQUIRED_DOCS, READ_INPUTS, ALLOWED_SOURCES, forbidden sources, allowed file changes, result path, and acceptance criteria first.
- `sed -n` on REQUIRED_DOCS - read requirements analyst role, result templates, TZ, and architecture/security constraints.
- `rg --files /home/pavel/projects/parser_ozon/docs/ozon_parser` - expanded allowed documentation wildcard only.
- `nl -ba ... | sed -n ...` on Ozon ALLOWED_SOURCES - read line-cited package scripts, collectors, extractors, tests, and docs.
- `rg -n "cookie|authorization|proxy-authorization|secret|credential|password|token|OZON_COOKIE_FILE|HAR|fixture|browser profile|profile" <OZON_ALLOWED_SOURCES_ONLY>` - bounded secret/risk exposure scan found cookie path handling, request-header sanitation code, fixture/raw response risks, and no copied secret values.
- `ls -la project-docs/07_reports` and `ls -la project-runtime/agent-results` - checked allowed output directories before creating files.
- `apply_patch` - created only the allowed report and result files.
- `git status --short -- project-docs/07_reports project-runtime/agent-results` - post-edit status showed only the two new allowed output files.
- `git -C /home/pavel/projects/parser_ozon status --short -- <OZON_ALLOWED_SOURCES_PATHS>` - source project status check was unavailable because `/home/pavel/projects/parser_ozon` is not a git repository; no write/edit command was run against that project.
- `rg -n` over RESULT section headings and `wc -l` on created files - RESULT contains required AGENT_RESULT_TEMPLATE and RESEARCH_RESULT_TEMPLATE fields.
- `rg -n "3635012|2dcc2d|cookie=|authorization:|proxy-authorization|bearer|AKIA|secret" <created_report_and_result>` - final created-file check found only policy/risk text, no copied secret values or opaque token examples.

EVIDENCE:
- Detailed research report: `project-docs/07_reports/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001_RESULT.md`.
- REASONING_LEVEL_COMPLIANCE: task packet has `REASONING_LEVEL VALUE: high`; user dispatch evidence states `requirements_analyst role default resolves to maximum` and `reasoning_effort xhigh` to satisfy maximum; role doc recommends maximum. This result explicitly records xhigh/maximum reasoning evidence.
- ORCHESTRATOR_DISPATCH_EVIDENCE: task TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001 was spawned as agent 019e3673-2872-7b13-ba2a-8e9cb615e1c3 (Popper) with reasoning_effort xhigh, satisfying final_required_dispatch_level maximum for requirements_analyst.
- Package scripts: `/home/pavel/projects/parser_ozon/package.json` lines 6-17.
- Suggest fields/flow: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_suggest.js` lines 6-18, 56-73, 103-135, 179-243, 259-360; `/home/pavel/projects/parser_ozon/ozon_parser/suggest_extractor.py` lines 16-46.
- Products fields/flow: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_products.js` lines 6-17, 19-92, 152-241, 252-309, 330-417, 425-496.
- Sellers fields/flow: `/home/pavel/projects/parser_ozon/scripts/enrich_ozon_sellers.js` lines 6-13, 17-100, 196-227, 243-309, 330-448.
- Network capture/security behavior: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_network.js` lines 34-44, 104-152, 184-197.
- Extractor/test behavior: `/home/pavel/projects/parser_ozon/ozon_parser/extractor.py` lines 18-57 and 60-82; `/home/pavel/projects/parser_ozon/tests/test_ozon_extractor.py` lines 14-36; `/home/pavel/projects/parser_ozon/tests/test_ozon_suggest_extractor.py` lines 15-101.
- Ozon documentation contracts and operations: `/home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md`, `/home/pavel/projects/parser_ozon/docs/ozon_parser/ENDPOINTS_AND_EXTRACTION.md`, `/home/pavel/projects/parser_ozon/docs/ozon_parser/OPERATIONS.md`, `/home/pavel/projects/parser_ozon/docs/ozon_parser/UNIFIED_HANDOFF.md`, `/home/pavel/projects/parser_ozon/docs/ozon_parser/endpoint_analysis.md`.

SCOPE_VERIFICATION:
- Task packet was read first, including REQUIRED_DOCS, READ_INPUTS, ALLOWED_SOURCES, FORBIDDEN_SOURCES, ALLOWED_FILE_CHANGES, and RESULT_PATH.
- READ_INPUTS is `NONE`; no additional input refs were used.
- Ozon source facts were inspected only from explicit ALLOWED_SOURCES and expanded `docs/ozon_parser/*`.
- No live scraping, npm scripts, Playwright browser, Python tests, source project commands, or data collection were run.
- No cookies, credentials, secrets, browser profiles, HAR files, raw fixtures, raw private data, or files outside allowed Ozon sources were read for Ozon facts.
- Changes are limited to `project-docs/07_reports/*` and `project-runtime/agent-results/*`.

FORBIDDEN_CHANGES_CHECK:
- No edits were made to `/home/pavel/projects/parser_ozon`, `/home/pavel/projects/wb-parser-v1`, `agent-system`, `project-input`, architecture docs, task packets, `.git`, secrets, credentials, cookies, or browser profiles.
- No commit or push was run.
- No destructive git or filesystem command was run.
- Current worktree status for allowed output directories lists only `project-docs/07_reports/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001_RESULT.md` and `project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md` as new files.
- `/home/pavel/projects/parser_ozon` git status could not be used because it is not a git repository; scope verification is based on executed command classes, all of which were read-only for Ozon sources.
- Secret exposure check was limited to allowed Ozon files and no secret value was copied into the report/result.

RISKS:
- Current scripts use `OZON_COOKIE_FILE` but also hardcode a local cookie fallback `cookie_07.05.26.txt`; final implementation must avoid hardcoded cookie paths.
- Network/suggest/product scripts can write full response bodies or HTML snapshots; request headers are sanitized in network capture, but response-body/user/session state requires a separate sanitization gate before fixtures/raw archives enter Git or export.
- Ozon frontend/widget keys and visual-state paths are unstable; final provider needs prefix matching, fixture tests, and explicit partial/failure statuses.
- Current prototype statuses are `success`, `empty`, `error`; market-parser-v2 needs run/component data-quality statuses such as partial/failure/invalid-for-reports.
- WB-shaped Ozon fields (`nmId`, `supplier_id`) are compatibility-only and must not be joined with WB ids without `source_system`.

BLOCKERS:
- NONE

GAPS:
- NONE

RESEARCH_QUESTION_ID:
RQ_OZON_SOURCE_CONTRACTS_001

RESEARCH_SUMMARY:
- Ozon suggest exact raw/staging/filter fields are confirmed from code and docs; extraction uses `webSuggestions*`, first 5 items, normalization, and dedupe.
- Ozon products/SERP exact raw/staging/mart/pages/preview fields are confirmed; extraction uses initial `state-tileGridDesktop*`, entrypoint `tileGrid*`, opaque `nextPage`, and sequential `absolute_position`.
- Ozon seller and bridge exact fields are confirmed; enrichment reads product-card `state-webCurrentSeller*`, blocks non-document resources, fills `supplier_id`/`supplier_name`, and writes sellers mart plus bridge.
- Existing outputs are WB-shaped compatibility contracts; `nmId` means Ozon product id/sku and `supplier_id` means Ozon seller id.
- Runtime infrastructure missing versus market-parser-v2 needs: provider-aware CLI, shared state/checkpoints, run reports, locks, validation, schema_version, data_quality_status, sanitized export bundle, and Web UI integration.
- Verified row-count claims from docs were not revalidated because output data/fixtures were outside ALLOWED_SOURCES.

SOURCES_USED:
- agent-system/01_roles/REQUIREMENTS_ANALYST.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
- project-docs/03_tasks/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md
- project-input/TZ.md
- project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md
- project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md
- project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md
- /home/pavel/projects/parser_ozon/package.json
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_suggest.js
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_products.js
- /home/pavel/projects/parser_ozon/scripts/enrich_ozon_sellers.js
- /home/pavel/projects/parser_ozon/scripts/collect_ozon_network.js
- /home/pavel/projects/parser_ozon/ozon_parser/extractor.py
- /home/pavel/projects/parser_ozon/ozon_parser/suggest_extractor.py
- /home/pavel/projects/parser_ozon/tests/test_ozon_extractor.py
- /home/pavel/projects/parser_ozon/tests/test_ozon_suggest_extractor.py
- /home/pavel/projects/parser_ozon/docs/ozon_parser/README.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/ENDPOINTS_AND_EXTRACTION.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/OPERATIONS.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/UNIFIED_HANDOFF.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/endpoint_analysis.md

EVIDENCE_MATRIX:
- QUESTION: What are exact Ozon suggest fields?
  SOURCE: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_suggest.js` lines 227-249, 259-360; `/home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md` lines 42-219.
  FINDING: Raw fields are `run_id`, `component`, `collected_at_utc`, `source_system`, `source_type`, `source_ref`, `status`, `error_message`, `base_prefix`, `typed_query`, `letter`, `depth`, `position`, `list_size`, `suggestion`; staging adds `suggestion_lc`, `is_empty_suggestion`; top queries fields and `queries.txt` export are listed in the detailed report.
  CONFIDENCE: maximum
  LIMITATION: Output CSV samples were not read because generated data files are outside ALLOWED_SOURCES.
- QUESTION: What are exact Ozon product/SERP fields?
  SOURCE: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_products.js` lines 19-92, 264-307, 446-496; `/home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md` lines 221-412.
  FINDING: Raw/staging product fields include service fields, query/position fields, WB-shaped id/seller/price/rating fields, `promo_markers`, `raw_json_fragment`, `raw_file`, and `raw_page_path`; mart omits `raw_json_fragment`; pages index and preview export fields are confirmed.
  CONFIDENCE: maximum
  LIMITATION: Documentation-only row count claims were not revalidated.
- QUESTION: What are exact Ozon seller and bridge fields?
  SOURCE: `/home/pavel/projects/parser_ozon/scripts/enrich_ozon_sellers.js` lines 53-100, 386-448; `/home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md` lines 414-554.
  FINDING: Sellers raw/staging fields include service fields, `supplier_id`, `supplier_name`, seller rating/review/count aggregate fields, refs, `raw_file`, and `raw_json_fragment`; mart omits `raw_json_fragment`; bridge fields link query, query_group, `nmId`, seller, and source product run.
  CONFIDENCE: maximum
  LIMITATION: Product-card raw seller states were not read.
- QUESTION: Which scripts implement collection and what inputs/configs do they require?
  SOURCE: `/home/pavel/projects/parser_ozon/package.json` lines 6-17 and script constants in allowed JS files.
  FINDING: Four npm scripts implement network capture, suggest collection, one-query product collection, and seller enrichment; inputs are env/path based and documented in report.
  CONFIDENCE: maximum
  LIMITATION: Scripts were not executed by design.
- QUESTION: How do extractors parse widgetStates and seller state?
  SOURCE: `/home/pavel/projects/parser_ozon/ozon_parser/suggest_extractor.py` lines 16-46; `/home/pavel/projects/parser_ozon/ozon_parser/extractor.py` lines 18-57, 60-82; `/home/pavel/projects/parser_ozon/scripts/enrich_ozon_sellers.js` lines 243-277.
  FINDING: Suggest extractor parses `webSuggestions*`; product extractor parses `tileGrid*` or product-like widgetStates; seller enrichment parses product-card `state-webCurrentSeller*` and recursively finds `sellerId`.
  CONFIDENCE: maximum
  LIMITATION: Current live Ozon frontend shape was not checked.
- QUESTION: What tests exist and what behavior do they prove?
  SOURCE: `/home/pavel/projects/parser_ozon/tests/test_ozon_extractor.py` lines 14-36; `/home/pavel/projects/parser_ozon/tests/test_ozon_suggest_extractor.py` lines 15-101.
  FINDING: Tests cover product extraction from fixture, ignoring non-product widget states, first-five suggest extraction, case/yo dedupe, and optional captured suggest fixture behavior.
  CONFIDENCE: high
  LIMITATION: Tests were not run and fixture files were not read.
- QUESTION: Which WB-shaped output assumptions are compatibility-only?
  SOURCE: `/home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md` lines 556-574; `/home/pavel/projects/parser_ozon/docs/ozon_parser/UNIFIED_HANDOFF.md` lines 320-345.
  FINDING: `nmId` stores Ozon product id for compatibility only; `supplier_id` stores Ozon seller id; both require provider context and should map to provider-neutral common fields in market-parser-v2.
  CONFIDENCE: maximum
  LIMITATION: Final normalized contract mapping remains a design task.
- QUESTION: What runtime infrastructure is missing compared with WB and market-parser-v2 needs?
  SOURCE: `/home/pavel/projects/parser_ozon/docs/ozon_parser/UNIFIED_HANDOFF.md` lines 320-334; `/home/pavel/projects/parser_ozon/docs/ozon_parser/OPERATIONS.md` lines 314-333.
  FINDING: Missing provider-aware CLI, StateDB/checkpoints, run reports, locks, config YAML, validation, Web UI integration, schema_version, data_quality_status, and export bundle.
  CONFIDENCE: maximum
  LIMITATION: WB source details were intentionally not inspected in this Ozon task.
- QUESTION: What anti-bot, cookie, fixture, and secret-handling risks are present?
  SOURCE: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_network.js` lines 34-44, 135-152, 184-197; `/home/pavel/projects/parser_ozon/docs/ozon_parser/ENDPOINTS_AND_EXTRACTION.md` lines 7-21, 308-353; `/home/pavel/projects/parser_ozon/docs/ozon_parser/endpoint_analysis.md` lines 167-193.
  FINDING: Cookie path must be env/external; request headers are sanitized in network capture, but full response bodies/HTML snapshots may carry sensitive state and require sanitization; Ozon anti-bot/empty pages require throttling, document-only seller loading, resume, and partial/failure status handling.
  CONFIDENCE: high
  LIMITATION: Raw fixtures and live responses were not read.

UNRESOLVED_FINDINGS:
- Current latest output row counts and CSV contents are documentation-only claims; generated outputs were not allowed sources.
- Exact sensitivity of raw Ozon response bodies and HTML snapshots is unresolved because fixtures/HAR/raw private data were not read.
- Current live Ozon endpoint/widget shape as of 2026-05-17 is unresolved because live scraping was forbidden.
- Final normalized field names for `external_product_id`, `external_seller_id`, product URL/image URL, `schema_version`, and `data_quality_status` require design decisions after audit.

DESIGN_OR_TASK_IMPLICATIONS:
- Implement Ozon as provider-specific components behind market-parser-v2 core, not as permanent standalone Node scripts.
- Preserve source-derived extraction rules but normalize output contracts to provider-aware fields and required service fields.
- Keep Ozon pagination opaque via `nextPage`; do not synthesize `paginator_token`, `search_page_state`, or `start_page_id`.
- Use `absolute_position` and visibility buckets for analytics compatibility; do not compare Ozon page numbers with WB page numbers.
- Add sanitization and secret exclusion before any raw Ozon response, fixture, or export bundle is committed or exposed.
- Add run reports, checkpoints/resume, throttling/concurrency config, contract validation, and partial/failure data-quality semantics before production migration.

RECOMMENDED_NEXT_ACTION:
- Send this research result to mandatory independent audit; after audit pass, return to designer continuation task `project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_CONTRACT_RESEARCH_001.md`.

NEXT_RECOMMENDED_ACTION:
- Request audit for `TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001`; after audit pass, route back to designer continuation per task packet.
