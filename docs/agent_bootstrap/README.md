# Agent bootstrap build plan

This folder documents how to generate bootstrap context for AI Recruiting Platform (working title) from the repository itself.

## Purpose

Bootstrap artifacts should help a stateless coding agent understand current implementation claims and documentation structure without replacing the source-of-truth files in the repo.

## Current bootstrap inputs

- `scripts/aggregate_project_docstrings.py`: exports a machine-readable JSON catalog of Python module, class, and function docstrings.
- `scripts/audit_docstrings.py`: produces a markdown inventory that is useful for parity review.
- `docs/master_documentation_index.md`: the main crosswalk from docs to code roots.
- package and folder `README.md` files under `apps/`, `src/`, `prompts/`, `skills/`, `context/`, and `docs/`.

## Recommended bootstrap workflow

1. Generate a docstring catalog:
   ```bash
   python scripts/aggregate_project_docstrings.py --root . --output context/project_docstrings_catalog.json
   ```
2. Generate a markdown inventory for review:
   ```bash
   python scripts/audit_docstrings.py --scan-root apps --scan-root src --scan-root scripts --scan-root tests --output build/automation_contract/docstring_inventory.md
   ```
3. Pair the generated artifacts with:
   - `docs/master_documentation_index.md`
   - the domain or workflow doc relevant to the task
   - the package README for the target folder
   - the current checklist entry being worked

## What should be added later

Future checklist work should add narrower bootstrap bundles for:
- route-family context;
- domain-module context;
- compliance and trust-center artifact context;
- prompt and skill indexes for specific agent roles.

Generated artifacts should remain derivative and clearly identify their source inputs.
