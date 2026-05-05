# Integrations package

**Purpose:** Connector abstractions and public integration contracts.

**Why this folder exists:** Use this folder for provider-specific interfaces and shared connector rules.

## Current assets

- `__init__.py`
- `ats_connectors_contract.py`
- `base_connector_contract.py`
- `crm_hcm_connectors_contract.py`
- `email_and_calendar_connectors_contract.py`
- `webhooks_and_public_api_contract.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
