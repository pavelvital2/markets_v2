# ARCH_MVP_BOUNDARIES_001

## Artifact Type

Architecture document. Not a task packet.

## Source Basis

- `project-input/TZ.md`
- audited runtime result `project-runtime/agent-results/TASK_RESEARCH_SOURCE_DISCOVERY_001.md`

No source project files were inspected for this document.

## Purpose

Define MVP boundaries for Market Intelligence Platform.

## MVP In Scope

The first working product includes:

- external WB market data collection;
- external Ozon market data collection;
- unified data contracts for WB/Ozon;
- parser export bundle;
- analytics import;
- run history;
- Market Intelligence web UI;
- overview dashboard;
- query analytics;
- product analytics;
- seller analytics;
- WB/Ozon comparison;
- data quality dashboard;
- search and filtering;
- Excel export.

## MVP Out of Scope as Confirmed Calculations

The first working version must not treat these as confirmed calculations:

- exact profit;
- exact margin;
- factual revenue;
- competitor sales;
- ad efficiency;
- card conversion;
- exact cost price;
- supply economics.

These require confirmed sources for sales, orders, stocks, costs, commissions, logistics, ads, returns, and finance reports.

## Future Contours

The architecture must prepare for, but not implement in MVP:

- Own Store Intelligence;
- WB Seller API integration;
- Ozon Seller API integration;
- Excel-based own-store imports if APIs are insufficient;
- product master;
- marketplace listing map;
- product matching;
- Decision Layer.

## Own-Store Placeholder Entities

Future entity placeholders from the TZ:

```text
product_master
marketplace_listing_map
```

These must not drive MVP behavior until own-store contracts are confirmed.

## Decision Layer Boundary

Decision Layer signals are future work. Recommendations must include data source, explanation, and confidence level. No recommendation formula is defined by this document.

## Score Boundary

The TZ names `competition_score`, `opportunity_score`, `visibility_score`, `price_index`, and `data_confidence_level`. Formula definition and thresholds require bounded follow-up design before implementation as business logic.

