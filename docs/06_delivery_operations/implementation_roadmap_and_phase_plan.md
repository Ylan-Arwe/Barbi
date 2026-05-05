# Implementation roadmap and phase plan

**Purpose:** Translate the blueprint's roadmap into a repository-aware phase plan that matches the checklist ordering and placeholder structure.

**Audience:** Maintainers sequencing work across sessions and coding agents choosing the highest-value bounded task.

**How to use this document:** Use this document to understand which implementation waves should happen in which order and why the checklist phases are structured as they are.

**Relation to the blueprint:** Derived from blueprint section 26 and adapted to the repo scaffold that now already contains split docs and placeholder modules.

**Relation to the repository tree:** Provides the phase narrative that the checklist operationalizes and that package READMEs and root docs should reference.

**Neighboring documents:**
- [Platform overview and build thesis](../01_product/platform_overview_and_build_thesis.md)
- [Feature inventory and prioritization](../01_product/feature_inventory_and_prioritization.md)
- [Final Productization Checklist](../../Final-Productization-Checklist.md)
- [Stateless coding agent handoff](../06_delivery_operations/stateless_coding_agent_handoff.md)

## Concise thesis

The scaffold is already doing phase-zero documentation and localization work. The roadmap therefore starts from the remaining build-out required to turn that scaffold into a usable platform rather than pretending we are at a blank whiteboard.

## Design problem this document addresses

A roadmap that ignores the current scaffold causes task duplication and checklist churn. This document reconciles the blueprint's original roadmap with the repo state after scaffold conversion.

## Phase interpretation

Recommended high-level phases:
- Phase 0: convert scaffold decisions into executable foundations such as settings, app shells, domain state, and migration strategy;
- Phase 1: build the first real job-to-shortlist and governed-outreach lane;
- Phase 2: deepen search, rediscovery, reply handling, scheduling, and analytics loops;
- Phase 3: expand enterprise controls, trust artifacts, richer integrations, and governance readiness;
- Phase 4: add governed agents, optimization, and maturity-stage operating depth.

## How this phase plan differs from the original blueprint

The original blueprint included discovery and architecture work as explicit roadmap phases. This repo pack already performs a large part of that work by splitting docs, localizing code, and generating checklist tasks. The remaining phases therefore focus on implementation rather than re-describing the design from scratch.

## Checklist relationship

The checklist should remain more granular than this roadmap. Use the roadmap to choose the right phase and dependency band, then use the checklist to select the specific bounded task with the correct prerequisites.

## Phased implementation notes

When a phase is materially re-sequenced, update this file, the checklist grouping, and the relevant package READMEs together. Do not silently change implementation order in one place only.
