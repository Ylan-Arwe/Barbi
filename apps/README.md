# apps/

**Purpose:** Deployable application-surface contracts and future runtime entrypoints for the platform.

**Why this folder exists:** This folder exists so the repo can separate runtime shells from internal business logic. Add framework bootstrapping here, not in the internal package.

## Current assets

- `api/`
- `extension/`
- `web/`
- `worker/`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/02_experience/`
- `docs/03_architecture/`
- `docs/06_delivery_operations/`
