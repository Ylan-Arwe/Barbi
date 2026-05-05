# Release Notes

## [Unreleased]

### Added
- Split the recruiting-platform blueprint into repository-native docs under `docs/01_product/` through `docs/06_delivery_operations/`.
- Added `docs/master_documentation_index.md` as the primary crosswalk for humans and stateless coding agents.
- Added scaffold roots for `apps/`, `src/ai_recruiting_platform/`, `prompts/`, and `skills/`, including folder READMEs and docstring-only Python placeholder modules.
- Added project-specific package READMEs to localize future implementation ownership.

### Changed
- Rewrote the root `README.md` to describe the recruiting-platform scaffold rather than the generic template.
- Updated `AGENTS.md` to preserve wrapper-first discipline while adding project-specific reading order, placeholder-file interpretation, and governance guardrails.
- Replaced the placeholder productization checklist content with prerequisite-ordered build tasks and a documentation-audit inventory.
- Updated `pyproject.toml` so static-analysis tooling covers the new `src/` and `apps/` roots and the project metadata reflects the working project identity.

### Notes
- This repository remains a scaffolded starting state. The added Python files intentionally contain narrative docstrings only and no business logic.
