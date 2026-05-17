# TASK PROPOSAL

## PROPOSAL_ID

```text
TASK_PROPOSAL_OWNER_DECISIONS_001
```

## PROPOSAL_STATUS

```text
draft
```

## PROPOSAL_TITLE

```text
Capture owner decisions for analytics formulas
```

## REQUESTED_BY_ROLE

```text
designer
```

## PURPOSE

```text
Record owner decisions that are not required for skeleton work but will block later business-facing analytics and recommendations if unresolved.
```

## PROPOSED_TASK_KIND

```text
design_continuation
```

## PROPOSED_TARGET_ROLE

```text
designer
```

## PROPOSED_SCOPE

```text
- convert owner decisions on analytics formulas, thresholds, partial data states, source-contract retention policy, and own-store source priority into governed design inputs
- keep the work non-dispatchable until a full TASK_PACKET_TEMPLATE-compatible task is created
```

## OPEN_QUESTIONS

```text
- Define formulas for visibility_score, competition_score, opportunity_score, price_index, and data_confidence_level.
- Define default thresholds for opportunity_score and competition_score.
- Decide which partial data states may be used for owner-facing reports.
- Decide whether initial MVP shows score placeholders, hides scores, or ships simple clearly labeled formulas after design approval.
- Decide retention and visibility policy for sanitized raw fixtures, raw JSON fragments, HTML snapshots, and HAR-derived artifacts.
- Decide future own-store source priority: WB/Ozon Seller APIs, Excel exports, or internal product directory first.
```

## DISPATCH_STATUS

```text
non_dispatchable
```

## CONVERSION_REQUIREMENTS

```text
- create a full TASK_PACKET_TEMPLATE-compatible packet before dispatch
- validate the resulting task packet with TASK_PACKET_SCHEMA_VALIDATION_RULES
- keep this proposal as non-dispatchable historical context if retained
```
