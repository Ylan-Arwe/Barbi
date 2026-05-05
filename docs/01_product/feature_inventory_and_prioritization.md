# Feature inventory and prioritization

**Purpose:** Translate the blueprint's exhaustive feature inventory into implementation-oriented feature clusters and priority bands that can drive the open checklist without degenerating into giant omnibus tasks.

**Audience:** Product maintainers, roadmap owners, and coding agents selecting bounded work from the checklist.

**How to use this document:** Use this document to understand which capabilities are launch-critical, which are sequencing-dependent, and which are explicitly deferred until stronger foundations exist.

**Relation to the blueprint:** Derived from blueprint section 7, but grouped into coherent product modules and priority bands rather than preserving a single monolithic feature table.

**Relation to the repository tree:** Defines the conceptual source for checklist phases, top-level package boundaries, and future milestone slicing across `apps/`, `src/ai_recruiting_platform/`, `prompts/`, and `skills/`.

**Neighboring documents:**
- [End-to-end workflow map](../01_product/end_to_end_workflow_map.md)
- [Repository asset map](../03_architecture/repository_asset_map.md)
- [Implementation roadmap and phase plan](../06_delivery_operations/implementation_roadmap_and_phase_plan.md)
- [Final Productization Checklist](../../Final-Productization-Checklist.md)

## Concise thesis

The blueprint's hundreds of features only become buildable when grouped into capability families with explicit prerequisites. Priority here means “what unlocks believable workflow progress,” not “what sounds most impressive in a demo.”

## Design problem this document addresses

A raw feature table is too fine-grained for repo orientation and too coarse for task execution. This document turns that table into launch bands and dependency logic that the checklist can operationalize.

## Launch-critical capability bands

P0 and early-P1 work should concentrate on:
- tenancy, identity, access, and admin foundations;
- job intake, approved criteria, and hiring-manager calibration;
- candidate profile assembly, provenance, freshness, and enrichment surfaces;
- search, rediscovery, scoring, and explainability;
- suppression, unsubscribe, privacy-request, and audit controls;
- recruiter-facing outreach, reply handling, and scheduling basics;
- at least one viable ATS connector plus email and calendar integrations;
- outcome instrumentation and trust documentation sufficient to support real internal or pilot use.

These are the bands that make the product coherent rather than fragmented.

## Differentiator bands that still depend on core workflow

Strong differentiators sit on top of the workflow core:
- field-level provenance and freshness visibility;
- governed agents with explicit permissions, logs, approvals, and kill switches;
- hiring-manager calibration loops that improve search strategy;
- candidate comparison and evidence panels that reduce decision ambiguity;
- ROI views that connect workflow activity to tangible funnel movement;
- documentation and trust artifacts that shorten buyer skepticism cycles.

They matter, but only after the basic workflow behaves predictably.

## Deferred or maturity-stage bands

Later phases should absorb:
- richer billing and packaging controls;
- more ATS/CRM/HCM providers;
- broader developer platform surfaces;
- public launch collateral and trust-center expansion;
- optimization work that requires real latency or usage data;
- browser-extension or network-assisted workflows that need careful policy review.

The scaffold includes localization for these lanes now so future work does not sprawl, but the checklist should continue to enforce prerequisites before agents implement them.

## Checklist translation rule

Every feature cluster in this document should map into many bounded checklist entries, not one. A feature family becomes actionable only after it is broken into data contracts, APIs, UI surfaces, worker flows, tests, analytics events, docs, and governance checks with explicit `DONE WHEN` conditions.

## Phased implementation notes

Use the priority bands to decide what stays runtime-dependency-free in the scaffold and what becomes explicit implementation work later. New dependencies, providers, and public claims should be introduced only when the corresponding priority band is actually being built.
