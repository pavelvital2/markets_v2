# AGENT RESULT

## STATUS

```text
fail
```

## ROLE

```text
auditor
```

## TASK

```text
TASK_AUDIT_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001
```

## SUMMARY

```text
Corrected downstream task packets are schema-valid and dispatchable. Audit failed because the stored correction RESULT was missing required AGENT_RESULT_TEMPLATE fields: READ_DOCS, READ_INPUTS, CREATED_FILES, and DELETED_FILES.
```

## EVIDENCE

```text
TASK_PACKET_SCHEMA_STATUS: passed
EVIDENCE_STATUS: failed
VALIDATED_TASK_PACKETS: project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md passed; project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md passed
```

## NEXT_RECOMMENDED_ACTION

```text
Correct project-runtime/agent-results/TASK_CORRECT_DESIGN_DOWNSTREAM_PACKETS_001.md result formatting, then rerun audit.
```
