# ARCH_PROVIDER_SOURCE_CONTRACTS_001

## Artifact Type

Architecture document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- `project-docs/01_architecture/ARCH_MARKET_PARSER_V2_001.md`
- `project-docs/01_architecture/ARCH_DATA_CONTRACTS_001.md`
- `project-docs/01_architecture/ARCH_EXPORT_CONTRACT_001.md`
- `project-docs/01_architecture/ARCH_DATA_QUALITY_MODEL_001.md`
- `project-docs/01_architecture/ARCH_SECURITY_CONSTRAINTS_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md`

No source project files were inspected for this design continuation. Provider
facts in this document are taken only from the audited research RESULTS listed
above.

## Purpose

Finalize the bounded provider source-contract design for WB and Ozon migration
into `market-parser-v2`.

## Evidence Boundary

The audited WB result confirms source fields, component behavior, state/report
behavior, CSV compatibility, and migration risks for the allowed WB sources.

The audited Ozon result confirms source fields, extraction rules, script/config
inventory, tests, missing runtime infrastructure, and security/migration risks
for the allowed Ozon sources.

Unresolved formulas, owner thresholds, current live marketplace behavior, exact
generated CSV samples, and source internals outside audited results remain
non-contract facts.

## Required V2 Additions

Both providers must emit common normalized marts with:

```text
marketplace
source_system
run_id
schema_version
data_quality_status
```

These are V2 contract requirements even where source outputs did not contain
all of them.

Accepted provider identities:

```text
source_system = wb
source_system = ozon
```

WB research confirms V1 default `source_system` is `wildberries`; V2 must
normalize it to `wb`.

## Common Query Contract

The normalized query mart must preserve service fields and query fields from
source suggest/filter behavior:

```text
marketplace
source_system
run_id
query
normalized_query
canonical_query
query_group
source_query
rank
score
hybrid_score
wordstat_volume
count
selected_reason
data_quality_status
schema_version
```

If a provider cannot confirm or compute a field from audited facts, the field
must be nullable or omitted from provider-specific raw/staging files but must
not be filled with invented values.

Audited WB and Ozon results both confirm suggest raw rows with:

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

Audited WB and Ozon results both confirm suggest staging adds:

```text
suggestion_lc
is_empty_suggestion
```

Ozon-specific query generation must keep only the first 5 dropdown suggestions
from `webSuggestions*` extraction and preserve dedupe behavior confirmed by
the audited result.

## Common Product/SERP Contract

The normalized product/SERP mart must use provider-neutral identifiers:

```text
marketplace
source_system
run_id
query
query_group
page
position_on_page
absolute_position
external_product_id
product_name
brand
external_seller_id
seller_name
final_price
price
old_price
sale_price
rating
reviews_count
feedbacks
promo_markers
raw_file
raw_page_path
data_quality_status
schema_version
```

WB `nmId` maps to `external_product_id`.

Ozon compatibility `nmId` maps to `external_product_id` but must be documented
as an Ozon product id/sku compatibility field, not as a WB identifier.

WB `supplier_id` and Ozon compatibility `supplier_id` map to
`external_seller_id` under provider context.

Ozon pagination state is opaque. V2 must use `nextPage` as opaque state where
needed, must not synthesize Ozon pagination tokens, and must calculate
`absolute_position` from observed item order. Ozon page size must be based on
actual `items.length`, not a permanent constant.

## Common Seller Contract

The normalized seller mart must use:

```text
marketplace
source_system
run_id
external_seller_id
seller_name
seller_rating
seller_reviews
feedbacks_count
product_count
query_count
queries_ref
query_groups_ref
external_product_ids_ref
source_product_run_ids
data_quality_status
schema_version
```

Ozon seller enrichment is best-effort because audited evidence confirms Ozon
SERP tileGrid does not contain seller data. Seller fields must come from
product-card HTML state enrichment and may be partial when enrichment is
blocked or missing.

## Seller-Query-Product Bridge

The bridge contract is:

```text
marketplace
source_system
run_id
query
query_group
external_product_id
external_seller_id
seller_name
product_run_id
schema_version
data_quality_status
```

Audited WB and Ozon research both confirm source bridge behavior that links
query, query group, product id, seller id/name, and source product run.

