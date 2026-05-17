# RESULT: TASK_RESEARCH_SOURCE_DISCOVERY_001

RESULT:
STATUS: pass

ROLE:
requirements_analyst

TASK:
TASK_RESEARCH_SOURCE_DISCOVERY_001

SUMMARY:
Source discovery completed from the bounded packet inputs only. WB parser V1 is confirmed as an operational staged parser with CLI, SQLite state, checkpoints, latest mirrors, run reports, Web UI, and CSV contracts. Ozon is confirmed as a working prototype with Playwright/Chromium scripts, Python extractors/tests, WB-compatible CSV-shaped outputs, and documented verified run evidence, but it lacks the WB runtime infrastructure. No live WB/Ozon scraping was run and no secret values, cookies, credentials, auth tokens, browser profiles, or fixture bodies were copied.

READ_DOCS:
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-input/TZ.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
- /home/pavel/projects/wb-parser-v1/README.md
- /home/pavel/projects/wb-parser-v1/ARCHITECTURE.md
- /home/pavel/projects/wb-parser-v1/PROJECT_STATE.md
- /home/pavel/projects/wb-parser-v1/DEVELOPMENT_STAGES.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/README.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/ENDPOINTS_AND_EXTRACTION.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/OPERATIONS.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/UNIFIED_HANDOFF.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/endpoint_analysis.md

READ_INPUTS:
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

CHANGED_FILES:
- NONE

CREATED_FILES:
- project-docs/07_reports/TASK_RESEARCH_SOURCE_DISCOVERY_001_RESULT.md

DELETED_FILES:
- NONE

COMMANDS_RUN:
- `sed -n '1,240p' project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md` -> read task packet part 1.
- `sed -n '241,520p' project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md` -> read task packet part 2.
- `sed -n '1,260p' project-input/TZ.md`; `sed -n '261,620p' project-input/TZ.md`; `sed -n '621,980p' project-input/TZ.md`; `sed -n '981,1320p' project-input/TZ.md` -> read required product brief.
- `sed -n '1,220p' agent-system/03_templates/AGENT_RESULT_TEMPLATE.md` -> read result template.
- `sed -n '1,260p' agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md` -> read research template.
- `find /home/pavel/projects/parser_ozon/docs/ozon_parser -maxdepth 1 -type f -print | sort` -> enumerated allowed Ozon docs glob only.
- `sed -n ... /home/pavel/projects/wb-parser-v1/README.md ARCHITECTURE.md PROJECT_STATE.md DEVELOPMENT_STAGES.md` -> read WB docs.
- `sed -n ... /home/pavel/projects/wb-parser-v1/app/common/paths.py csv_io.py runner.py` -> read WB common runtime code.
- `sed -n ... /home/pavel/projects/wb-parser-v1/app/suggest/alpha.py filter/engine.py serp/engine.py sellers/engine.py` -> read WB component code and field lists.
- `rg -n "def _fields|raw_fields|staging_fields|mart_fields|bridge_fields|..." /home/pavel/projects/wb-parser-v1/app/...` -> located WB code-defined field lists.
- `sed -n '1,260p' /home/pavel/projects/wb-parser-v1/state/run_reports/latest.json` -> read WB latest run report.
- `sed -n ... /home/pavel/projects/parser_ozon/package.json scripts/*.js` -> read Ozon package scripts and collectors/enrichment/network capture.
- `sed -n ... /home/pavel/projects/parser_ozon/ozon_parser/*.py /home/pavel/projects/parser_ozon/tests/*.py` -> read Ozon Python extractors and tests.
- `sed -n ... /home/pavel/projects/parser_ozon/docs/ozon_parser/*.md` -> read allowed Ozon docs.
- `rg -n "cookie|authorization|proxy-authorization|token|secret|password|api[_ -]?key|OZON_COOKIE|WB_COOKIE|WEBUI_SECRET|WEBUI_ADMIN" <allowed files only>` -> bounded secret-surface check; found only env names, placeholders, hardcoded local cookie path strings, code references, and policy text, not secret values.

