# RUNTIME_OUTLINE_001

## Artifact Type

Runtime design document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`

No source project files were inspected for this document.

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

