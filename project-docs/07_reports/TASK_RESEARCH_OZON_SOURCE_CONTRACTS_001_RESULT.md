# Ozon Source Contracts Research

Task: `TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001`

Role: `requirements_analyst`

Reasoning evidence: xhigh/maximum requested by dispatch; the role default requires maximum reasoning. This report separates code-confirmed facts, documentation-only claims, migration implications, and unresolved limitations.

## Scope

Read scope was limited to the task packet REQUIRED_DOCS and the Ozon ALLOWED_SOURCES:

- `/home/pavel/projects/parser_ozon/package.json`
- `/home/pavel/projects/parser_ozon/scripts/collect_ozon_suggest.js`
- `/home/pavel/projects/parser_ozon/scripts/collect_ozon_products.js`
- `/home/pavel/projects/parser_ozon/scripts/enrich_ozon_sellers.js`
- `/home/pavel/projects/parser_ozon/scripts/collect_ozon_network.js`
- `/home/pavel/projects/parser_ozon/ozon_parser/extractor.py`
- `/home/pavel/projects/parser_ozon/ozon_parser/suggest_extractor.py`
- `/home/pavel/projects/parser_ozon/tests/test_ozon_extractor.py`
- `/home/pavel/projects/parser_ozon/tests/test_ozon_suggest_extractor.py`
- `/home/pavel/projects/parser_ozon/docs/ozon_parser/*`

No live scraping was run. No cookie, fixture, HAR, browser profile, credential, secret, or raw private data files were read.

## Summary

- Ozon prototype is a Playwright/Chromium Node prototype with Python extractors/tests. Package scripts expose `capture:ozon`, `collect:suggest`, `collect:products`, and `enrich:sellers` (`package.json:6-10`).
- Current outputs are WB-shaped compatibility contracts. Ozon product id is written to `nmId`, and Ozon seller id is written to `supplier_id`; both are provider-local and require `source_system=ozon` to avoid cross-marketplace joins (`DATA_CONTRACTS.md:556-574`).
- Suggest extracts `widgetStates["webSuggestions-*"]`, accepts only first 5 dropdown items, dedupes case/`ё`, and writes raw/staging/filter outputs plus `exports/queries.txt` (`collect_ozon_suggest.js:108-135`, `260-360`; `suggest_extractor.py:16-46`).
- SERP/products extract `tileGrid*` states from initial HTML and `/api/entrypoint-api.bx/page/json/v2`, follow opaque `nextPage`, compute `absolute_position` from collected item order, and write raw/staging/mart products plus pages index (`collect_ozon_products.js:252-309`, `330-417`, `425-485`).
- Seller data is not in SERP tileGrid. Seller enrichment visits product cards, loads only document resources, parses `state-webCurrentSeller*`, fills `supplier_id`/`supplier_name`, and writes sellers mart plus query-product-seller bridge (`enrich_ozon_sellers.js:243-277`, `287-309`, `341-448`).
- Source code lacks market-parser-v2 runtime infrastructure: provider-aware CLI, shared state/checkpoints, run reports, run locks, formal config YAML, contract validation, export bundle, schema_version, and data_quality_status. Ozon docs state the same limitation (`UNIFIED_HANDOFF.md:320-334`; `OPERATIONS.md:314-333`).

## Script And Config Inventory

### `package.json`

`package.json` declares one dev dependency, Playwright `^1.59.1`, and four npm scripts (`package.json:6-17`):

| Script | Command | Purpose |
|---|---|---|
| `capture:ozon` | `node scripts/collect_ozon_network.js` | network investigation fixture capture |
| `collect:suggest` | `node scripts/collect_ozon_suggest.js` | suggest/raw/staging/filter query collection |
| `collect:products` | `node scripts/collect_ozon_products.js` | one-query SERP/product collection |
| `enrich:sellers` | `node scripts/enrich_ozon_sellers.js` | product-card seller enrichment |

### `collect_ozon_suggest.js`

Inputs/configs:

- `OZON_COOKIE_FILE`, fallback `cookie_07.05.26.txt` (`collect_ozon_suggest.js:6`).
- `OZON_PREFIXES_FILE`, fallback `config/prefixes.txt` (`collect_ozon_suggest.js:7`, `56-63`).
- `OZON_SUGGEST_FIXTURE_DIR`, fallback `fixtures/ozon/suggest` (`collect_ozon_suggest.js:8`).
- `RUN_ID`, `OZON_MAX_TYPED`, `OZON_TOP_N`, `OZON_SUGGEST_THROTTLE_MS`, `HEADLESS` (`collect_ozon_suggest.js:9-13`).