## WB Migration Contract

WB migration must preserve the audited staged pipeline:

```text
suggest -> filter -> serp -> sellers -> export
```

Required migration behavior:

- write provider-specific raw/staging rows and common normalized marts;
- preserve run-scoped outputs, latest mirrors, run reports, checkpoints, and
  status/error reporting;
- keep CSV compatibility where required: `utf-8-sig` and `;`;
- normalize `wildberries` source identity to `wb`;
- add V2-only `marketplace`, `schema_version`, provider-neutral ids, and
  `data_quality_status`;
- keep WB-specific names such as `nmId` and `supplier_id` out of common joins
  unless provider context is present.

WB unresolved findings from the audited result:

- exact test files, fixtures, assertions, and behavior coverage;
- exact SQLite schema columns;
- exact config validation schema and default config values;
- exact generated CSV headers/samples;
- exact `run_report.py` latest/duration behavior outside runner/sample
  evidence.

These unresolved findings do not authorize guessing. If implementation needs
one of them as a hard requirement, it must stop with a research dependency or
gap.

## Ozon Migration Contract

Ozon migration must preserve source-derived extraction rules while moving them
behind V2 provider interfaces:

- Chromium/browser session for suggest/products where required;
- `webSuggestions*` extraction for suggest;
- first 5 dropdown suggestions only;
- `tileGrid*` or product-like widget state extraction for products;
- opaque `nextPage` handling for pagination;
- sequential `absolute_position`;
- product-card `state-webCurrentSeller*` seller enrichment;
- document-only seller page loading with non-document resources blocked;
- progress/resume support for seller enrichment;
- configurable throttle/concurrency;
- explicit partial/failure status for anti-bot, empty pages, missing pages, or
  blocked enrichment.

Ozon must not remain a standalone script-only integration. The audited result
confirms missing V2 runtime infrastructure: provider-aware CLI, shared state
and checkpoints, run reports, locks, config YAML, validation,
`schema_version`, `data_quality_status`, export bundle, and Web UI integration.

Ozon unresolved findings from the audited result:

- current latest output row counts and CSV contents are documentation-only
  claims;
- exact sensitivity of raw response bodies and HTML snapshots;
- current live Ozon endpoint/widget shape as of 2026-05-17;
- final normalized field names for optional URL/image/product-id variants
  beyond the common aliases above.

These unresolved findings must remain limitations unless a bounded audited
research dependency resolves them.

## Export Implications

The analytics export bundle must include common normalized marts, bridge,
manifest, checksums, and data-quality summary. It must not include cookies,
tokens, browser profiles, unsanitized HAR files, raw sensitive response bodies,
HTML snapshots, or raw JSON fragments unless a separate sanitized fixture
contract is accepted.

## Data Quality Implications

Provider migration must map source row statuses into V2 run/component/row
quality status without hiding partial data.

Confirmed source statuses include `success`, `empty`, `error`, `dry_run`, and
WB run/report statuses including `success`, `partial`, `failed`, and
`not_ready`.

V2 user-facing usability statuses remain:

```text
valid_for_reports
partial_use_with_warning
invalid_for_reports
```

The numeric or categorical formula for `data_confidence_level` is not defined
by audited source-contract research and remains an owner/design gap.

## Security Implications

Ozon cookie configuration must use environment/path based configuration such as
`OZON_COOKIE_FILE`; hardcoded local cookie fallbacks are forbidden in V2.

Raw response bodies, raw HTML snapshots, HAR files, and fixtures must pass a
sanitization gate before they can be committed, exported, or used as shared
test fixtures.

Provider identifiers are security-relevant data boundaries: WB and Ozon ids
must never be joined or compared without `marketplace` or `source_system`.

## Owner Gaps

The source-contract research is sufficient for provider data/export/quality
migration tasks, but not for business formulas or thresholds:

- `visibility_score`;
- `competition_score`;
- `opportunity_score`;
- `price_index`;
- `data_confidence_level`;
- default thresholds for score-based recommendations;
- owner-facing policy for which partial data states may be used in reports.

These decisions remain non-dispatchable owner/design proposal scope and must
not be implemented as factual recommendations during provider migration.
