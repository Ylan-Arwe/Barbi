# Database migrations

This folder owns transactional schema migrations for the AI Recruiting Platform runtime baseline.

## Tooling baseline

Phase 0 adopts **Alembic** + **SQLAlchemy** for migration and metadata management.

- Alembic config: `migrations/alembic.ini`
- Alembic environment: `migrations/env.py`
- Migration scripts: `migrations/versions/`

## Scope of the first schema plan

The initial migration sequence is intentionally focused on foundational relational state required by downstream checklist phases:

1. tenancy and access control (`tenants`, `workspaces`, `users`, `teams`, `roles`, `role_assignments`)
2. job intake/calibration (`jobs`, `job_criteria`, `rubrics`, `job_approvals`)
3. candidate and provenance core (`candidates`, `candidate_profiles`, `candidate_sources`, `provenance_events`)
4. audit and compliance anchors (`audit_events`, `privacy_requests`, `suppression_registry`, `unsubscribe_registry`)

## How to run

From repository root:

```bash
alembic -c migrations/alembic.ini upgrade head
```

Create a revision:

```bash
alembic -c migrations/alembic.ini revision -m "describe change"
```

## Notes

- Keep migrations append-only; do not rewrite previously committed revision files.
- Align migration names and table boundaries with `docs/03_architecture/data_model_and_domain_objects.md`.
- When adding new persistence families, update this README and architecture docs in the same session.
