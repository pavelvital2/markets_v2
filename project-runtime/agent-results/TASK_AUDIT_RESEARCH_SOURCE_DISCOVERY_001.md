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
TASK_AUDIT_RESEARCH_SOURCE_DISCOVERY_001
```

## SUMMARY

```text
Research audit failed because the authoritative runtime RESULT for TASK_RESEARCH_SOURCE_DISCOVERY_001 lacked mandatory NEXT_RECOMMENDED_ACTION. Bounded-source compliance, changed-file scope, and secret exposure checks passed.
```

## EVIDENCE

```text
RESULT_TEMPLATE_STATUS: failed
CHANGED_FILES_SCOPE_STATUS: passed
SECRET_EXPOSURE_STATUS: passed
REASONING_LEVEL_COMPLIANCE: passed
```

## NEXT_RECOMMENDED_ACTION

```text
Correct project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md to include NEXT_RECOMMENDED_ACTION and rerun audit.
```
