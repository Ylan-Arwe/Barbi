# Product principles, personas, and jobs

**Purpose:** Translate the blueprint's principles and persona tables into practical design and implementation constraints that should shape UI, data modeling, AI behavior, and checklist ordering.

**Audience:** Product owners, UX designers, service authors, and coding agents implementing recruiter-facing or reviewer-facing behavior.

**How to use this document:** Use this document when defining screen behavior, writing service contracts, or deciding whether a feature supports a real user job or only adds conceptual clutter.

**Relation to the blueprint:** Derived from blueprint sections 4 and 5, reformatted around implementation consequences rather than abstract product values.

**Relation to the repository tree:** Informs `docs/02_experience/`, `src/ai_recruiting_platform/domain/`, `src/ai_recruiting_platform/services/`, and policy-sensitive modules under `src/ai_recruiting_platform/compliance/` and `src/ai_recruiting_platform/agents/`.

**Neighboring documents:**
- [Platform overview and build thesis](../01_product/platform_overview_and_build_thesis.md)
- [UX specification](../02_experience/ux_specification.md)
- [Data model and domain objects](../03_architecture/data_model_and_domain_objects.md)
- [Compliance, privacy, and AI governance](../05_governance_trust/compliance_privacy_and_ai_governance.md)

## Concise thesis

Every persona in the blueprint implies a different failure mode. Recruiters punish cognitive overload, compliance reviewers punish opaque decisions, candidates punish disrespectful contact, and procurement punishes undocumented claims. The repository should treat those reactions as design facts, not post-launch surprises.

## Design problem this document addresses

If principles and personas stay trapped in one planning document, implementation drifts into convenient abstractions. Stateless agents need to know which user job a module supports and which anti-patterns are unacceptable before code begins.

## Operating principles converted into repo rules

The key principles can be restated as repository expectations:
- recruiter-first workflow means default surfaces must expose the next useful action rather than raw model internals;
- evidence-backed AI means scoring, summaries, and personalization must be rooted in candidate or job evidence that can later be surfaced;
- human-in-the-loop by default means consequential actions require review paths and audit state;
- compliance-by-design means suppression, privacy requests, and notices are not “future polish” tasks;
- integration-first architecture means stage maps, sync logs, and failure recovery belong in core design, not backlog trivia.

## Persona clusters and what they demand from the scaffold

Recruiters and sourcers need search, shortlist, candidate cards, and outreach flows that reduce manual thrash. Hiring managers need limited-permission review, structured feedback, and comparison surfaces. Coordinators need scheduling and interview logistics. Admins and recruiting operations need integrations, permissions, audit logs, and billing visibility. Compliance and security reviewers need explainability, privacy workflows, and trust artifacts. Candidates need respectful communication, notices, accessibility, and rights exercise paths.

These clusters explain why the repo includes distinct app surfaces, route contracts, domain modules, analytics modules, and governance docs instead of one undifferentiated “platform” package.

## Jobs to be done that should drive implementation priority

The first-priority jobs are:
1. convert a job description into approved criteria and a credible search strategy;
2. generate and review a useful shortlist;
3. safely contact appropriate candidates;
4. classify replies and move candidates to scheduling;
5. keep ATS and communication systems in sync;
6. measure whether this actually saved time and reduced failure.

Any early implementation work that does not strengthen one of those jobs needs strong justification.

## Persona-specific red lines

Some anti-patterns should be treated as build blockers:
- recruiters should not have to open multiple systems to understand fit, history, and contact state;
- hiring managers should not see black-box scores without evidence;
- compliance reviewers should not need engineering help to reconstruct a decision trail;
- candidates should not be contacted after opt-out or kept ignorant about rights and notices;
- procurement reviewers should not see marketing claims that the repository cannot back with docs or planned evidence artifacts.

## Phased implementation notes

Use persona demands to break ties when choosing between tasks. If two backlog items compete, implement the one that reduces recruiter friction or compliance ambiguity in the shortest end-to-end workflow first. Expand persona coverage only after prerequisite identity, data, and policy layers are in place.
