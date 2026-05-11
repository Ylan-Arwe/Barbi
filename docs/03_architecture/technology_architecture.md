# Technology architecture

**Purpose:** Record concrete runtime decisions for the first implementation lane, plus explicit constraints and deferred decisions.

**Audience:** Technical leads, contributors selecting frameworks, and coding agents introducing runtime dependencies.

**How to use this document:** Treat this as the source of truth for phase-zero runtime choices. If implementation requires a different technology, update this file, the roadmap, and checklist sequencing in the same session.

**Relation to the blueprint:** Derived from blueprint section 12 and converted from directional guidance into concrete implementation decisions.

**Relation to the repository tree:** Defines how `apps/`, `src/ai_recruiting_platform/`, and `migrations/` should acquire stack-specific code.

## Concise thesis

The repository now commits to a single Python-first runtime lane: FastAPI for HTTP APIs, Celery workers backed by Redis, PostgreSQL with SQLAlchemy and Alembic for transactional storage, OpenSearch for lexical search, pgvector in PostgreSQL for semantic retrieval prototyping, and Auth0-compatible OIDC for identity integration.

## Decision record for Phase 0 foundations

### 1) Web runtime and UI delivery

**Decision:** Use Next.js (App Router, TypeScript) for `apps/web`.

**Rationale:**
- aligns with recruiter-facing, workflow-heavy UI needs where server rendering and route-level data loading help first paint and deep-linking;
- supports modern component ecosystems for admin and analytics surfaces;
- keeps API separation explicit by consuming `apps/api` contracts.

**Rejected alternatives for the first lane:**
- React + Vite SPA only: simpler bootstrap, but weaker default SSR behavior for workflow navigation and deep-linking;
- Django templates: strong backend coupling, but reduces UI modularity for a separate frontend team.

### 2) API runtime

**Decision:** Use FastAPI + Uvicorn in `apps/api`.

**Rationale:**
- typed request/response contracts map cleanly to existing schema placeholders;
- async support matches integration-heavy workflows;
- straightforward health, readiness, and OpenAPI endpoints for phase-zero shells.

**Rejected alternatives:**
- Flask: good ergonomics but weaker typed-contract posture;
- Django REST Framework: heavier framework surface before we have domain flows implemented.

### 3) Worker runtime and queueing

**Decision:** Use Celery workers with Redis as broker/result backend in `apps/worker`.

**Rationale:**
- mature delayed/retry/task-chaining model for enrichment, scoring, and integration sync flows;
- Redis is already needed for shared operational concerns;
- broad operational familiarity and observability support.

**Rejected alternatives:**
- RQ: lighter but less expressive for complex orchestration;
- Dramatiq: strong option, but less existing operational familiarity across template contributors.

### 4) Transactional persistence and migrations

**Decision:** Use PostgreSQL + SQLAlchemy 2.x + Alembic.

**Rationale:**
- relational guarantees for tenancy, privacy, audit, and rights-state controls;
- SQLAlchemy models can remain internal while route schemas stay explicit;
- Alembic is a stable migration path for prerequisite-ordered rollout.

**Rejected alternatives:**
- Django ORM: not chosen because API runtime is FastAPI;
- NoSQL-first approach: weaker fit for strict relational governance and audit lineage.

### 5) Search and retrieval

**Decision:**
- lexical and filter search via OpenSearch;
- semantic prototype path via pgvector in PostgreSQL (upgradable to dedicated vector store later).

**Rationale:**
- OpenSearch handles recruiter filter/search patterns and operational faceting;
- pgvector provides low-friction semantic retrieval during early phases without immediate extra infrastructure.

**Deferred decision:** Whether to move semantic retrieval to a dedicated vector engine after workload profiling.

### 6) Identity and authentication

**Decision:**
- OIDC/OAuth2 integration using Auth0-compatible provider contracts;
- JWT validation in API routes with tenant/workspace claims.

**Rationale:**
- enterprise-friendly path for later SSO expansion;
- lets phase-one auth flows start with local-dev and managed-provider options.

### 7) Observability and operations

**Decision:**
- OpenTelemetry instrumentation for API and worker traces;
- structured JSON logs;
- Prometheus metrics endpoint from API and worker exporters.

**Rationale:**
- supports evidence-backed debugging and ops discipline called for across governance docs;
- keeps vendor choice open while enforcing telemetry shape early.

## Dependency posture and implementation boundaries

- Runtime dependencies are now approved for phase-zero foundations and should be introduced only in the owning roots (`apps/`, `src/ai_recruiting_platform/config/`, and `migrations/`).
- Do not add provider SDKs (ATS, CRM, email vendors) until the corresponding checklist item is active.
- Keep `src/ai_recruiting_platform/` framework-light: domain, services, schemas, and contracts should not depend on web routing internals.

## Remaining explicit decisions

The following are intentionally deferred and must be documented before adoption:
- frontend component library standardization;
- infrastructure-as-code stack and deployment substrate;
- analytics warehouse/BI vendor;
- long-term semantic vector store strategy after production profiling.
