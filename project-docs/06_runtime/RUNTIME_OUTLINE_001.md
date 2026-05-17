# RUNTIME_OUTLINE_001

## Artifact Type

Runtime design document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_WB_SOURCE_CONTRACTS_001.md`
- audited research result `project-runtime/agent-results/TASK_RESEARCH_OZON_SOURCE_CONTRACTS_001.md`

Source-contract updates use only audited research RESULTS. No source project
files were inspected for this design continuation.

## Purpose

Define the initial runtime outline for local and target operation of `market-parser-v2` and `market-analytics`.

## Temporary No-Domain Mode

Recommended ports from the TZ:

```text
market-parser-v2 web panel:  8092
market-parser-v2 MCP/debug:  8095, only if needed and protected
market-parser-v2 export/API: 8096
market-analytics web/API:    8090
```

Example access:

```text
http://SERVER_IP:8092
http://SERVER_IP:8096/analytics-export/latest.json
http://SERVER_IP:8090
```

## Target Mode

Target access:

```text
Internet
  -> Nginx 80/443
    -> 127.0.0.1:8092 parser web
    -> 127.0.0.1:8096 parser export
    -> 127.0.0.1:8090 analytics web/API
```

Future domain examples:

```text
https://parser.domain.ru
https://analytics.domain.ru
```

## Required Runtime Controls

Runtime implementation must include:

- HTTPS in target mode;
- HTTP to HTTPS redirect;
- authorization for web panels;
- replaced default passwords;
- restricted debug endpoints;
- read-only export endpoint;
- access logs;
- error logs;
- backup/restore for configs and data;
- data-retention policy.

## Process Boundary

The TZ recommends `systemd` and Nginx in target mode. Service files and deployment hardening are future implementation tasks after skeletons exist.

## Runtime Data Boundary

Runtime paths must separate:

- source code;
- parser data;
- analytics database files or database service storage;
- logs;
- secrets;
- cookies;
- raw archives;
- temporary files.

These non-code assets must not be committed.

## Ozon Runtime Boundary

Ozon runs require browser/Chromium behavior and cookie handling. Cookie path must be environment/path based and must not be logged or exported.

Concurrency and throttle must be configurable.

Ozon provider migration must add shared V2 runtime infrastructure that the
audited source-contract result reports as missing from the prototype: provider
aware CLI, state/checkpoints, run reports, locks, validation, schema version,
data-quality status, export bundle integration, and Web UI integration.

Seller enrichment must support progress/resume because product-card visits are
slow and block-sensitive.

## WB Runtime Boundary

WB provider migration may reuse the audited operational pattern of staged
components, run reports, checkpoints, latest mirrors, and CSV compatibility,
but common V2 runtime output must normalize provider identity to `wb` and must
not preserve source defaults that conflict with the TZ.
