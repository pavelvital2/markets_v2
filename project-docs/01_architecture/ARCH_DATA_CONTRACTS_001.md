# ARCH_DATA_CONTRACTS_001

## Artifact Type

Architecture document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`

No source project files were inspected for this document.

## Purpose

Define the initial cross-provider data contract boundaries for parser marts and analytics import.

## Contract Status

This is an initial architecture contract. It is sufficient for skeletons, validators, and schema-version placeholders.

It is not sufficient for final provider migration because exact WB/Ozon source fields, sample outputs, and optionality were not available in the allowed read set. Those facts require audited research dependencies.

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

Fields that depend on source confirmation or future implementation may be nullable or omitted from provider-specific files until contract research resolves them.

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

- WB field-level contract research.
- Ozon field-level contract research.
- Design continuation after both source contract research tasks pass audit.

