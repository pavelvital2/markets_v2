# ARCH_EXPORT_CONTRACT_001

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

Define the stable parser-to-analytics export contract.

## Production Rule

`market-analytics` must not read parser internal folders directly in production mode. The stable integration boundary is the parser export bundle.

## Export Layout

Required layout:

```text
market-parser-v2 analytics export:
  latest.json
  {marketplace}/{run_id}/manifest.json
  {marketplace}/{run_id}/bundle.tar.gz
  {marketplace}/{run_id}/checksums.sha256
```

## Manifest Minimum Fields

`manifest.json` must contain at least:

```text
marketplace
source_system
run_id
schema_version
export_created_at_utc
component_statuses
file_list
row_counts
checksums
data_quality_summary
usable_for_reports
warnings
errors
```

## Bundle Contents

The bundle must contain only files needed by analytics:

- normalized query marts;
- normalized product/SERP marts;
- normalized seller marts;
- seller-query-product bridge;
- data-quality summary;
- any contract metadata required for import validation.

Recommended stable bundle paths:

```text
marts/queries.csv
marts/products.csv
marts/sellers.csv
marts/seller_query_product_bridge.csv
quality/data_quality_summary.json
metadata/contract.json
```

Provider-specific raw/staging outputs are parser internals and are excluded
from the analytics bundle unless a separate sanitized fixture/export contract
is accepted.

## Forbidden Bundle Contents

The bundle must not include:

- cookies;
- API keys;
- auth tokens;
- raw sensitive fixtures;
- unsanitized HAR files;
- browser profiles;
- working logs;
- secrets;
- temporary files not required by analytics.
- raw JSON fragments or raw HTML snapshots that may contain sensitive state.

## Checksums

`checksums.sha256` must cover every file that analytics imports from the bundle. Analytics must verify checksums before accepting an import.

## Latest Pointer

`latest.json` is a pointer and summary for convenience. It must not erase run history and must not be the only import registry in analytics.

## Partial Data

Partial data is allowed only with explicit manifest status, component statuses, warnings, and data-quality summary. Analytics must surface partial-data warnings to users.

Manifest status and data-quality summary must preserve provider and component
partial/failure evidence. Ozon anti-bot, empty page, missing page, and blocked
seller enrichment behavior must not be silently converted to success.

## Import Failure Rule

Analytics must reject or quarantine bundles when:

- manifest is missing;
- checksum validation fails;
- schema version is unsupported;
- provider identity is invalid;
- required marts are absent for a run marked usable;
- secret-like files are present in the bundle.