Behavior:

- Builds tasks as each base prefix plus seed and `prefix + Russian letter`; alphabet has 30 Russian letters, excluding `ъ` and including `ь` (`collect_ozon_suggest.js:19`, `65-73`).
- Calls `/api/entrypoint-api.bx/page/json/v2?url=<encoded /searchSuggestions/search/...>&__rr=1` from inside Chromium page context (`collect_ozon_suggest.js:103-105`, `179-189`).
- Writes fixture JSON with full response body, but no request headers (`collect_ozon_suggest.js:209-221`).
- Writes CSV as UTF-8 with BOM and `;` delimiter (`collect_ozon_suggest.js:84-91`).

### `collect_ozon_products.js`

Inputs/configs:

- `OZON_COOKIE_FILE`, fallback `cookie_07.05.26.txt` (`collect_ozon_products.js:6`).
- `OZON_QUERY`, default `шеврон на липучке` (`collect_ozon_products.js:7`).
- `OZON_QUERY_GROUP`, default `all` (`collect_ozon_products.js:8`).
- `OZON_SERP_PRODUCTS`, `OZON_SERP_PAGES`, `RUN_ID`, `HEADLESS`, `OZON_SERP_THROTTLE_MS` (`collect_ozon_products.js:9-17`, `416`).

Behavior:

- Opens `https://www.ozon.ru/search/?text=<query>` in Chromium and waits for the initial document (`collect_ozon_products.js:350-354`).
- Captures fetch responses to `/api/entrypoint-api.bx/page/json/v2`, extracts tile grids, and stores `nextPage` from response bodies (`collect_ozon_products.js:330-347`).
- Extracts page 1 from initial HTML elements with id prefix `state-tileGridDesktop` (`collect_ozon_products.js:356-378`).
- Follows `nextPage` as the inner URL and does not synthesize pagination tokens (`collect_ozon_products.js:385-417`; `ENDPOINTS_AND_EXTRACTION.md:116-123`).
- Writes raw page JSON under `data/raw/serp/{run_id}/{query_slug}/page_*.json` and CSV outputs under raw/staging/marts/latest/exports (`collect_ozon_products.js:425-485`).

### `enrich_ozon_sellers.js`

Inputs/configs:

- `OZON_COOKIE_FILE`, fallback `cookie_07.05.26.txt` (`enrich_ozon_sellers.js:6`).
- `OZON_PRODUCTS_RAW`, fallback `data/raw/serp/latest/products_raw.csv` (`enrich_ozon_sellers.js:7`).
- `RUN_ID`, `OZON_SELLERS_CONCURRENCY`, `OZON_SELLERS_LIMIT`, `OZON_SELLERS_DELAY_MS`, `OZON_SELLERS_JITTER_MS`, `OZON_SELLERS_PROGRESS` (`enrich_ozon_sellers.js:8-13`).

Behavior:

- Parses semicolon CSV with BOM handling (`enrich_ozon_sellers.js:129-167`).
- Reconstructs canonical product URL from `raw_json_fragment.action.link` (`enrich_ozon_sellers.js:216-227`).
- Loads product page document, reads `[id^="state-webCurrentSeller"]`, parses `data-state`, recursively finds `sellerId`, and extracts seller name/rating/reviews (`enrich_ozon_sellers.js:243-277`).
- Blocks all non-document resource types during seller enrichment (`enrich_ozon_sellers.js:287-301`).
- Saves progress to `state/ozon_seller_enrichment_progress.json` after every product and resumes successful products (`enrich_ozon_sellers.js:196-214`, `330-338`; `OPERATIONS.md:200-208`).

### `collect_ozon_network.js`

Inputs/configs:

- `OZON_COOKIE_FILE`, fallback `cookie_07.05.26.txt`; `OZON_FIXTURE_DIR`, fallback `fixtures/ozon`; `OZON_SEARCH_URL`, default Ozon search URL; `HEADLESS` (`collect_ozon_network.js:5-9`, `79-97`).

Behavior:

