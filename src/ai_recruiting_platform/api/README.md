# API route package

**Purpose:** Transport-layer route contracts grouped by domain family.

**Why this folder exists:** Use this folder for HTTP route grouping and request-handling boundaries, not core business logic.

## Current assets

- `__init__.py`
- `agents_routes.py`
- `analytics_routes.py`
- `auth_and_identity_routes.py`
- `billing_routes.py`
- `candidates_routes.py`
- `compliance_routes.py`
- `integrations_routes.py`
- `jobs_routes.py`
- `outreach_routes.py`
- `scheduling_routes.py`
- `scoring_routes.py`
- `search_routes.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
