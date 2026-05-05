# UX specification

**Purpose:** Define the user-experience posture for recruiter, coordinator, hiring-manager, admin, compliance, developer, and candidate surfaces so that future interface work stays recruiter-first, evidence-backed, and low-friction.

**Audience:** Frontend contributors, product designers, API authors who support UI needs, and agents implementing or auditing user-facing behavior.

**How to use this document:** Use this document when translating workflow goals into screens, components, route contracts, and API response shapes. It is the governing UX stance document, not a final design system.

**Relation to the blueprint:** Derived from blueprint section 8 and reinforced by the product principles and workflow map.

**Relation to the repository tree:** Owns the experience rules that should later inform `apps/web/`, `apps/extension/`, API route design, analytics events, and accessibility tasks.

**Neighboring documents:**
- [Product principles, personas, and jobs](../01_product/product_principles_personas_and_jobs.md)
- [Information architecture and navigation](../02_experience/information_architecture_and_navigation.md)
- [Screen inventory](../02_experience/screen_inventory.md)
- [Testing, quality assurance, and eval strategy](../06_delivery_operations/testing_quality_assurance_and_eval_strategy.md)

## Concise thesis

The platform should feel like a focused recruiter workbench, not a model demo. Defaults should emphasize queues, evidence, next actions, and safe completion paths over speculative intelligence theater.

## Design problem this document addresses

Without a governing UX specification, the repository can accumulate screens that expose implementation internals, bury compliance checks, or increase recruiter context switching instead of reducing it.

## Core UX posture

The scaffold assumes a few non-negotiable interaction rules:
- default views should show the next useful action;
- evidence should be visible without turning every screen into a forensic report;
- risky actions should expose guardrails before execution, not as after-the-fact warnings;
- advanced model detail should be progressively disclosed;
- accessible candidate and recruiter flows are part of core product quality, not a later theme pass.

## High-value surface patterns

The highest-value early surfaces are:
- a Today-style operating queue for recruiters and coordinators;
- a fast job-intake and calibration flow;
- explainable candidate cards and shortlist review;
- outreach drafting and approval with suppression visibility;
- reply triage and scheduling surfaces;
- integration-health and audit views for admins and reviewers.

These patterns map directly to the placeholder app contracts under `apps/web/`, `apps/api/`, and `apps/worker/`.

## Safeguards and cognitive-load rules

Bulk actions, AI-generated drafts, agent suggestions, and candidate-contact actions should all communicate scope, confidence, and blocking policy conditions. Keyboard efficiency is encouraged, but confirmation and undo patterns are still needed around destructive or high-volume actions. The UI should not require users to infer suppression state, privacy state, or source freshness from hidden tabs.

## Accessibility and candidate experience

Candidate-facing scheduling, notices, privacy requests, and unsubscribe flows should be accessible from the outset. Internally, recruiter screens should still honor keyboard navigation, semantic labeling, visible focus, and screen-reader compatibility. Accessibility here is both a product quality expectation and a governance expectation because the platform touches employment workflows.

## Phased implementation notes

Begin with wire-level flow completion, route ownership, and API-state needs before polishing components. Treat accessibility, evidence exposure, and workflow guardrails as implementation requirements that inform data shape and tests, not as downstream styling tasks.
