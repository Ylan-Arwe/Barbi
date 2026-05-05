# Screen inventory

**Purpose:** Provide a repository-friendly inventory of the main screens and screen families the scaffold is reserving space for, along with their primary goals, dependencies, and likely code ownership.

**Audience:** UI implementers, API designers, QA contributors, and agents validating that a new screen belongs in the correct surface family.

**How to use this document:** Use this document as a screen-level crosswalk between experience goals, route groups, API needs, and placeholder file ownership.

**Relation to the blueprint:** Derived from blueprint section 10, condensed into screen families that map cleanly into repo assets.

**Relation to the repository tree:** Connects screen concepts to `apps/web/web_surface_contract.py`, `apps/extension/extension_surface_contract.py`, API routes, and future test plans.

**Neighboring documents:**
- [UX specification](../02_experience/ux_specification.md)
- [Information architecture and navigation](../02_experience/information_architecture_and_navigation.md)
- [API design and webhooks](../03_architecture/api_design_and_webhooks.md)
- [Testing, quality assurance, and eval strategy](../06_delivery_operations/testing_quality_assurance_and_eval_strategy.md)

## Concise thesis

The screen inventory should be detailed enough that a stateless agent can identify the right target folder and neighboring APIs, but abstract enough that it does not pretend final UI decisions have already been made.

## Design problem this document addresses

A repository without screen inventory tends to scatter UI behavior across arbitrary routes and then retrofit consistency after implementation costs are already sunk.

## Core screen families

The scaffold assumes the following early screen families:
- setup and identity screens;
- job list, job detail, intake wizard, and hiring-manager calibration;
- search results, candidate card, candidate profile, and comparison;
- project or pipeline workspaces;
- outreach builder, inbox, and campaign analytics;
- scheduling, interview-plan, and scorecard surfaces;
- agent console and run detail views;
- analytics, ROI, compliance, audit, integrations, billing, and developer surfaces.

Each family should later gain explicit route ownership, API dependencies, loading states, and accessibility expectations.

## Surface-to-code mapping

At this stage the mapping is:
- `apps/web/web_surface_contract.py` describes shared web-app ownership and route-group responsibilities;
- `src/ai_recruiting_platform/api/*_routes.py` define server-side route families that back the surfaces;
- `src/ai_recruiting_platform/schemas/*.py` define response and mutation contracts;
- `services/*.py` localize orchestration logic needed by the screen;
- analytics and audit packages define the non-visible obligations the screen must satisfy.

## What should be added later, not now

This inventory is not a design mockup library. It should not hard-code final component hierarchy, styling systems, or framework-specific routing syntax until implementation tasks formally choose them. Treat it as a screen-level plan of record that future UI code can fill in.

## Phased implementation notes

When implementing a new screen, update this inventory if the route family changes or if a new cross-cutting obligation appears. Use it to prevent duplicate surfaces and unowned UI behavior.