EVIDENCE:
- WB architecture/status: `/home/pavel/projects/wb-parser-v1/README.md`, `ARCHITECTURE.md`, `PROJECT_STATE.md`, `DEVELOPMENT_STAGES.md`.
- WB runtime orchestration/status/report facts: `/home/pavel/projects/wb-parser-v1/app/common/runner.py`, `/home/pavel/projects/wb-parser-v1/state/run_reports/latest.json`.
- WB path/latest behavior: `/home/pavel/projects/wb-parser-v1/app/common/paths.py`.
- WB CSV format: `/home/pavel/projects/wb-parser-v1/app/common/csv_io.py` confirms `utf-8-sig` and `;`.
- WB output fields: `/home/pavel/projects/wb-parser-v1/app/suggest/alpha.py`, `app/filter/engine.py`, `app/serp/engine.py`, `app/sellers/engine.py`.
- Ozon scripts and commands: `/home/pavel/projects/parser_ozon/package.json`, `scripts/collect_ozon_suggest.js`, `scripts/collect_ozon_products.js`, `scripts/enrich_ozon_sellers.js`, `scripts/collect_ozon_network.js`.
- Ozon extraction rules/tests: `/home/pavel/projects/parser_ozon/ozon_parser/extractor.py`, `ozon_parser/suggest_extractor.py`, `tests/test_ozon_extractor.py`, `tests/test_ozon_suggest_extractor.py`.
- Ozon verified prototype facts and contracts: `/home/pavel/projects/parser_ozon/docs/ozon_parser/*.md`.

SCOPE_VERIFICATION:
- Inspected only the task packet, REQUIRED_DOCS, READ_INPUTS, and ALLOWED_SOURCES listed in the packet.
- Did not read cookie files, credential files, browser profiles, HAR files, fixture JSON bodies, unrelated source files, `.git`, runtime state outside the explicitly allowed WB `latest.json`, or project secrets.
- Did not run live WB or Ozon collection commands.
- Did not run tests because the packet requested command/test inventory and no live collection; tests reference fixtures outside the allowed source list.
- Wrote only `project-docs/07_reports/TASK_RESEARCH_SOURCE_DISCOVERY_001_RESULT.md`.

FORBIDDEN_CHANGES_CHECK:
- No source project files changed under `/home/pavel/projects/wb-parser-v1` or `/home/pavel/projects/parser_ozon`.
- No files changed under `agent-system`, `project-runtime`, `project-input`, `.git`, secrets, credentials, cookies, or browser profiles.
- No commit or push performed.
- Secret exposure check: only secret-related variable names/placeholders/path strings were observed in allowed files; no cookie, credential, token, password, browser profile, or API key values were copied.

RISKS:
- Ozon frontend/widget structure can change; current extraction depends on `webSuggestions`, `tileGridDesktop`, and `state-webCurrentSeller` prefixes.
- Ozon scripts rely on fresh cookies and Chromium session behavior; anti-bot or empty pages require partial/failure status and resume design.
- Ozon prototype has no WB-style StateDB, run reports, locks, common runner, or Web UI integration.
- Ozon `nmId` and `supplier_id` are compatibility column names only; they are Ozon-local identifiers and must not be joined with WB identifiers without `source_system`.
- WB code default `source_system` appears as `wildberries`, while `TZ.md` requires `wb`; v2 contract must normalize this.
- WB filter outputs do not carry all common service fields, so common service field requirements need explicit per-output handling.
- Ozon raw fixtures and raw JSON fragments may contain sensitive or unstable platform state; do not use them as sample data without a separate sanitization pass.
- Ozon documented verified output row counts were not independently checked in CSV data because those CSV output files were not in the allowed source list.

BLOCKERS:
- NONE

GAPS:
- NONE

NEXT_RECOMMENDED_ACTION:
- Send this research result to mandatory audit; after audit pass, continue with `project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md`.

RESEARCH_QUESTION_ID:
RQ_SOURCE_DISCOVERY_001

