# Data model and domain objects

**Purpose:** Define the initial aggregate boundaries, core objects, and privacy-sensitive data categories that should guide schema design and service boundaries.

**Audience:** Backend contributors, schema authors, analytics planners, and agents implementing persistence or event contracts.

**How to use this document:** Use this document before creating database migrations, request schemas, event payloads, or integration mappings.

**Relation to the blueprint:** Derived from blueprint section 13 and simplified into domain families that map cleanly to the placeholder modules.

**Relation to the repository tree:** Informs `src/ai_recruiting_platform/domain/`, `schemas/`, `analytics/`, `audit/`, and compliance modules.

**Neighboring documents:**
- [System architecture](../03_architecture/system_architecture.md)
- [API design and webhooks](../03_architecture/api_design_and_webhooks.md)
- [Code localization plan](../03_architecture/code_localization_plan.md)
- [Compliance, privacy, and AI governance](../05_governance_trust/compliance_privacy_and_ai_governance.md)

## Concise thesis

The platform's core objects are not just recruiter entities like jobs and candidates. They also include policy state, provenance, AI artifacts, integration state, analytics events, and billing entitlements. The data model must preserve those relationships from the start.

## Design problem this document addresses

Stateless agents need domain boundaries so they do not model the platform as a single candidate table plus assorted JSON fields. That kind of shortcut destroys auditability, rights workflows, and explainability later.

## Primary aggregate families

The scaffold reserves the following domain families:
- tenancy and access;
- jobs, criteria, and calibration;
- candidate profiles, sources, talent graph, freshness, and data quality;
- search, rediscovery, scoring, and explainability;
- outreach, replies, and conversations;
- scheduling, interviews, and scorecards;
- compliance, privacy requests, suppression, and audit;
- integrations and sync state;
- analytics, reporting, ROI, billing, and notifications;
- AI and agent metadata such as prompt versions, model versions, evaluation runs, and agent runs.

## Boundary rules

A few boundary rules should shape implementation:
- candidate identity, contact data, consent, and suppression state are privacy-sensitive and should not be casually duplicated across unrelated modules;
- scoring artifacts must be reconstructable from criteria, evidence, and versioned model or prompt state;
- integrations need their own connection, mapping, sync-job, and error records rather than burying state in domain entities;
- analytics and audit records should be append-oriented and reference domain objects rather than replace them.

## Schema and event design consequences

Request schemas should remain typed and explicit about mutation scope. Event payloads should identify tenant, actor, object, action, and relevant workflow context. Future migrations should prefer normalized authoritative records plus event and projection layers over all-purpose denormalized storage. That design makes it easier to satisfy both workflow speed and compliance traceability.

## Phased implementation notes

Implement persistence in layers: start with domain objects and lifecycle states, then request and response schemas, then migrations and storage, then event projections and analytics views. Never add screening or privacy state as undocumented side fields on unrelated entities.


## Migration scaffolding status

A phase-zero Alembic migration scaffold now exists in `migrations/` with an initial revision anchor. Implement table-creating revisions in the order listed in this document so tenancy/access and governance-critical state land before downstream workflow entities.
