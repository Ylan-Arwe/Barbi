# API design and webhooks

**Purpose:** Define the HTTP and webhook contract philosophy that should shape route groups, schemas, auth, idempotency, and integration events.

**Audience:** API authors, integration contributors, QA engineers, and coding agents implementing route families.

**How to use this document:** Use this document when adding or reviewing API routes, public endpoints, webhook events, or schema contracts.

**Relation to the blueprint:** Derived from blueprint section 14 plus the integration design sections that describe public API and webhook expectations.

**Relation to the repository tree:** Maps directly to the placeholder files in `apps/api/` and `src/ai_recruiting_platform/api/` and to future public-facing developer documentation.

**Neighboring documents:**
- [System architecture](../03_architecture/system_architecture.md)
- [Data model and domain objects](../03_architecture/data_model_and_domain_objects.md)
- [Integration design](../06_delivery_operations/integration_design.md)
- [Stateless coding agent handoff](../06_delivery_operations/stateless_coding_agent_handoff.md)

## Concise thesis

The platform should be REST-first, typed, auditable, and explicit about tenant scope. Public and internal routes should share consistent shapes for pagination, filtering, auth, errors, and idempotent mutations.

## Design problem this document addresses

If route philosophy is unspecified, future agents will implement ad hoc endpoint shapes that are hard to test, hard to document, and painful to integrate across ATS, scheduling, analytics, and governance surfaces.

## Route families

The current placeholder route families are:
- auth and identity;
- jobs;
- candidates;
- search;
- scoring;
- outreach;
- scheduling;
- agents;
- compliance;
- integrations;
- analytics;
- billing.

That grouping should remain stable unless a new route family supports a genuinely distinct domain boundary.

## Contract expectations

Every route family should later support:
- typed request and response schemas in `src/ai_recruiting_platform/schemas/`;
- tenant and permission enforcement;
- structured error shapes;
- pagination and filtering for collection reads;
- idempotency for externally visible or high-risk mutations;
- audit emission for sensitive reads, exports, or writes;
- version-friendly naming and documentation.

Webhook design should mirror the same event taxonomy and include retry, signing, replay, and failure visibility.

## Public API caution

The repo already reserves space for public API and webhook contracts, but that does not mean the public developer surface is launch-ready. Public exposure should follow after internal route semantics, auditability, and provider event handling are stable enough to support external trust and support obligations.

## Phased implementation notes

Build internal route consistency before broadening public exposure. Keep public API scope conservative until integration mappings, auth stories, and event replay semantics are well understood and test-backed.