RESEARCH_SUMMARY:
- WB confirmed: components `suggest`, `filter`, `serp`, `sellers`; pipelines `daily` and `monthly`; run-scoped `raw/staging/marts`; latest mirrors; SQLite state; checkpoints; retry/backoff; statuses; Web UI; run reports; CSV `utf-8-sig` and `;`.
- WB latest report confirmed: run `20260516_211514Z`, pipeline `daily`, status `success`, totals `items_ok=385`, `items_error=0`; filter selected 20 of 1876 candidates from 2075 WB search analytics rows; SERP produced 300 product rows over 23 pages; sellers processed 65 sellers.
- Ozon confirmed by code: Node scripts collect suggest, products/SERP, seller enrichment, and network fixtures through Playwright/Chromium; Python extractors/tests cover product and suggest parsing.
- Ozon confirmed by docs plus code paths: verified query `шеврон на липучке`, 1000 product rows, 125 Ozon pagination portions, 8 products per desktop portion, 120 unique sellers, 1000 bridge rows.
- Assumption boundary: Ozon verified row counts are documented and code-compatible, but not independently re-read from CSV output because Ozon output CSVs were not allowed sources.
- Sample-data finding: header-only contracts and sanitized mart samples are candidate downstream samples; raw fixtures, cookies, browser profiles, HAR-like captures, and raw JSON fragments must be excluded or separately sanitized.

SOURCES_USED:
- project-input/TZ.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/03_templates/RESEARCH_RESULT_TEMPLATE.md
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
- /home/pavel/projects/parser_ozon/docs/ozon_parser/README.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/ENDPOINTS_AND_EXTRACTION.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/OPERATIONS.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/UNIFIED_HANDOFF.md
- /home/pavel/projects/parser_ozon/docs/ozon_parser/endpoint_analysis.md

EVIDENCE_MATRIX:
- QUESTION: RQ1 WB components and runtime
  SOURCE: `/home/pavel/projects/wb-parser-v1/README.md`; `/home/pavel/projects/wb-parser-v1/ARCHITECTURE.md`; `/home/pavel/projects/wb-parser-v1/PROJECT_STATE.md`
  FINDING: WB V1 is documented as operational with `suggest`, `filter`, `serp`, `sellers`, unified CLI, SQLite state, checkpoints, retry/backoff, contracts/smoke checks, doctor, Web UI, cleanup, locks, normalized error codes, and run reports.
  CONFIDENCE: high
  LIMITATION: Documentation can diverge from code; code field checks were performed separately.
- QUESTION: RQ1 WB pipelines and commands
  SOURCE: `/home/pavel/projects/wb-parser-v1/README.md`; `/home/pavel/projects/wb-parser-v1/app/common/runner.py`
  FINDING: CLI commands include `doctor`, `validate`, `runs`, `run suggest/filter/serp/sellers/monthly/daily`, dry-run/job-id, and cleanup. Code resolves `daily` as `filter -> serp -> sellers`; `monthly` is `filter` only when `filter.source_mode=wb_search_analytics`, otherwise `suggest -> filter`.
  CONFIDENCE: maximum
  LIMITATION: Main CLI parser file was not in allowed sources, so command inventory relies on README plus common runner.
- QUESTION: RQ1 WB state/checkpoints/status
  SOURCE: `/home/pavel/projects/wb-parser-v1/README.md`; `/home/pavel/projects/wb-parser-v1/ARCHITECTURE.md`; `/home/pavel/projects/wb-parser-v1/app/common/runner.py`
  FINDING: SQLite tables are documented as `runs`, `tasks`, `errors`, `checkpoints`; checkpoint keys are `prefix|letter|depth`, `stage|group`, `query|page`, `seller_id`; runner statuses are `success`, `partial`, `failed`, `not_ready`; error severity is critical/non-critical.
  CONFIDENCE: high
  LIMITATION: StateDB implementation was not in allowed sources.
- QUESTION: RQ1 WB paths/latest mirrors
  SOURCE: `/home/pavel/projects/wb-parser-v1/app/common/paths.py`; `/home/pavel/projects/wb-parser-v1/README.md`
  FINDING: Historical output paths are `data/{layer}/{component}/{run_id}`; latest publishing copies selected files to `data/{layer}/{component}/latest`; exports live under `exports`.
  CONFIDENCE: maximum
  LIMITATION: Actual data files other than WB latest run report were not opened.
- QUESTION: RQ1 WB CSV format
  SOURCE: `/home/pavel/projects/wb-parser-v1/app/common/csv_io.py`
  FINDING: WB CSV IO uses `CSV_ENCODING = "utf-8-sig"` and `CSV_DELIMITER = ";"`.
  CONFIDENCE: maximum
  LIMITATION: NONE
