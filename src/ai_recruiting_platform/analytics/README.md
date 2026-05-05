# Analytics package

**Purpose:** Event taxonomy, metrics catalog, and reporting contract definitions.

**Why this folder exists:** Use this folder for metrics and reporting contracts.

## Current assets

- `__init__.py`
- `event_taxonomy_contract.py`
- `metrics_catalog_contract.py`
- `reporting_and_qbr_contract.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
