# src/ai_recruiting_platform/

**Purpose:** Primary internal package for the recruiting platform scaffold.

**Why this folder exists:** Most product logic should eventually live somewhere under this package.

## Current assets

- `agents/`
- `ai/`
- `analytics/`
- `api/`
- `audit/`
- `billing/`
- `compliance/`
- `config/`
- `data_quality/`
- `domain/`
- `integrations/`
- `notifications/`
- `schemas/`
- `search/`
- `services/`
- `__init__.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/master_documentation_index.md`