- QUESTION: RQ1 WB latest report
  SOURCE: `/home/pavel/projects/wb-parser-v1/state/run_reports/latest.json`
  FINDING: Latest allowed run report is `20260516_211514Z`, `daily`, `success`, duration 77 seconds, no errors; filter `items_ok=20`, SERP `items_ok=300`, sellers `items_ok=65`, result refs point to raw/staging/marts/latest/export files.
  CONFIDENCE: maximum
  LIMITATION: This is one latest report only.
- QUESTION: RQ1 WB suggest fields
  SOURCE: `/home/pavel/projects/wb-parser-v1/app/suggest/alpha.py`
  FINDING: Suggest raw fields: `run_id`, `component`, `collected_at_utc`, `source_system`, `source_type`, `source_ref`, `status`, `error_message`, `base_prefix`, `typed_query`, `letter`, `depth`, `position`, `list_size`, `suggestion`; staging adds `suggestion_lc`, `is_empty_suggestion`.
  CONFIDENCE: maximum
  LIMITATION: Suggest latest CSV was not opened.
- QUESTION: RQ1 WB filter fields
  SOURCE: `/home/pavel/projects/wb-parser-v1/app/filter/engine.py`
  FINDING: Filter writes `filter_candidates_raw.csv`, `debug_scores.csv`, `top_queries.csv`, and `queries.txt`. `top_queries.csv` fields are `run_id`, `component`, `rank`, `query`, `query_group`, `niche`, `normalized_query`, `canonical_query`, `source_query`, `hybrid_score`, `score_suggest`, `score_wordstat`, `wordstat_volume`, `count`, `selected_reason`.
  CONFIDENCE: maximum
  LIMITATION: Filter outputs omit several common service fields; v2 must decide whether to preserve or extend.
- QUESTION: RQ1 WB SERP fields
  SOURCE: `/home/pavel/projects/wb-parser-v1/app/serp/engine.py`
  FINDING: SERP product raw/staging fields are `run_id`, `component`, `collected_at_utc`, `source_system`, `source_type`, `source_ref`, `status`, `error_message`, `query`, `query_group`, `page`, `position_on_page`, `absolute_position`, `nmId`, `imtId`, `product_name`, `brand`, `brandId`, `supplier_id`, `supplier_name`, `final_price`, `price`, `sale_price`, `discount`, `sale`, `rating`, `feedbacks`, `valuation`, `total_quantity`, `promo_markers`, `raw_json_fragment`, `raw_file`, `raw_page_path`; mart removes `raw_json_fragment`; pages index fields are `run_id`, `component`, `collected_at_utc`, `source_system`, `source_type`, `source_ref`, `status`, `error_message`, `query`, `query_group`, `page`, `http_status`, `products_count`, `raw_file`, `raw_page_path`.
  CONFIDENCE: maximum
  LIMITATION: NONE
- QUESTION: RQ1 WB sellers fields
  SOURCE: `/home/pavel/projects/wb-parser-v1/app/sellers/engine.py`
  FINDING: Seller raw/staging fields are `run_id`, `component`, `collected_at_utc`, `source_system`, `source_type`, `source_ref`, `status`, `error_message`, `supplier_id`, `supplier_name`, `rating`, `valuation`, `feedbacks_count`, `sale_item_quantity`, `registration_date`, `update_date`, `delivery_duration`, `supp_ratio`, `ratio_mark_supp`, `rating_is_invisible`, `http_status`, `query_count`, `product_count`, `queries_ref`, `query_groups_ref`, `nm_ids_ref`, `source_product_run_ids`, `raw_file`, `raw_json_fragment`; mart removes `raw_json_fragment`; bridge fields are `run_id`, `component`, `collected_at_utc`, `source_system`, `source_type`, `source_ref`, `status`, `error_message`, `supplier_id`, `supplier_name`, `query`, `query_group`, `nmId`, `product_run_id`.
  CONFIDENCE: maximum
  LIMITATION: NONE
- QUESTION: RQ2 Ozon scripts/commands
  SOURCE: `/home/pavel/projects/parser_ozon/package.json`
  FINDING: npm scripts are `capture:ozon`, `collect:suggest`, `collect:products`, and `enrich:sellers`; Playwright is a dev dependency.
  CONFIDENCE: maximum
  LIMITATION: Commands were inventoried, not executed.