- Captures target endpoint and search-like fetch/xhr responses (`collect_ozon_network.js:104-117`).
- Removes request `cookie`, `authorization`, and `proxy-authorization` headers before writing fixtures (`collect_ozon_network.js:34-44`, `135-147`).
- Writes full response bodies and an HTML snapshot to fixture paths (`collect_ozon_network.js:119-152`, `184-197`).

## Field-Level Contracts

### Common Service Columns

Ozon docs define service columns used where applicable: `run_id`, `component`, `collected_at_utc`, `source_system`, `source_type`, `source_ref`, `status`, `error_message`, with `source_system = ozon` and prototype statuses `success`, `empty`, `error` (`DATA_CONTRACTS.md:13-40`). The Node scripts implement these fields in suggest, products, sellers, and bridge rows (`collect_ozon_suggest.js:227-243`; `collect_ozon_products.js:271-307`; `enrich_ozon_sellers.js:386-435`).

Required market-parser-v2 service fields `schema_version`, `data_quality_status`, and explicit `marketplace` are not present in current Ozon CSV field arrays and must be added during migration (`ARCH_DATA_CONTRACTS_001.md`; source absence confirmed by `collect_ozon_suggest.js:259-349`, `collect_ozon_products.js:19-72`, `enrich_ozon_sellers.js:17-100`).

### Suggest Raw

Path: `data/raw/suggest/{run_id}/suggest_alpha_raw.csv`, latest mirror `data/raw/suggest/latest/suggest_alpha_raw.csv` (`DATA_CONTRACTS.md:42-49`; code writes `rawPath` and latest copy at `collect_ozon_suggest.js:278-280`, `356`).

Fields:

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

Evidence: field array in `collect_ozon_suggest.js:259-275`; same contract in `DATA_CONTRACTS.md:51-81`.

Ozon values:

- `component = suggest`
- `source_type = ozon_search_suggestions_entrypoint`
- `source_ref = typed_query`
- `depth = 0` for seed, `1` for prefix + letter
- `letter = seed` or Russian letter
- `position = 1..5` for accepted suggestions, `0` for empty row
- `list_size = suggestions.length`, max 5

Evidence: constants and row construction in `collect_ozon_suggest.js:14-18`, `224-243`; docs in `DATA_CONTRACTS.md:71-85`.

### Suggest Staging

Path: `data/staging/suggest/{run_id}/suggest_alpha_staging.csv`, latest mirror `data/staging/suggest/latest/suggest_alpha_staging.csv` (`DATA_CONTRACTS.md:87-94`; code at `collect_ozon_suggest.js:279-281`, `357`).

Fields are raw fields plus:

```text
suggestion_lc
is_empty_suggestion
```

Evidence: `collect_ozon_suggest.js:245-249`, `276`; `DATA_CONTRACTS.md:96-116`.

### Filter Top Queries

Path: `data/marts/filter/{run_id}/top_queries.csv`, latest mirror `data/marts/filter/latest/top_queries.csv` (`collect_ozon_suggest.js:350`, `358`; `DATA_CONTRACTS.md:131-139`).

