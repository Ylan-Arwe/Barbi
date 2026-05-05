# Data quality package

**Purpose:** Freshness, confidence, deduplication, and merge-review contracts.

**Why this folder exists:** Use this folder for profile-quality support logic.

## Current assets

- `__init__.py`
- `deduplication_and_merge_review.py`
- `freshness_and_confidence_scoring.py`

## Responsibility boundaries

This folder should own the concerns described above and should not silently absorb unrelated responsibilities just because it is nearby. If a new file is added here, update this README and the relevant architecture or localization doc in the same session.

## Nearby related docs or modules

- `docs/03_architecture/code_localization_plan.md`
- `docs/master_documentation_index.md`
- `src/ai_recruiting_platform/README.md`