- QUESTION: RQ2 Ozon suggest flow
  SOURCE: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_suggest.js`; `/home/pavel/projects/parser_ozon/ozon_parser/suggest_extractor.py`; `/home/pavel/projects/parser_ozon/tests/test_ozon_suggest_extractor.py`
  FINDING: Suggest uses Chromium with Ozon cookies, reads prefixes, creates seed and prefix+Russian-letter tasks, calls `/api/entrypoint-api.bx/page/json/v2?url=/searchSuggestions/search/...`, extracts `widgetStates` keys starting `webSuggestions`, takes only first 5 items, dedupes normalized values, writes raw/staging/top queries/queries export/latest.
  CONFIDENCE: maximum
  LIMITATION: Cookie-dependent collection was not executed.
- QUESTION: RQ2 Ozon product/SERP flow
  SOURCE: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_products.js`; `/home/pavel/projects/parser_ozon/ozon_parser/extractor.py`; `/home/pavel/projects/parser_ozon/tests/test_ozon_extractor.py`; Ozon docs
  FINDING: Product collection opens public search URL in Chromium, captures initial `state-tileGridDesktop` from HTML, captures/fetches page JSON via `/api/entrypoint-api.bx/page/json/v2`, follows `nextPage` as opaque state, extracts `tileGrid` items, computes sequential `absolute_position`, writes raw/staging/mart/pages index/latest/exports and a summary JSON.
  CONFIDENCE: high
  LIMITATION: Actual Ozon output CSVs were not opened; tests reference fixture files not in allowed sources.
- QUESTION: RQ2 Ozon product fields
  SOURCE: `/home/pavel/projects/parser_ozon/scripts/collect_ozon_products.js`; `/home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md`
  FINDING: Ozon product CSV field order intentionally matches WB product fields. `nmId` stores Ozon `sku || id`; `imtId` stores `id || sku`; seller fields are blank until seller enrichment; raw rows include `raw_json_fragment` but marts remove it.
  CONFIDENCE: maximum
  LIMITATION: The script also computes `product_url` and `image_url`, but these are not in standard product CSV fields and only appear in preview/enriched preview output.
- QUESTION: RQ2 Ozon seller enrichment
  SOURCE: `/home/pavel/projects/parser_ozon/scripts/enrich_ozon_sellers.js`; `/home/pavel/projects/parser_ozon/docs/ozon_parser/ENDPOINTS_AND_EXTRACTION.md`
  FINDING: Seller enrichment reads product raw CSV, derives canonical product URLs from product tile raw JSON, skips rows already having `supplier_id`, uses a JSON progress file, loads only HTML documents, blocks scripts/XHR/images/media/fonts/CSS, extracts `state-webCurrentSeller`, recursively finds `sellerId`, reads seller name/rating/reviews, updates product CSVs/exports, writes sellers raw/staging/mart and seller bridge.
  CONFIDENCE: maximum
  LIMITATION: It is a standalone Node script and not a WB-style component runner.
- QUESTION: RQ2 Ozon verified output state
  SOURCE: `/home/pavel/projects/parser_ozon/docs/ozon_parser/DATA_CONTRACTS.md`; `/home/pavel/projects/parser_ozon/docs/ozon_parser/OPERATIONS.md`; `/home/pavel/projects/parser_ozon/docs/ozon_parser/UNIFIED_HANDOFF.md`; `/home/pavel/projects/parser_ozon/docs/ozon_parser/endpoint_analysis.md`
  FINDING: Docs state verified output for query `шеврон на липучке`: `products_daily.csv` has 1000 rows, 125 pages/portions, observed 8 products per desktop response, `absolute_position` 1..1000, all product rows enriched with `supplier_id/supplier_name`, `sellers_daily.csv` 120 rows, bridge 1000 rows, tests 5 OK.
  CONFIDENCE: default
  LIMITATION: This is documented verified output, not independently read from output CSVs under this packet.
