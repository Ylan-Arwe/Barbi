# Compliance package

**Purpose:** Privacy, suppression, model-card, and audit-export contract definitions.

**Why this folder exists:** Use this folder for governance-sensitive logic and contract structures.

## Current assets

- `__init__.py`
- `audit_export_and_bias_support.py`
- `model_cards_and_risk_classification.py`
- `privacy_requests_and_candidate_rights.py`
- `suppression_and_unsubscribe_registry.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