Fields:

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
min_position
source_typed_queries_count
```

Evidence: `collect_ozon_suggest.js:311-349`; `DATA_CONTRACTS.md:140-188`.

Scoring:

```text
score = count * 100 + max(0, 20 - min_position)
selected_reason = ozon_suggest_score
default top_n = 50
```

Evidence: `collect_ozon_suggest.js:302-329`; `UNIFIED_HANDOFF.md:157-178`; `DATA_CONTRACTS.md:182-219`.

### Queries Export

Paths:

```text
data/marts/filter/{run_id}/queries.txt
data/marts/filter/latest/queries.txt
exports/queries.txt
```

Format is one normalized query per line, UTF-8. Evidence: `collect_ozon_suggest.js:351-360`; `DATA_CONTRACTS.md:190-219`.

### Products Raw, Staging, Mart

Raw path: `data/raw/serp/{run_id}/products_raw.csv`, latest mirror `data/raw/serp/latest/products_raw.csv` (`collect_ozon_products.js:468`, `478`; `DATA_CONTRACTS.md:221-228`).

Staging path: `data/staging/serp/{run_id}/products_staging.csv`, latest mirror `data/staging/serp/latest/products_staging.csv` (`collect_ozon_products.js:469`, `479`; `DATA_CONTRACTS.md:301-314`).

Mart path: `data/marts/serp/{run_id}/products_daily.csv`, latest mirror `data/marts/serp/latest/products_daily.csv`, export `exports/products_for_sellers.csv` (`collect_ozon_products.js:470`, `480-482`; `DATA_CONTRACTS.md:316-324`).

Raw/staging fields:

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

Evidence: `collect_ozon_products.js:19-53`; `DATA_CONTRACTS.md:221-299`.

Mart fields are the same minus `raw_json_fragment`. Evidence: `collect_ozon_products.js:55`, `473-476`; `DATA_CONTRACTS.md:316-367`.

Ozon mapping:

- `component = serp`
- `source_type = ozon_search_entrypoint_tilegrid`
- `source_ref = {query}|page={page}`
- `page = Ozon pagination portion`, not a WB 100-item page
- `position_on_page = item index in actual grid.items`
- `absolute_position = sequential collected rank`
- `nmId = String(item.sku || item.id || "")`
- `imtId = String(item.id || item.sku || "")`
- `supplier_id`/`supplier_name` are empty until seller enrichment
- `brand`, product rating, feedbacks, and promo markers are best-effort visual-state values

Evidence: `collect_ozon_products.js:264-307`; docs mapping in `DATA_CONTRACTS.md:268-299`.

Additional non-contracted fields:

- `product_url` and `image_url` are calculated in row objects but are not in `PRODUCT_FIELDS`; they only appear in `products_daily_enriched_preview.csv` with `MART_FIELDS + product_url + image_url` (`collect_ozon_products.js:305-307`, `487-496`).
- Python extractor returns `productId`, `sku`, `title`, `price`, `product_url`, `image_url`, `position`, which is a fixture/test extraction contract, not the full CSV contract (`extractor.py:45-55`; `endpoint_analysis.md:248-268`).

### Pages Raw Index

Path: `data/raw/serp/{run_id}/pages_raw_index.csv`, latest mirror `data/raw/serp/latest/pages_raw_index.csv` (`collect_ozon_products.js:471`, `481`; `DATA_CONTRACTS.md:378-405`).

Fields:

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

Evidence: `collect_ozon_products.js:56-72`, `446-462`.

### Product Preview Export

Path: `exports/products_daily_preview.csv` (`collect_ozon_products.js:484-485`; `OPERATIONS.md:121-134`).

Fields:

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

Evidence: `collect_ozon_products.js:74-92`.

### Sellers Raw And Mart

Raw path: `data/raw/sellers/{run_id}/sellers_raw.csv`, latest mirror `data/raw/sellers/latest/sellers_raw.csv` (`enrich_ozon_sellers.js:437`, `445`; `DATA_CONTRACTS.md:414-455`).

Staging path: `data/staging/sellers/{run_id}/sellers_staging.csv`, latest mirror `data/staging/sellers/latest/sellers_staging.csv` (`enrich_ozon_sellers.js:438`, `446`).

Mart path: `data/marts/sellers/{run_id}/sellers_daily.csv`, latest mirror `data/marts/sellers/latest/sellers_daily.csv` (`enrich_ozon_sellers.js:439`, `447`; `DATA_CONTRACTS.md:490-511`).

Raw/staging fields:

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

Evidence: `enrich_ozon_sellers.js:53-83`; `DATA_CONTRACTS.md:423-488`.

Mart fields are the same minus `raw_json_fragment`. Evidence: `enrich_ozon_sellers.js:84`, `417-444`; `DATA_CONTRACTS.md:490-505`.

Ozon mapping:

- `component = sellers`
- `source_type = ozon_product_current_seller_state`
- `source_ref = seller:{supplier_id}`
- `supplier_id = Ozon sellerId from product card state`
- `supplier_name = seller title from product card state`
- `rating` and `feedbacks_count` are best-effort from seller state
- `queries_ref`, `query_groups_ref`, `nm_ids_ref`, and `source_product_run_ids` are pipe-separated aggregates

Evidence: `enrich_ozon_sellers.js:386-416`; `DATA_CONTRACTS.md:457-488`.

### Seller-Query-Product Bridge

Path: `data/marts/sellers/{run_id}/seller_query_product_bridge.csv`, latest mirror `data/marts/sellers/latest/seller_query_product_bridge.csv` (`enrich_ozon_sellers.js:440`, `448`; `DATA_CONTRACTS.md:513-554`).

Fields:

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

Evidence: `enrich_ozon_sellers.js:85-100`, `418-435`; `DATA_CONTRACTS.md:522-548`.

Mapping:

- `source_type = seller_query_product_bridge`
- `source_ref = {supplier_id}|{nmId}|{query}`
- `nmId = Ozon product id`
- `product_run_id = source SERP run_id`

Evidence: `enrich_ozon_sellers.js:421-435`; `DATA_CONTRACTS.md:541-548`.

## Extractor Behavior

### Suggest Extractor

`ozon_parser/suggest_extractor.py`:

- Accepts either a raw response or wrapper with `response_body` (`suggest_extractor.py:16-18`).
- Requires object `widgetStates`; returns empty list otherwise (`suggest_extractor.py:21-25`).
- Processes only keys starting with `webSuggestions` (`suggest_extractor.py:27-33`).
- Parses widget state if it is a JSON string (`suggest_extractor.py:49-55`).
- Reads `items[:5]`, extracts `cellItem.centerBlock.title.text`, normalizes spaces, dedupes lowercase with `ё -> е`, and preserves first spelling (`suggest_extractor.py:35-46`, `58-71`).

### Product Extractor

`ozon_parser/extractor.py`:

- Accepts fixture wrapper with `response_body` or direct body (`extractor.py:18-21`).
- Iterates widget states and yields grids when key starts with `tileGrid` or items look product-like (`extractor.py:60-74`).
- Parses JSON-string widget states (`extractor.py:76-82`).
- Extracts `sku`, `productId`, title, product URL, image URL, price, and absolute-like `position` (`extractor.py:35-55`).
- Canonicalizes product URLs to absolute Ozon URL without query string (`extractor.py:133-140`).
- Position uses `grid.page`, actual `len(items)`, and item index (`extractor.py:29-30`, `174-177`).

## Browser Flow And Extraction Rules

### Suggest

Endpoint:

```text
GET https://www.ozon.ru/api/entrypoint-api.bx/page/json/v2?url=<encoded /searchSuggestions/search/?text=<typed_query>&from_global=true>&__rr=1
```

Evidence: `collect_ozon_suggest.js:103-105`; `ENDPOINTS_AND_EXTRACTION.md:23-80`; `endpoint_analysis.md:116-165`.

Extraction:

- Parse `response_body.widgetStates["webSuggestions-*"]`.
- Parse widget state value as JSON when it is a string.
- Read `items[].cellItem.centerBlock.title.text`.
- Accept only first 5 items.

Evidence: `collect_ozon_suggest.js:108-135`; `ENDPOINTS_AND_EXTRACTION.md:43-68`.

Limitation: code does not check `action.link starts with /search/`; docs recommend combining that check with `position <= 5` if Ozon begins returning non-query entries in first positions (`OPERATIONS.md:298-306`).

### SERP/Products

Flow:

- Public URL is `https://www.ozon.ru/search/?text=<query>`.
- Ozon may redirect to predicted category pages.
- Page 1 product grid can be embedded in initial HTML `state-tileGridDesktop*`.
- Page 2+ comes from `/api/entrypoint-api.bx/page/json/v2?url=<encoded nextPage>`.
- `nextPage`, `paginator_token`, `search_page_state`, and `start_page_id` are opaque.