- QUESTION: RQ2 Ozon docs/code/output differences
  SOURCE: Ozon docs; Ozon scripts; WB latest run report
  FINDING: Differences: Ozon docs require final no hardcoded cookie path, but scripts have local fallback `cookie_07.05.26.txt`; Ozon prototype docs say final should use WB runtime, but code is standalone Node without StateDB/run reports/locks; standard product CSV drops `product_url/image_url` though scripts/extractor can derive them; docs' WB timing observation references an older latest run (`20260506_211514Z`, 5m19s) while the allowed current WB latest report is `20260516_211514Z`, 77s.
  CONFIDENCE: maximum
  LIMITATION: Ozon output CSV content not read.
- QUESTION: RQ3 confirmed vs assumptions vs gaps
  SOURCE: All allowed sources
  FINDING: Confirmed: code field lists, paths, command names, runtime requirements, WB latest report, Ozon scripts and documented verified state. Assumptions: Ozon documented latest output row counts still reflect current files; Ozon widget paths remain stable. Gaps: direct sanitized sample rows need separate authorization/source allowance; v2 must decide product mart mutation vs separate enriched mart for Ozon sellers; v2 must normalize WB `source_system` to `wb`.
  CONFIDENCE: high
  LIMITATION: Some gaps require design decisions rather than more source reading.
- QUESTION: RQ4 sanitized sample candidates
  SOURCE: Code/docs and secret-surface check over allowed files
  FINDING: Safe candidates: CSV headers from code, manifest/run-report shapes, and after separate scan, small rows from marts without `raw_json_fragment`. Avoid copying cookies, cookie files, browser profiles, unsanitized fixtures, raw Ozon response bodies, raw product/seller JSON fragments, HTML snapshots, and HAR-like captures. `collect_ozon_network.js` removes cookie/authorization/proxy-authorization request headers, but response bodies may still contain platform/user/session fields and need sanitization.
  CONFIDENCE: high
  LIMITATION: No sample rows were copied in this research result.

UNRESOLVED_FINDINGS:
- Direct Ozon latest CSV output row counts and sample row values were not independently verified because output CSVs were not listed in ALLOWED_SOURCES.
- Need design decision: Ozon seller stage currently mutates product raw/staging/mart CSVs after SERP; final contract should either formalize this side effect or write a separate `serp_enriched`/seller-enriched product mart.
- Need contract decision: include `product_url` and `image_url` in common product marts or keep them only in provider-specific/enriched preview outputs.
- Need normalization decision: map WB code/config `source_system=wildberries` to `source_system=wb` required by `TZ.md`, while preserving old compatibility if needed.
- Need sample-data task or authorization if downstream design requires actual sanitized rows rather than header-only contracts.

RISKS:
- Ozon anti-bot behavior, cookies, and frontend widget changes may invalidate observed extraction paths.
- Ozon seller enrichment is the slowest and most block-sensitive stage; concurrency/throttle/resume must be first-class settings.
- Raw fixtures and raw JSON fragments are not automatically safe for reports or export bundles.
- WB and Ozon identifiers are provider-local; analytics must always include `source_system`/`marketplace`.
- Partial runs can be mistaken for complete data unless component statuses, row counts, warnings, and usability flags are in the export manifest.

DESIGN_OR_TASK_IMPLICATIONS:
- Build `market-parser-v2` as provider-aware from the start with `source_system`, `run_id`, component statuses, latest mirrors, run reports, checkpoint/resume, contract validation, and export bundle manifest/checksums.
- Preserve WB-compatible CSV encoding/delimiter and field order where compatibility is required, but document semantic aliases such as Ozon `nmId`.
- Use `absolute_position` for cross-provider analytics; do not compare WB page numbers with Ozon pagination portions.
- Model Ozon pages as opaque `nextPage` portions and compute positions from collected item order/actual `items.length`, not a fixed page size.
- Treat Ozon seller enrichment as a dedicated resumable stage with document-only loading, throttle/concurrency settings, and explicit partial/failure states.
- Exclude cookies, browser profiles, raw fixtures, raw sensitive state, raw JSON fragments, and working logs from analytics export bundles.
- Add contract tests for WB/Ozon field headers, source-system semantics, latest mirrors, and export manifest integrity before analytics importer work.

RECOMMENDED_NEXT_ACTION:
- Audit this report for source-bound compliance, no forbidden reads/changes, and no secret exposure; after audit pass, use it as input for `TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001`.
