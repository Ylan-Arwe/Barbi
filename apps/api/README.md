# apps/api/

**Purpose:** HTTP application entrypoint contract for the API surface.

**Why this folder exists:** Use this folder for framework-level API bootstrap concerns such as middleware, route registration, and runtime wiring.

## Current assets

- `api_surface_contract.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/02_experience/`
- `docs/03_architecture/`
- `docs/06_delivery_operations/`
