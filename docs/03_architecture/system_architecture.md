# System architecture

**Purpose:** Describe the major runtime components, state boundaries, and service interactions that the recruiting platform will need once implementation begins.

**Audience:** Backend and full-stack contributors, architecture reviewers, and agents planning service boundaries.

**How to use this document:** Use this document when deciding where behavior belongs: app shell, API route, service orchestrator, background worker, domain model, integration connector, analytics pipeline, or governance surface.

**Relation to the blueprint:** Derived from blueprint section 11, converted from a broad component map into repo-native implementation boundaries.

**Relation to the repository tree:** Owns the conceptual mapping between `apps/`, `src/ai_recruiting_platform/`, external systems, and the cross-cutting observability, audit, and policy layers.

**Neighboring documents:**
- [Technology architecture](../03_architecture/technology_architecture.md)
- [Data model and domain objects](../03_architecture/data_model_and_domain_objects.md)
- [Repository asset map](../03_architecture/repository_asset_map.md)
- [Observability, operations, and support](../06_delivery_operations/observability_operations_and_support.md)

## Concise thesis

The architecture should separate user surfaces, HTTP contracts, orchestration services, long-running workers, domain rules, integrations, analytics, and governance concerns so that workflow logic stays traceable and policy-sensitive behavior can be audited.

## Design problem this document addresses

If system architecture is left implicit, future agents tend to blend UI concerns, orchestration, persistence, and integration behavior into whichever file was open first. That produces brittle code and impossible audits.

## Component layers

The intended layers are:
- app surfaces in `apps/` for web, API entrypoint, worker runtime, and extension;
- internal package modules in `src/ai_recruiting_platform/` for domain contracts, service orchestration, route families, schemas, search, integrations, AI, agents, analytics, compliance, audit, notifications, and billing;
- supporting infrastructure for databases, search indexes, vector search, background queues, identity, email, calendar, ATS/CRM/HCM providers, and analytics storage.

The scaffold intentionally reserves a file home for each of these layers before implementation so that later code can land in predictable locations.

## Control and data flow

A typical control flow should look like:
user or external event → app surface / HTTP route → permission and schema validation → service orchestration → domain rules and persistence → async work or integration calls where needed → analytics and audit emission → user-visible state update.

AI and agent behavior are not allowed to float outside that structure. They should flow through explicit gateway, orchestration, and logging layers.

## Cross-cutting system obligations

Three obligations apply almost everywhere:
- tenant and role isolation;
- audit and provenance capture for sensitive actions;
- analytics and operations signals that let humans reconstruct what happened.

These concerns justify dedicated `audit/`, `analytics/`, and compliance modules instead of repeating ad hoc logic across every service.

## Phased implementation notes

Start with clear interfaces and event boundaries before introducing framework-specific implementations. Maintain a separation between user-facing contracts, orchestration services, and provider adapters so the platform can add depth without collapsing into route-level business logic.
