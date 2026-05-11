# Release Notes

## [Unreleased]

### Added
- Split the recruiting-platform blueprint into repository-native docs under `docs/01_product/` through `docs/06_delivery_operations/`.
- Added `docs/master_documentation_index.md` as the primary crosswalk for humans and stateless coding agents.
- Added scaffold roots for `apps/`, `src/ai_recruiting_platform/`, `prompts/`, and `skills/`, including folder READMEs and docstring-only Python placeholder modules.
- Added project-specific package READMEs to localize future implementation ownership.
- Added repository-operational docs for troubleshooting, generated-artifact contracts, source boundaries, security hygiene, context triggers, and runtime support.
- Added initial repository workflow recipes under `context/recipes/`, prompt assets under `prompts/task_recipes/`, and project skills under `skills/project/`.
- Added CI and collaboration assets including `.gitignore`, a GitHub quality-gates workflow, runtime-specific agent instructions, and a pull-request evidence template.

### Changed
- Rewrote the root `README.md` to describe the recruiting-platform scaffold rather than the generic template.
- Updated `AGENTS.md`, `CONTRIBUTING.md`, `docs/new_user_onboarding.md`, `docs/README.md`, and `docs/agent_bootstrap/README.md` so the repo points contributors to the new operational docs, prompt recipes, and skill assets.
- Replaced the placeholder productization checklist content with prerequisite-ordered build tasks and a documentation-audit inventory.
- Updated `scripts/audit_docstrings.py`, `scripts/run_precommit_suite.py`, `scripts/README.md`, and `tests/test_audit_docstrings.py` so interrogate failures produce actionable follow-up inventory output that includes missing-docstring and scan-failure reporting.
- Updated `pyproject.toml` so static-analysis tooling covers the new `src/` and `apps/` roots and the project metadata reflects the working project identity.

### Notes
- This repository remains a scaffolded starting state. The added Python files intentionally contain narrative docstrings only and no business logic.
