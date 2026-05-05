# Schemas package

**Purpose:** Typed request, response, and event contracts used by routes, services, and tests.

**Why this folder exists:** Use this folder for typed API and event shapes.

## Current assets

- `__init__.py`
- `analytics_schemas.py`
- `billing_schemas.py`
- `candidates_schemas.py`
- `compliance_schemas.py`
- `integration_schemas.py`
- `jobs_schemas.py`
- `outreach_schemas.py`
- `scheduling_schemas.py`
- `scoring_schemas.py`
- `search_schemas.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
