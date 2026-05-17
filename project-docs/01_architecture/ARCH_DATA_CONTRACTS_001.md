# ARCH_DATA_CONTRACTS_001

## Artifact Type

Architecture document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md`

Source-contract updates use only audited research RESULTS. No source project
files were inspected for this design continuation.

## Purpose

Define the cross-provider data contract boundaries for parser marts and analytics import.

## Contract Status

This contract is finalized for bounded provider migration where audited
source-contract evidence is sufficient.

Provider-specific source field evidence, compatibility mappings, unresolved
findings, and migration constraints are bounded in:

```text
project-docs/01_architecture/ARCH_PROVIDER_SOURCE_CONTRACTS_001.md
```

The contract remains intentionally incomplete for business formulas,
management thresholds, and unsupported source facts.

## Mandatory Service Fields

Use these fields where applicable to the entity:

```text
run_id
component
collected_at_utc
source_system
source_type
source_ref
status
error_message
schema_version
```

Provider identity:

```text
source_system = wb
source_system = ozon
```

## Identifier Rules

Provider identifiers are scoped by marketplace/source system.

Universal keys:

```text
source_system + external_product_id
source_system + external_seller_id
source_system + query
```

WB `nmId` and Ozon product identifiers must not be joined without provider context.

Provider compatibility mapping:

```text
WB nmId -> external_product_id
Ozon compatibility nmId -> external_product_id
WB supplier_id -> external_seller_id
Ozon compatibility supplier_id -> external_seller_id
supplier_name -> seller_name
```

Ozon compatibility `nmId` is not a WB `nmId`.

## Query Contract

Expected query analytics fields:

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

Fields that depend on future implementation or facts still unresolved by the
audited research results may be nullable or omitted from provider-specific
files until a bounded follow-up task resolves them.

## Product/SERP Contract

Expected product mart fields:

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

`absolute_position` is required for cross-provider analytics. Provider page number must not be treated as a directly comparable metric across WB and Ozon.

## Seller Contract

Expected seller mart fields:

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

Ozon seller fields are best-effort because the TZ states that Ozon SERP tileGrid does not contain seller data and seller enrichment requires product-card HTML state.

## Seller-Query-Product Bridge

Required bridge fields:

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

## CSV Compatibility

Where CSV compatibility with WB is required:

```text
encoding = utf-8-sig
delimiter = ;
```

Provider-specific raw/staging outputs may have different internal formats if normalized marts and export bundles satisfy the accepted contract.

## Schema Versioning

Every exported contract file must carry `schema_version`. Analytics import must reject or quarantine unsupported schema versions.

Audited research confirms inspected source output arrays do not fully prove
`schema_version` and `marketplace` in existing source outputs. They are V2
required additions, not source-derived facts.

## Required Validation

Validators must detect at least:

- missing mandatory fields;
- unexpected CSV columns where strict mode applies;
- schema version mismatch;
- duplicate product positions;
- missing seller id when seller data is expected;
- invalid provider identity;
- invalid or absent `run_id`.

## Required Follow-Up

- audit this design continuation before provider migration dispatch;
- implement common parser contract/export/data-quality enforcement before provider migration completion;
- keep owner formula and threshold decisions in non-dispatchable proposal scope.
