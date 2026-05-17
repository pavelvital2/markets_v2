# TASK_RESEARCH_WB_SOURCE_CONTRACTS_001 Research Report

## Scope

Research question: `RQ_WB_SOURCE_CONTRACTS_001`.

Correction task: `TASK_CORRECT_RESEARCH_WB_SOURCE_CONTRACTS_REASONING_001`.

This report was independently re-checked under the correction packet. Sources were limited to:

- correction packet `REQUIRED_DOCS`;
- correction packet WB `ALLOWED_SOURCES`.

WB source facts below are based only on these allowed WB source files:

- `/home/pavel/projects/wb-parser-v1/README.md`
- `/home/pavel/projects/wb-parser-v1/ARCHITECTURE.md`
- `/home/pavel/projects/wb-parser-v1/PROJECT_STATE.md`
- `/home/pavel/projects/wb-parser-v1/DEVELOPMENT_STAGES.md`
- `/home/pavel/projects/wb-parser-v1/app/suggest/alpha.py`
- `/home/pavel/projects/wb-parser-v1/app/filter/engine.py`
- `/home/pavel/projects/wb-parser-v1/app/serp/engine.py`
- `/home/pavel/projects/wb-parser-v1/app/sellers/engine.py`
- `/home/pavel/projects/wb-parser-v1/app/common/paths.py`
- `/home/pavel/projects/wb-parser-v1/app/common/csv_io.py`
- `/home/pavel/projects/wb-parser-v1/app/common/runner.py`
- `/home/pavel/projects/wb-parser-v1/state/run_reports/latest.json`

No live scraping was run. No files outside the task packet's allowed WB source list were inspected for WB source facts. The re-check preserved existing findings where they matched allowed-source evidence and kept unresolved facts as explicit limitations.

## Correction Reasoning and Boundary Evidence

- Reasoning-level requirement: correction packet declares `REASONING_LEVEL VALUE: maximum`; `agent-system/01_roles/REQUIREMENTS_ANALYST.md` also sets the requirements analyst recommended reasoning level to `maximum`; dispatch evidence for this correction records reasoning effort `xhigh`.
- Audit trigger: `project-runtime/agent-results/TASK_AUDIT_RESEARCH_WB_SOURCE_CONTRACTS_001.md` blocked the original result because source/content scope passed but traceable maximum/xhigh reasoning-level evidence was missing.
- READ_INPUTS for the correction packet is `NONE`; no extra runtime inputs were used.
- Forbidden source boundary: no cookies, credentials, browser profiles, `.git` internals, generated WB data files, or unrelated files were inspected for WB source facts.
- Source project boundary: `/home/pavel/projects/wb-parser-v1` was read-only; no source project file was edited.
- Secret exposure check was limited to the allowed WB files and found only variable names, placeholder examples, cookie-path handling, and non-secret token-normalization code terms.
- Result correction scope is limited to `project-docs/07_reports/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001_RESULT.md` and `project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md`.

## High-Level WB Contract Summary

WB V1 is a staged parser with components `suggest`, `filter`, `serp`, and `sellers`; pipeline targets are `monthly` and `daily` (README lines 5-14, ARCHITECTURE lines 6-16). Historical data is run-scoped under raw/staging/marts with `latest` mirrors (README lines 154-162, paths.py lines 74-105). CSV IO uses `utf-8-sig` and `;` (csv_io.py lines 7-35).

The implementation defaults `source_system` to `wildberries` in suggest, SERP, and sellers code, while Market Parser V2 requires `source_system = wb`; migration must normalize this field at provider output or config level (alpha.py line 293, serp/engine.py line 65, sellers/engine.py line 63; TZ requires `wb`).

V1 field lists do not include `schema_version` or `marketplace` in the inspected CSV field arrays. V2 must add them in normalized marts/export contracts.

## Command and Config Inventory

Commands documented in README:

- `py main.py --config config/config.yaml doctor`
- `py main.py --config config/config.yaml validate`
- `py main.py --config config/config.yaml runs --limit 20`
- `py main.py --config config/config.yaml run suggest`
- `py main.py --config config/config.yaml run filter`
- `py main.py --config config/config.yaml run serp`
- `py main.py --config config/config.yaml run sellers`
- `py main.py --config config/config.yaml run monthly`
- `py main.py --config config/config.yaml run daily`
- `py main.py --config config/config.yaml run serp --dry-run --job-id manual_check`
- `py main.py --config config/config.yaml cleanup`
- `py main.py --config config/config.yaml cleanup --apply`
- Web UI: `py -m uvicorn app.webui.app:app --host 127.0.0.1 --port 8080`

Evidence: README lines 96-135, 235-250.

Relevant config/env facts from allowed files:

