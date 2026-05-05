# Information architecture and navigation

**Purpose:** Describe the major navigation surfaces, route groups, and role-specific wayfinding patterns that should organize the web experience and related app surfaces.

**Audience:** Frontend authors, UX planners, and stateless agents deciding where a new screen, route, or navigation affordance belongs.

**How to use this document:** Use this document when adding or renaming user-facing sections, planning route ownership, or checking whether a new feature belongs in an existing navigation group.

**Relation to the blueprint:** Derived from blueprint section 9 and informed by the workflow map and screen inventory.

**Relation to the repository tree:** Maps experience architecture to `apps/web/`, `apps/extension/`, route-level placeholders under `src/ai_recruiting_platform/api/`, and analytics instrumentation plans.

**Neighboring documents:**
- [UX specification](../02_experience/ux_specification.md)
- [Screen inventory](../02_experience/screen_inventory.md)
- [Repository asset map](../03_architecture/repository_asset_map.md)
- [Web surface contract](../../apps/web/README.md)

## Concise thesis

Navigation should mirror real workflow chunks: today, jobs, search, candidates, outreach, scheduling, analytics, integrations, governance, and admin. If users must invent their own mental grouping, the information architecture has already failed.

## Design problem this document addresses

A large platform can become impossible to navigate if every feature claims top-level status or if role-specific reviewer flows are buried inside recruiter-only surfaces.

## Primary navigation groups

The recommended top-level navigation is:
- Today
- Jobs
- Search
- Candidates
- Outreach
- Calendar / Interviews
- Agents
- Analytics
- Integrations
- Compliance
- Admin
- Developer / API
- Help / Docs

Not every role sees every group. Hiring managers, candidates, and compliance reviewers should receive limited-purpose views that expose only the routes relevant to their job.

## Role-aware route ownership

Route ownership should follow user intent:
- recruiter and sourcer flows dominate Today, Jobs, Search, Candidates, Outreach, and parts of Analytics;
- coordinators live primarily in Calendar / Interviews and Today;
- hiring managers need a constrained review portal and comparison surfaces;
- compliance and security roles need dedicated access to logs, reports, notices, and rights workflows;
- admins own organization settings, integrations, identity, billing, and audit review;
- developers need key, webhook, and API-reference surfaces but not broad candidate workflows.

## Navigation-state requirements

Each major navigation group eventually needs:
- permission-aware visibility;
- a predictable landing screen with empty, loading, and error states;
- breadcrumb or contextual links to adjacent workflow steps;
- explicit indication of blocked states such as disconnected integrations or privacy restrictions.

This is why navigation planning belongs in repo docs early: route ownership affects API grouping, analytics taxonomy, and even checklist sequencing.

## Phased implementation notes

Stabilize navigation groups before deep UI buildout. When new modules appear, prefer adding them under an existing workflow family unless a genuine new top-level audience or operational mode exists.