Evidence: `collect_ozon_products.js:350-417`; `ENDPOINTS_AND_EXTRACTION.md:81-159`; `endpoint_analysis.md:42-115`.

Extraction:

- Product ids: `item.sku || item.id`.
- Product URL: `item.action.link`, canonicalized.
- Title: `mainState[]` where `id == "name"` then first `textAtom`.
- Price: `mainState[].priceV2.price[]`; `PRICE` or `SALE_PRICE` is current, `ORIGINAL_PRICE` is original.
- Image: `tileImage.items[].image.link`.
- Rating/feedbacks: `mainState[].labelListV2` with `testInfo.automatizationId == "tile-list-rating"`.
- Brand: best-effort from labels before title.

Evidence: `collect_ozon_products.js:152-241`, `264-307`; `ENDPOINTS_AND_EXTRACTION.md:160-234`.

### Sellers

Flow:

- SERP tileGrid has no seller data.
- Product URL is derived from tile `action.link`.
- Product-card initial HTML contains `state-webCurrentSeller-*`.
- Seller enrichment loads only the document and blocks scripts, XHR, images, media, fonts, and CSS.
- Seller id is found recursively by key `sellerId`; seller name is read from `sellerCell.centerBlock.title.text`.

Evidence: `enrich_ozon_sellers.js:216-227`, `243-277`, `287-309`; `ENDPOINTS_AND_EXTRACTION.md:231-325`; `endpoint_analysis.md:270-296`.