- Runtime config: `config/config.yaml`; query rules: `config/query_rules.yaml`; prefixes: `config/prefixes.txt` (README lines 47-59).
- Env/path names: `WB_COOKIE_FILE`, `WEBUI_ADMIN_PASSWORD`, `WEBUI_SECRET_KEY`; `.env` is not auto-loaded (README lines 60-70).
- Suggest config keys used in code: `suggest.prefixes_file`, `alphabet_mode`, `throttle_ms`, `type_delay_ms`, `headless`, `user_agent`, `persistent_context`, `max_typed_queries`, `full_refresh_checkpoints`, `force_full_refresh`, `empty_checkpoint_policy`, `browser_profile_dir`; it also reads `serp.wb_cookie_file` if present (alpha.py lines 230-247).
- Filter config keys used in code: `filter.source_mode`, `rules_file`, `input_files.suggest_staging_csv`, `wb_search_analytics_files`, `wb_search_analytics_glob`, `wb_search_analytics_latest_only`, `wordstat_csv_files`, `wordstat_csv`, `wordstat_csv_glob`, and output file names (filter/engine.py lines 76-88, 121-160, 178-208, 350-390, 607-614).
- SERP config keys used in code: `project.source_system`, `serp.base_url`, `request_params`, `user_agent`, `referer_base`, `x_requested_with`, `pages_per_query`, `page_size`, `stop_on_empty_page`, sleeps, `output_files`, `wb_cookie_file`, `wb_cookie_file_env`, and input files for top queries / queries txt (serp/engine.py lines 64-86, 319-360).
- Sellers config keys used in code: `project.source_system`, `sellers.api_base_url`, `curr`, `user_agent`, `sleep_between_sellers_ms`, output file names, `raw_responses_subdir`, `full_refresh_checkpoints`, `request_headers`, and products input file (sellers/engine.py lines 62-80, 82-88, 203-218, 314-328).

## Field-Level Contracts

### Suggest

Files:

- raw: `suggest_alpha_raw.csv`
- staging: `suggest_alpha_staging.csv`

Raw fields confirmed in code:

```text
run_id
component
collected_at_utc
source_system
source_type
source_ref
status
error_message
base_prefix
typed_query
letter
depth
position
list_size
suggestion
```

Staging fields add:

```text
suggestion_lc
is_empty_suggestion
```

Statuses/checkpoint values: `success`, `empty`, `error`; empty checkpoint behavior depends on `empty_checkpoint_policy` (alpha.py lines 27-30, 249-260, 369-485). `source_type` is `wb_suggest_dom`; `source_system` defaults to `wildberries` (alpha.py lines 293-294).

Evidence: alpha.py lines 274-291, 410-459.

### Filter

Files:

- raw: `filter_candidates_raw.csv`
- staging/debug: `debug_scores.csv`
- mart: `top_queries.csv`
- run-local mart text: `queries.txt`
- operator export: `exports/queries.txt`

Raw fields:

```text
run_id
component
collected_at_utc
normalized_query
canonical_query
source_query
niche
count
source_rows
source_typed_queries_count
min_position
suggest_position_sum
depth0_hits
wordstat_volume
parent_query
children_count
```

Debug fields:

```text
run_id
component
normalized_query
canonical_query
source_query
niche
niche_multiplier_total
is_selected
selected_reason
exclude_reason
rank_in_niche
passes_filters
hybrid_score
score_suggest
score_wordstat
score_parent
score_priority
wordstat_volume
count
min_position
source_rows
source_typed_queries_count
depth0_hits
matched_required_terms
matched_priority_patterns
parent_query
children_count
parent_hops_used
parent_selected_flag
```

Top queries fields:

```text
run_id
component
rank
query
query_group
niche
normalized_query
canonical_query
source_query
hybrid_score
score_suggest
score_wordstat
wordstat_volume
count
selected_reason
```

`queries.txt` contains normalized selected queries, one per line, written with `encoding="utf-8"` rather than through the shared CSV writer (filter/engine.py lines 722-733). Filter uses either WB search analytics input or suggest staging; source mode defaults to `wb_search_analytics` (filter/engine.py lines 76-90).

Evidence: filter/engine.py lines 607-749.

### SERP / Products

Files:

- raw CSV: `products_raw.csv`
- raw page index: `pages_raw_index.csv`
- raw page JSON files under `data/raw/serp/{run_id}/{query_slug}/page_{page}.json`
- staging CSV: `products_staging.csv`
- mart CSV: `products_daily.csv`
- export copy for sellers: `exports/products_for_sellers.csv`
- preview export: `exports/products_daily_preview.csv`

Raw and staging product fields:

```text
run_id
component
collected_at_utc
source_system
source_type
source_ref
status
error_message
query
query_group
page
position_on_page
absolute_position
nmId
imtId
product_name
brand
brandId
supplier_id
supplier_name
final_price
price
sale_price
discount
sale
rating
feedbacks
valuation
total_quantity
promo_markers
raw_json_fragment
raw_file
raw_page_path
```

Mart product fields are the same except `raw_json_fragment` is omitted. Page index fields:

```text
run_id
component
collected_at_utc
source_system
source_type
source_ref
status
error_message
query
query_group
page
http_status
products_count
raw_file
raw_page_path
```

Preview export fields:

```text
query
page
position_on_page
absolute_position
nmId
product_name
brand
supplier_id
supplier_name
final_price
price
sale_price
rating
feedbacks
raw_file
run_id
collected_at_utc
```

SERP status values observed in code: `success`, `error`, `empty`, `dry_run`; HTTP/network errors are recorded as non-critical page errors. `source_type` is `wb_serp_exactmatch_v18`; `source_system` defaults to `wildberries`. `absolute_position` is computed as `((page - 1) * page_size) + idx` using configurable page size, default 100.

Evidence: serp/engine.py lines 64-86, 91-305, 477-598, 601-688.

### Sellers

Files:

- raw: `sellers_raw.csv`
- staging: `sellers_staging.csv`
- mart: `sellers_daily.csv`
- bridge: `seller_query_product_bridge.csv`
- raw supplier response JSON under sellers raw response subdir

Raw and staging seller fields:

```text
run_id
component
collected_at_utc
source_system
source_type
source_ref
status
error_message
supplier_id
supplier_name
rating
valuation
feedbacks_count
sale_item_quantity
registration_date
update_date
delivery_duration
supp_ratio
ratio_mark_supp
rating_is_invisible
http_status
query_count
product_count
queries_ref
query_groups_ref
nm_ids_ref
source_product_run_ids
raw_file
raw_json_fragment
```

Seller mart fields are the same except `raw_json_fragment` is omitted. Bridge fields:

```text
run_id
component
collected_at_utc
source_system
source_type
source_ref
status
error_message
supplier_id
supplier_name
query
query_group
nmId
product_run_id
```

Seller status values observed in code: `success`, `error`, `dry_run`; bridge may emit an `empty` row with `error_message=no_links` if no bridge rows are built. `source_type` for seller API rows is `wb_suppliers_shipment_api_v1`; bridge uses `seller_query_product_bridge`. `source_system` defaults to `wildberries`.

Evidence: sellers/engine.py lines 55-201, 226-312, 387-487.

## State, Checkpoints, Latest Mirrors, Reports

Run identity:

- `run_id` format is `YYYYMMDD_HHMMSSZ`, generated once per command invocation and propagated via `RunContext` (README lines 85-94; ARCHITECTURE lines 17-20; runner.py lines 114-146).

Pipeline component resolution:

- `daily`: `filter -> serp -> sellers`.
- `monthly`: `filter` only when `filter.source_mode == wb_search_analytics`, otherwise `suggest -> filter`.
- Single components: `suggest`, `filter`, `serp`, `sellers`.

Evidence: runner.py lines 41-54.

State/checkpoint tables documented:

- `runs`
- `tasks`
- `errors`
- `checkpoints`

Checkpoint key contracts:

- suggest: `prefix|letter|depth`
- filter: `stage|group`
- serp: `query|page`
- sellers: `seller_id`

Evidence: README lines 85-94; ARCHITECTURE lines 81-97; PROJECT_STATE lines 47-63.

Latest mirrors:

- `latest_output_path` first checks `data/{layer}/{component}/latest/{filename}` and falls back to newest run dir.
- `publish_latest_output` copies selected output to `latest`.

Evidence: paths.py lines 82-105.

Run reports:

- `state/run_reports/{run_id}.json`
- `state/run_reports/latest.json`

Report payload fields confirmed by runner:

```text
run_id
pipeline
job_id
status
started_at_utc
finished_at_utc
totals.items_ok
totals.items_error
totals.critical_errors
totals.non_critical_errors
components[]
tasks[]
errors[]
note
lock_path
generated_at_utc
```

`latest.json` sample also includes `duration_seconds`. The sample run `20260516_211514Z` has pipeline `daily`, status `success`, totals `items_ok=385`, `items_error=0`, and component result refs for filter/SERP/sellers outputs.

Evidence: runner.py lines 77-111, 149-181, 183-236, 238-284, 286-362, 364-481; latest.json lines 1-116.

Status model:

- Runner statuses: `success`, `partial`, `failed`, `not_ready` from README/architecture/project state and runner imports/branches.
- Component page/row statuses additionally include `empty`, `error`, `dry_run` in specific CSV outputs.
- Error severity: `critical`, `non_critical`; page/seller fetch errors are recorded as non-critical with network code.

