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
TASK_AUDIT_BOOTSTRAP_DESIGNER_001
```

## SUMMARY

```text
Bootstrap designer audit failed. Designer-declared changed files are within allowed paths, but both downstream dispatchable task packets fail executable schema validation because mandatory FILESYSTEM_GOVERNANCE and RUNTIME_GOVERNANCE sections are missing. The bootstrap continuation points to an invalid downstream task packet, so BOOTSTRAP_CONTINUATION_CHECK fails.
```

## BOOTSTRAP_CONTINUATION_STATUS

```text
downstream_task_packet
```

## BOOTSTRAP_CONTINUATION_CHECK

```text
failed
```

## READ_DOCS

```text
- project-docs/03_tasks/TASK_AUDIT_BOOTSTRAP_DESIGNER_001.md
- project-runtime/bootstrap/TASK_BOOTSTRAP_DESIGNER_001.md
- project-runtime/agent-results/TASK_BOOTSTRAP_DESIGNER_001.md
- agent-system/01_roles/AUDITOR.md
- agent-system/03_templates/AGENT_RESULT_TEMPLATE.md
- agent-system/09_validators/TASK_PACKET_SCHEMA_VALIDATION_RULES.md
- agent-system/09_validators/CHANGED_FILES_SCOPE_MATRIX.md
- project-docs/01_architecture/ARCH_BOOTSTRAP_DESIGN_INTAKE_001.md
- project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md
- project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md
```

## COMMANDS_RUN

```text
- python3 agent-system/scripts/validate_task_packet.py --mode checkpoint --active-doc-root project-docs project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md: failed, missing FILESYSTEM_GOVERNANCE and RUNTIME_GOVERNANCE
- python3 agent-system/scripts/validate_task_packet.py --mode checkpoint --active-doc-root project-docs project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md: failed, missing FILESYSTEM_GOVERNANCE and RUNTIME_GOVERNANCE
- python3 agent-system/scripts/validate_task_packet.py --mode checkpoint --active-doc-root project-docs project-docs/03_tasks/TASK_AUDIT_BOOTSTRAP_DESIGNER_001.md: passed
```

## EVIDENCE

```text
CHANGED_FILES_SCOPE_STATUS: passed
TASK_PACKET_SCHEMA_STATUS: failed
REPOSITORY_IDENTITY_STATUS: passed
FORBIDDEN_PATH_STATUS: passed
RUNTIME_MUTATION_STATUS: passed
EVIDENCE_STATUS: passed
SECRET_EXPOSURE_STATUS: passed
REASONING_LEVEL_COMPLIANCE: blocked
SYNTAX_EVIDENCE_STATUS: not_applicable
BOOTSTRAP_CONTINUATION_STATUS: downstream_task_packet
BOOTSTRAP_CONTINUATION_CHECK: failed
```

## VALIDATED_TASK_PACKETS

```text
- path: project-docs/03_tasks/TASK_RESEARCH_SOURCE_DISCOVERY_001.md; classification: TASK_PACKET; TASK_PACKET_SCHEMA_STATUS: failed; dispatchable: no
- path: project-docs/03_tasks/TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md; classification: TASK_PACKET; TASK_PACKET_SCHEMA_STATUS: failed; dispatchable: no
- path: project-docs/03_tasks/TASK_AUDIT_BOOTSTRAP_DESIGNER_001.md; classification: TASK_PACKET; TASK_PACKET_SCHEMA_STATUS: passed; dispatchable: yes
```

## SCOPE_VERIFICATION

```text
Auditor made no file changes. Designer output cannot pass until changed downstream dispatchable task packets are schema-valid.
```

## RISKS

```text
- Reasoning-level compliance could not be fully verified from allowed audit inputs because actual designer spawn-level evidence is absent.
```

## BLOCKERS

```text
NONE
```

## GAPS

```text
NONE
```

## NEXT_RECOMMENDED_ACTION

```text
Route governed correction for the designer downstream task packets so both TASK_RESEARCH_SOURCE_DISCOVERY_001.md and TASK_DESIGN_CONTINUATION_AFTER_SOURCE_DISCOVERY_001.md include mandatory FILESYSTEM_GOVERNANCE and RUNTIME_GOVERNANCE sections and pass validation.
```