## Test Inventory

- `tests/test_ozon_extractor.py::test_extracts_products_from_entrypoint_fixture` proves extractor can read a captured entrypoint fixture, expects 8 products, first `productId`/`sku` `3450635382`, expected title, price text, canonical product URL, image URL, and position `9` (`test_ozon_extractor.py:14-29`).
- `tests/test_ozon_extractor.py::test_ignores_non_product_widget_states` proves non-product widget states are ignored (`test_ozon_extractor.py:30-36`).
- `tests/test_ozon_suggest_extractor.py::test_extracts_web_suggestions` proves only first 5 suggestion items are returned and sixth advertising/store-like item is excluded (`test_ozon_suggest_extractor.py:15-80`).
- `tests/test_ozon_suggest_extractor.py::test_dedupes_case_and_yo` proves duplicate detection folds case and `ё`/`е` (`test_ozon_suggest_extractor.py:82-91`).
- `tests/test_ozon_suggest_extractor.py::test_extracts_from_captured_fixture_when_present` is optional: it skips if captured fixture is absent and expects fixture suggestions include `шеврон` and at least 5 suggestions (`test_ozon_suggest_extractor.py:93-101`).

Tests were not executed because task testing requirements are `none`, and fixture/raw data paths are outside ALLOWED_SOURCES for this research. Documentation claims current tests are `5 OK`, but this was not independently verified (`OPERATIONS.md:248-256`).

## Docs vs Code Mismatches And Limitations

- Code hardcodes a local cookie fallback `cookie_07.05.26.txt` in all browser scripts, while docs state this is local test input and final implementation must not hardcode it (`collect_ozon_suggest.js:6`; `collect_ozon_products.js:6`; `enrich_ozon_sellers.js:6`; `collect_ozon_network.js:6`; `UNIFIED_HANDOFF.md:318`; `ENDPOINTS_AND_EXTRACTION.md:15-21`).
- `collect_ozon_products.js` uses observed page size `8` when defaulting `OZON_SERP_PAGES` from `OZON_SERP_PRODUCTS`, although docs say final code must not rely on fixed page size and should use actual `items.length` (`collect_ozon_products.js:9-12`; `ENDPOINTS_AND_EXTRACTION.md:343-353`). The collector does compute positions and counts from actual items once pages are collected (`collect_ozon_products.js:264-309`, `423-445`).
- Suggest code enforces only `items.slice(0, 5)` and does not check `action.link starts with /search/`; docs identify that extra check as a possible production rule (`collect_ozon_suggest.js:124-132`; `OPERATIONS.md:298-306`).
- Python extractors expose a minimal fixture extraction shape (`productId`, `sku`, `title`, `price`, `product_url`, `image_url`, `position`) that differs from the Node CSV product contract (`extractor.py:45-55`; `collect_ozon_products.js:19-53`). Use Python fields as test extractor behavior, not mart contract.
- Docs claim verified latest state of 1000 product rows, 125 pages, 120 sellers, and 1000 bridge rows (`UNIFIED_HANDOFF.md:92-128`; `DATA_CONTRACTS.md:369-376`, `507-554`; `OPERATIONS.md:136-149`, `248-256`). These claims were not revalidated from output data because data/raw/marts/fixtures were not in ALLOWED_SOURCES.
- `collect_ozon_network.js` sanitizes request headers but writes full response bodies and HTML snapshot (`collect_ozon_network.js:34-44`, `135-152`, `184-197`). Docs also list `userInfo` and `userToken` as observed response keys (`endpoint_analysis.md:167-193`). This creates a fixture/raw response sanitization requirement not fully proven by current code.

## WB-Shaped Compatibility Assumptions