Evidence: README lines 198-205; ARCHITECTURE lines 98-103; runner.py lines 149-181, 183-236, 238-284, 286-362, 442-481; serp/engine.py lines 173-231; sellers/engine.py lines 130-171.

## Tests Inventory

Allowed source facts confirm only:

- Test/sanity command: `py -m pytest -q`.
- Stage 9 says entrypoint commands were verified against the live project including pytest/doctor/cleanup/webui/CLI run.

Evidence: README lines 245-250; DEVELOPMENT_STAGES.md lines 62-70.

Limitations:

- No test files are listed in `ALLOWED_SOURCES`; therefore field-level behavior proven by tests, test names, fixtures, coverage, and exact assertions remain unresolved from this task.

## Migration Constraints and Unsafe Copy Areas

- Normalize `source_system`: V1 defaults to `wildberries`, V2 requires `wb`. Do not copy this default unchanged.
- Add `schema_version`: V1 inspected CSV field arrays do not include it; V2 export/marts require it.
- Add provider-neutral aliases: V1 uses WB-specific `nmId`, `imtId`, `supplier_id`, `supplier_name`; V2 common marts should map `nmId -> external_product_id` and `supplier_id -> external_seller_id` while preserving WB-specific raw/staging fields if needed.
- Add/derive `marketplace`: V1 inspected fields do not include `marketplace`; V2 contracts include marketplace/source_system.
- Keep raw `raw_json_fragment` out of stable analytics bundle unless explicitly sanitized and approved; raw fragments can carry provider response shape and bloat/sensitive operational data risk.
- Do not copy source project paths as production paths; V1 README is Windows-primary and latest sample paths are `/home/pavel/projects/wb-parser-v1/...`; V2 must use its own storage root.
- Treat latest mirrors as convenience only. V2 analytics export/import must preserve run history and manifest/checksum discipline.
- Preserve WB CSV compatibility where needed: `utf-8-sig`, delimiter `;`.
- Keep cookie handling env/path-based. Allowed files show cookie env/path names and cookie header use, but no cookie secret values were inspected or reported.
- Do not assume monthly always runs suggest: runner skips suggest for `filter.source_mode == wb_search_analytics`.
- Do not claim seller data comes from product card enrichment for WB V1; inspected code uses SERP product supplier fields for seeds and a suppliers shipment API for seller details.

## Unresolved Findings

- Exact test coverage and behavior proven by tests are unresolved because tests are outside `ALLOWED_SOURCES`.
- Exact SQLite schema columns are unresolved because `state_db.py` is outside `ALLOWED_SOURCES`; only table names and report/task/error facts from allowed docs/runner are confirmed.
- Exact run report writer behavior for `duration_seconds` and latest copy mechanics inside `run_report.py` are unresolved because `run_report.py` is outside `ALLOWED_SOURCES`; latest sample confirms `duration_seconds` exists in at least one report.
- Exact config validation rules are unresolved because `config_validation.py` and config example are outside `ALLOWED_SOURCES`.
- Exact source constants/error-code values are only partially confirmed through imports and docs because `constants.py` and `error_codes.py` are outside `ALLOWED_SOURCES`.
- Exact current sample CSV headers from generated outputs were not read because generated data files are outside `ALLOWED_SOURCES`; field lists are code-derived.

## Secret Exposure Check

Limited scan command was run only across allowed files:

```text
rg -n "(?i)(password|secret|token|cookie|api[_-]?key|credential|authorization|bearer)" <allowed-files-only>
```

Findings:

- Allowed docs/code contain secret-related variable names and placeholder examples only (`WB_COOKIE_FILE`, `WEBUI_ADMIN_PASSWORD`, `WEBUI_SECRET_KEY`, cookie path/header handling).
- No actual cookie, password, token, API key, bearer token, or credential value was found in the allowed files by this bounded scan.
- False positives included non-secret code terms such as token normalization in filter logic.

## Design / Task Implications

- WB provider tasks should implement a compatibility mapping layer from V1 fields to V2 common contracts rather than copying V1 field names into common marts unchanged.
- Contract validators should check `source_system == wb`, mandatory `schema_version`, provider-scoped IDs, strict CSV headers where applicable, and duplicate product positions per `run_id + query + absolute_position`.
- Export bundle design should include V1-derived WB files as inputs but publish only stable normalized files plus manifest/checksums.
- Additional audited research or a new task is needed if implementation requires exact tests, SQLite schema, config validation internals, or generated sample CSV headers.

## Recommended Next Action

Proceed to independent audit of this corrected research result. If audit passes, return to the designer continuation task so WB provider contract/migration tasks can be designed with the above constraints.
