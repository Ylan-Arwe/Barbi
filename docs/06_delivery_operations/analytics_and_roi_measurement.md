# Analytics and ROI measurement

**Purpose:** Define the event taxonomy, core metrics, and reporting expectations that should let the platform measure workflow outcomes rather than just feature usage.

**Audience:** Analytics contributors, product owners, backend engineers, and agents implementing event emission or reporting surfaces.

**How to use this document:** Use this document before adding analytics events, dashboards, ROI language, or QBR-style reporting features.

**Relation to the blueprint:** Derived from blueprint section 21 and related workflow and analytics sections.

**Relation to the repository tree:** Owns the relationship between workflow events, analytics package placeholders, reporting surfaces, and evidence-backed ROI language.

**Neighboring documents:**
- [End-to-end workflow map](../01_product/end_to_end_workflow_map.md)
- [Billing, packaging, and usage](../06_delivery_operations/billing_packaging_and_usage.md)
- [Testing, quality assurance, and eval strategy](../06_delivery_operations/testing_quality_assurance_and_eval_strategy.md)
- [Analytics package README](../../src/ai_recruiting_platform/analytics/README.md)

## Concise thesis

The platform's ROI story should come from measured workflow movement: faster shortlist creation, cleaner contact data, safer outreach, better coordination, and fewer preventable failures. Metrics without clear event semantics will collapse into marketing fog.

## Design problem this document addresses

The blueprint treats measurable ROI as a core wedge. That only works if the repo localizes event taxonomy and metric ownership before dashboards are built.

## Metric families

The most important early metrics are:
- time to first useful shortlist;
- contact accuracy and reveal quality;
- positive reply rate and campaign yield;
- ATS sync success and duplicate reduction;
- scheduling time saved;
- recruiter override and agent acceptance rates;
- compliance exceptions prevented;
- usage and entitlement consumption where billing depends on them.

## Event design implications

Every workflow stage should later emit events with tenant, actor, object, workflow context, and timing fields. Analytics should not depend on scraping UI state after the fact. This is why the scaffold includes dedicated analytics contracts and route placeholders instead of burying reporting logic inside business services.

## ROI claim discipline

Do not treat analytics as a license to invent savings. ROI statements should be tied to metric definitions, calculation logic, and caveats documented in this file and in future public-artifact work. If a metric is estimate-based or partial, say so.

## Phased implementation notes

Implement analytics incrementally: define the taxonomy, emit high-value events in core workflows, validate them in tests, then build reporting views. Keep ROI language subordinate to what the event system can actually support.
