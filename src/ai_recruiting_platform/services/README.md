# Services package

**Purpose:** Service orchestration modules that coordinate domain logic, side effects, and provider calls.

**Why this folder exists:** Use this folder for workflow orchestration and multi-module operations.

## Current assets

- `__init__.py`
- `analytics_service.py`
- `billing_service.py`
- `enrichment_service.py`
- `explainability_service.py`
- `integration_sync_service.py`
- `interview_planning_service.py`
- `job_intake_service.py`
- `notification_service.py`
- `outreach_service.py`
- `privacy_and_suppression_service.py`
- `rediscovery_service.py`
- `reply_classification_service.py`
- `scheduling_service.py`
- `scoring_service.py`
- `search_service.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
