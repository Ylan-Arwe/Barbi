# apps/api/

**Purpose:** HTTP application entrypoint contract for the API surface.

**Why this folder exists:** Use this folder for framework-level API bootstrap concerns such as middleware, route registration, and runtime wiring.

## Current assets

- `api_surface_contract.py`

## Implemented bootstrap surface

`api_surface_contract.py` now provides a real FastAPI bootstrap entrypoint:
- `create_application()` for app creation and base wiring;
- `/v1/healthz` liveness endpoint with typed payload mapping;
- extension hooks for middleware, observability, and background dispatch registration.

Run locally after runtime dependencies are installed:

```bash
uvicorn apps.api.api_surface_contract:create_application --factory --host 0.0.0.0 --port 8000
```

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/02_experience/`
- `docs/03_architecture/`
- `docs/06_delivery_operations/`
