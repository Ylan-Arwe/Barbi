# Agents package

**Purpose:** Governed agent contracts and registry logic.

**Why this folder exists:** Use this folder for explicit agent definitions, permissions, and related runtime policy.

## Current assets

- `__init__.py`
- `agent_registry_and_permissions.py`
- `compliance_agent_contract.py`
- `data_quality_agent_contract.py`
- `hiring_manager_calibration_agent_contract.py`
- `outreach_agent_contract.py`
- `research_agent_contract.py`
- `roi_insights_agent_contract.py`
- `scheduling_agent_contract.py`
- `sourcing_agent_contract.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
