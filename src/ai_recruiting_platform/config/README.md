# Configuration package

**Purpose:** Typed runtime settings and configuration boundaries.

**Why this folder exists:** Use this folder for environment and settings contracts that are shared across app shells and services.

## Current assets

- `__init__.py`
- `runtime_and_settings.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