- `nmId` is a WB column name reused for Ozon product id/sku compatibility. It must be treated as `external_product_id` with `source_system=ozon`, not as WB nmId (`DATA_CONTRACTS.md:268-280`, `541-548`, `556-574`; `UNIFIED_HANDOFF.md:332-345`).
- `supplier_id` is reused for Ozon `sellerId`; it is provider-local and not semantically identical to WB supplier id (`enrich_ozon_sellers.js:260-274`; `DATA_CONTRACTS.md:457-474`, `556-574`; `UNIFIED_HANDOFF.md:332-345`).
- Ozon `page` is an Ozon pagination portion, not a WB 100-item page. Analytics should compare `absolute_position`/visibility buckets, not provider page numbers (`DATA_CONTRACTS.md:276-279`; `UNIFIED_HANDOFF.md:189-209`).
- CSV encoding/delimiter compatibility is UTF-8 with BOM and `;` delimiter (`collect_ozon_suggest.js:84-91`; `collect_ozon_products.js:138-145`; `enrich_ozon_sellers.js:175-180`; `DATA_CONTRACTS.md:5-11`).

## Missing Runtime Infrastructure For market-parser-v2

Current Ozon prototype lacks the following market-parser-v2 infrastructure:

- provider-aware CLI and component runner;
- shared config YAML/provider config;
- StateDB/checkpoints for suggest and SERP;
- seller checkpointing beyond JSON progress file;
- run reports;
- run lock;
- contract validation;
- schema versioning;
- data quality status model;
- latest/export manifest/checksums/bundle;
- Web UI control;
- partial/failure status semantics beyond `success`, `empty`, `error`.

Evidence: source scripts are standalone Node entrypoints (`package.json:6-10`); docs list prototype limitations and final checklist (`UNIFIED_HANDOFF.md:320-334`; `OPERATIONS.md:314-333`). Architecture requires these capabilities for market-parser-v2 (`ARCH_MARKET_PARSER_V2_001.md`, `ARCH_DATA_CONTRACTS_001.md`).

## Risks

- Cookie handling risk: scripts can fall back to a local cookie filename. Final implementation must require env/external secret path and must not log or commit cookie values (`collect_ozon_suggest.js:6`, `141-143`; `ENDPOINTS_AND_EXTRACTION.md:7-21`; `ARCH_SECURITY_CONSTRAINTS_001.md`).
- Fixture/raw response risk: network capture removes sensitive request headers, but response bodies and HTML snapshots may include account/session state. Sanitization must inspect response payloads before fixtures/raw archives enter Git or export bundles (`collect_ozon_network.js:34-44`, `135-152`, `184-197`; `endpoint_analysis.md:167-193`; `ARCH_SECURITY_CONSTRAINTS_001.md`).
- Anti-bot/empty response risk: Ozon requires fresh cookies, browser context, throttling, and conservative seller resource loading. Empty pages should become clear partial/failure statuses, not silently valid data (`ENDPOINTS_AND_EXTRACTION.md:308-353`; `OPERATIONS.md:284-313`; `ARCH_DATA_CONTRACTS_001.md`).
- Frontend contract drift risk: widget key prefixes and visual state paths can change. Code uses prefix matching, but final implementation needs fixture/contract tests and explicit failure modes (`ENDPOINTS_AND_EXTRACTION.md:343-353`; `extractor.py:60-82`; `suggest_extractor.py:27-55`).
- Product URL/image contract gap: code can derive product URL/image, Python tests verify them, but mart CSVs do not expose them except enriched preview. Design must decide whether they belong in provider mart/export contract (`collect_ozon_products.js:305-307`, `487-496`; `extractor.py:45-55`).

## Unresolved Findings

- Exact current output row counts and latest CSV contents were not verified because `data/`, `exports/`, and `fixtures/` were outside ALLOWED_SOURCES. Use documentation claims as historical prototype claims, not fresh evidence.
- Exact Ozon raw response sensitivity is unresolved because raw fixtures/HAR/private data were not read. Treat all response bodies and HTML snapshots as potentially sensitive until sanitized.
- Exact stability of Ozon endpoint/widget shapes as of 2026-05-17 is unresolved because live scraping was forbidden. Future implementation must validate with controlled, audited runs.
- Final common contract field names for Ozon `external_product_id`, `external_seller_id`, product URL, image URL, `schema_version`, and `data_quality_status` require migration design/contract decisions. The source prototype currently uses WB-shaped compatibility names.

## Design And Task Implications

