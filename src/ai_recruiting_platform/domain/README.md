# Domain package

**Purpose:** Core business concepts, lifecycle states, and invariant-bearing domain objects.

**Why this folder exists:** Use this folder for business rules and state transitions rather than route glue or provider calls.

## Current assets

- `__init__.py`
- `analytics_and_roi.py`
- `audit_and_provenance.py`
- `billing_and_entitlements.py`
- `candidate_profiles_and_talent_graph.py`
- `compliance_privacy_and_suppression.py`
- `integrations_and_sync.py`
- `jobs_and_calibration.py`
- `outreach_and_sequences.py`
- `replies_and_conversations.py`
- `scheduling_and_interviews.py`
- `scoring_and_explainability.py`
- `search_and_rediscovery.py`
- `tenancy_and_access.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
