# Technology architecture

**Purpose:** Record the preferred technical stack direction, the areas that remain intentionally undecided, and the dependency policy that should govern implementation.

**Audience:** Technical leads, contributors selecting frameworks, and coding agents deciding whether a new runtime dependency is justified yet.

**How to use this document:** Use this document before adding frameworks, SDKs, databases, or build tools so that stack decisions remain consistent with the scaffold's conservative dependency posture.

**Relation to the blueprint:** Derived from blueprint section 12, but rewritten as a decision-and-boundary document rather than a shopping list.

**Relation to the repository tree:** Explains why `pyproject.toml` currently stays conservative, how future app roots should acquire dependencies, and which folders are expected to own stack-specific code once decisions are approved.

**Neighboring documents:**
- [System architecture](../03_architecture/system_architecture.md)
- [API design and webhooks](../03_architecture/api_design_and_webhooks.md)
- [Prompt recipes, skills, and context injection plan](../04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md)
- [Implementation roadmap and phase plan](../06_delivery_operations/implementation_roadmap_and_phase_plan.md)

## Concise thesis

The scaffold is intentionally ahead on architecture and behind on framework commitments. That is a feature, not a gap. Runtime dependencies should be added only when the corresponding implementation slice is being built and its tests, docs, and operational needs are known.

## Design problem this document addresses

Without explicit technology-architecture rules, stateless agents can quietly turn a conservative scaffold into an accidental framework pileup with overlapping abstractions, incompatible build assumptions, and speculative dependencies.

## Proposed stack directions

The blueprint points toward a modern web frontend, typed backend APIs, relational transactional storage, search plus vector retrieval, queue-backed workers, provider-agnostic AI orchestration, and observability built on logs, traces, and metrics. Those are directions, not yet committed implementation facts.

The scaffold therefore localizes likely code roots without asserting the final framework. `apps/web/` can later host the chosen frontend runtime, `apps/api/` the HTTP application entrypoint, and `apps/worker/` the async runtime. `src/ai_recruiting_platform/` remains the product logic package regardless of framework.

## Dependency posture for this scaffold stage

Current policy:
- preserve template development tooling and wrapper-first automation;
- do not add runtime libraries until the relevant checklist phase begins;
- prefer checklist entries over speculative dependency commits;
- update `pyproject.toml` path coverage when new code roots appear so quality tooling sees them;
- keep framework-specific decisions documented in this file and in the roadmap when they become real.

This keeps the repo coherent for future implementation without pretending the architecture has already been code-proven.

## Decision categories that must be made explicitly later

The scaffold still requires explicit decisions for:
- frontend framework and component library;
- backend framework and API stack;
- database migration tool and persistence approach;
- search and vector storage strategy;
- worker/queue runtime;
- identity provider strategy;
- analytics warehouse and BI/reporting approach;
- deployment topology and infrastructure automation.

Each of these decisions should be opened by a checklist entry before code or dependencies land.

## Phased implementation notes

Use this document to block speculative implementation shortcuts. When a runtime choice becomes necessary, update this file, the roadmap, the relevant package README, and the checklist in the same session so future agents inherit an explicit decision trail.