- Implement Ozon behind provider-aware components, not by copying standalone scripts as permanent architecture.
- Normalize WB-shaped Ozon columns into provider-aware contract fields while preserving compatibility only where explicitly required.
- Treat browser/cookie/session behavior as provider-specific runtime infrastructure with configurable throttle/concurrency and document-only seller enrichment.
- Add contract validators before analytics export: service fields, provider identity, duplicate positions, missing seller id, unsupported schema_version, unexpected columns, and partial/empty run statuses.
- Add sanitization gates for any Ozon fixtures/raw response archives and exclude cookies, browser profiles, HAR, raw private data, and unsanitized response snapshots from Git/export.
- Use `nextPage` as the only pagination continuation source and keep pagination tokens opaque.
- For analytics, use `absolute_position` and top-N/visibility metrics, not Ozon page numbers.

## Secret Exposure Check

Search was limited to the allowed Ozon source files. Findings:

- No literal cookie values, passwords, API keys, or authorization header values were found in allowed source text.
- Allowed code references cookie file paths and parses cookie headers (`collect_ozon_suggest.js:6`, `141-143`; `collect_ozon_products.js:6`, `313-314`; `enrich_ozon_sellers.js:6`, `296`; `collect_ozon_network.js:6`, `73-76`).
- `collect_ozon_network.js` explicitly removes request `cookie`, `authorization`, and `proxy-authorization` headers before writing fixtures (`collect_ozon_network.js:34-44`, `142`).
- Fixture/raw body sanitization remains a risk because scripts write full response bodies/HTML snapshots and docs mention response keys such as `userInfo`/`userToken` (`collect_ozon_network.js:135-152`, `184-197`; `endpoint_analysis.md:167-193`).

## Evidence Matrix

| Research question | Finding | Evidence | Confidence | Limitation |
|---|---|---|---|---|
| Exact Ozon suggest fields | Raw/staging/filter/query export fields listed above. | `collect_ozon_suggest.js:259-360`; `DATA_CONTRACTS.md:42-219` | maximum | Output samples not read. |
| Exact products/SERP fields | Raw/staging/mart/pages/preview fields listed above. | `collect_ozon_products.js:19-92`, `468-496`; `DATA_CONTRACTS.md:221-412` | maximum | Latest row counts are docs-only. |
| Exact seller and bridge fields | Sellers raw/mart and bridge fields listed above. | `enrich_ozon_sellers.js:53-100`, `386-448`; `DATA_CONTRACTS.md:414-554` | maximum | Raw seller state samples not read. |
| Scripts and configs | Four npm scripts and env/config inputs inventoried. | `package.json:6-17`; script constants cited above; `OPERATIONS.md:44-208` | maximum | Did not execute scripts. |
| Suggest extraction | `webSuggestions*`, first 5 items, normalized/deduped. | `collect_ozon_suggest.js:108-135`; `suggest_extractor.py:16-46`; tests `15-91` | maximum | No action.link check in code. |
| SERP extraction | Initial HTML tileGrid plus entrypoint `nextPage`; tile paths and absolute positions. | `collect_ozon_products.js:252-417`; `extractor.py:18-57`; `ENDPOINTS_AND_EXTRACTION.md:81-234` | maximum | Live endpoint freshness not checked. |
| Seller extraction | Product-card `state-webCurrentSeller*`, document-only loading, recursive sellerId. | `enrich_ozon_sellers.js:243-309`; `ENDPOINTS_AND_EXTRACTION.md:235-325` | maximum | Seller state samples not read. |
| Tests | Five test behaviors inventoried; tests not run. | `test_ozon_extractor.py:14-36`; `test_ozon_suggest_extractor.py:15-101`; `OPERATIONS.md:248-256` | high | Fixture files not allowed. |
| WB-shaped assumptions | `nmId`/`supplier_id` are compatibility-only provider-local ids. | `DATA_CONTRACTS.md:556-574`; `UNIFIED_HANDOFF.md:332-345` | maximum | Final contract mapping pending. |
| Missing runtime infrastructure | No shared state, reports, locks, validation, provider CLI, export bundle. | `UNIFIED_HANDOFF.md:320-334`; `OPERATIONS.md:314-333`; script structure | maximum | WB implementation details not read in this task. |
| Security/anti-bot risks | Cookie env/path required; response body sanitization and anti-bot partial status needed. | `ENDPOINTS_AND_EXTRACTION.md:7-21`, `308-353`; `collect_ozon_network.js:34-44`, `135-152`; `ARCH_SECURITY_CONSTRAINTS_001.md` | high | Raw fixtures not inspected. |

