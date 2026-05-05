# AI package

**Purpose:** Provider gateways, ranking contracts, prompt registries, and evaluation or guardrail contracts.

**Why this folder exists:** Use this folder for AI-facing interfaces and controls.

## Current assets

- `__init__.py`
- `evaluation_and_guardrails_contract.py`
- `model_gateway_contract.py`
- `prompt_registry_contract.py`
- `ranking_and_matching_contract.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
