# apps/web/

**Purpose:** Web application shell contract for recruiter, admin, compliance, hiring-manager, and candidate-facing surfaces.

**Why this folder exists:** Use this folder for framework-level route grouping, layouts, and app bootstrap.

## Current assets

- `web_surface_contract.py`

## Implemented bootstrap surface

`web_surface_contract.py` now exposes a Next.js-facing bootstrap contract:
- typed route-group metadata for recruiter, hiring-manager, admin, and compliance areas;
- `create_web_shell_contract()` for environment-aware shell bootstrap payloads;
- explicit extension points for layout, role navigation, data loading, and error-state patterns.

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/02_experience/`
- `docs/03_architecture/`
- `docs/06_delivery_operations/`
