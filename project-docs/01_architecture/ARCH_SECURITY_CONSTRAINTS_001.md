# ARCH_SECURITY_CONSTRAINTS_001

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

Define security and data-separation constraints for `market-parser-v2` and `market-analytics`.

## Secret Handling

Forbidden:

- committing cookies;
- committing API keys;
- committing auth tokens;
- saving HAR/fixtures with secrets;
- logging cookies or tokens;
- exposing secrets through UI;
- exposing secrets through export bundles.

Secrets must be configured through environment variables or external secret files outside Git.

For Ozon cookies, the TZ allows a path such as:

```text
OZON_COOKIE_FILE
```

The file content must not be logged, committed, included in fixtures, or shown in UI.

Audited Ozon research reports a current prototype risk around env/path cookie
handling and a local fallback cookie path. V2 must not hardcode cookie paths.

## Data Separation

These categories must remain separate:

- code;
- data;
- logs;
- cookies;
- secrets;
- raw archives;
- temporary files.

Data, logs, cookies, secrets, raw archives, and temporary files must not enter Git.

## Export Safety

The parser export bundle must be sanitized and must contain only analytics-required files. It must not contain cookies, tokens, raw sensitive fixtures, browser profiles, working logs, or unsanitized HAR files.

Raw response bodies, raw HTML snapshots, raw JSON fragments, HAR files, and
fixtures are not safe for Git or analytics export until a sanitizer has removed
secret-like request/response state and the resulting artifact is explicitly
classified as sanitized.

## Identifier Safety

WB and Ozon identifiers must not be mixed without provider context. Cross-provider joins require `marketplace` or `source_system`.

## Financial Claims

The system must not present unconfirmed financial metrics as facts. Exact profit, margin, factual revenue, competitor sales, ad efficiency, conversion, cost price, and supply economics require confirmed future sources.

## Web Access

Web panels must have authorization. Default passwords must be replaced. Debug endpoints must not be externally exposed unless explicitly required and protected.

The parser export endpoint must be read-only.

## Production Edge

Target production access should use Nginx on 80/443 with HTTPS and reverse proxy to localhost service ports.

Direct external service ports should be closed in target mode except 80/443.

## Backup and Retention

Architecture must include backup/restore policy and data-retention policy before production hardening.
