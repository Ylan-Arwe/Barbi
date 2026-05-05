# Platform overview and build thesis

**Purpose:** Turn the blueprint into a repository-native statement of what the platform is, what it must prove, and why the scaffold is organized around that proof burden.

**Audience:** Human maintainers, architecture reviewers, and coding agents choosing between competing implementation paths.

**How to use this document:** Read this first when you need the shortest credible explanation of the platform's intended end-state and the design posture that should constrain every implementation choice.

**Relation to the blueprint:** Derived primarily from blueprint sections 1 through 4, with product framing narrowed into repository decisions instead of market-facing prose.

**Relation to the repository tree:** Owns the strategic thesis that justifies the folder layout in `apps/`, `src/`, `prompts/`, `skills/`, and the supporting documentation under `docs/`.

**Neighboring documents:**
- [Product principles, personas, and jobs](../01_product/product_principles_personas_and_jobs.md)
- [End-to-end workflow map](../01_product/end_to_end_workflow_map.md)
- [System architecture](../03_architecture/system_architecture.md)
- [Implementation roadmap and phase plan](../06_delivery_operations/implementation_roadmap_and_phase_plan.md)

## Concise thesis

The platform is not being built as a feature grab bag. It is being scaffolded as a recruiter-first operating system that only makes claims the repository can later defend through code, logs, tests, docs, and audit artifacts.

## Design problem this document addresses

A monolithic blueprint can describe ambition, but it does not tell a stateless coding agent where work belongs, what must be built first, or what forms of product risk must be designed out before growth features arrive.

## What the repository is optimizing for

This repository is optimized for disciplined execution rather than early implementation theatrics. The scaffold localizes work around the measurable job of taking an approved requisition to a qualified, interested, and scheduled candidate while preserving candidate rights, human oversight, and proof-backed documentation.

The build thesis therefore favors:
- provenance before aggressive enrichment claims;
- explainability before autonomous screening claims;
- suppression and privacy controls before outreach automation;
- auditability before agent autonomy marketing;
- documentation and acceptance criteria before broad launch positioning.

## Primary user and buyer logic

The primary day-to-day user is the recruiter or sourcer who needs a usable queue, a credible shortlist, and safe next actions. Buyers and reviewers include talent acquisition leaders, recruiting operations, enterprise procurement, compliance, security, and, in some markets, public-sector reviewers. That mix means the repository must support both operational throughput and defensibility.

This is why the scaffold separates recruiter experience, architecture, AI automation, governance, and delivery operations into different documentation families. A future agent can work on one lane without losing the context that another stakeholder group will later use to judge the result.

## Competitive posture translated into repository policy

The differentiator described in the blueprint is proof-backed execution. In repository terms, that means every substantial product claim should eventually have a home in one or more of these places:
- a placeholder module that localizes implementation ownership;
- a doc that defines expected behavior and boundaries;
- a checklist entry with explicit `DONE WHEN` conditions;
- a test or evaluation plan;
- a public-artifact or trust-center task when the claim will face buyers.

If a future implementation cannot be mapped into that chain, it should not be treated as a finished platform capability.

## Implications for build order

The repository is deliberately front-loaded with structure. The correct build order is not “whichever feature sounds impressive.” Access control, tenancy, jobs, candidates, provenance, suppression, scoring evidence, and integration health all sit underneath the more visible recruiter surfaces. Outreach, scheduling, analytics, and agent automation depend on those foundations. Enterprise trust and public claims depend on all of them.

This document should therefore be read together with the roadmap, code localization plan, and checklist before a stateless agent chooses a task.

## Phased implementation notes

Implement from thesis outward: first confirm identity, access boundaries, workflow ownership, and data contracts; then build the shortest end-to-end lane that proves shortlist creation, governed outreach, and measurable funnel movement; then deepen integrations, enterprise controls, and agents. When implementation pressure conflicts with the thesis, preserve evidence, explainability, and candidate-rights defaults.
