# Agent bootstrap build plan

This folder documents how to generate bootstrap context for AI Recruiting Platform (working title) from the repository itself.

## Purpose

Bootstrap artifacts should help a stateless coding agent understand current implementation claims, workflow policy, and documentation structure without replacing the source-of-truth files in the repo.

## Current bootstrap inputs

- `scripts/aggregate_project_docstrings.py`: exports a machine-readable JSON catalog of Python module, class, and function docstrings.
- `scripts/audit_docstrings.py`: produces a markdown inventory that is useful for parity review and interrogate remediation.
- `docs/master_documentation_index.md`: the main crosswalk from docs to code roots.
- `docs/agent_bootstrap/operator_context_injection.md`: mandatory workflow playbook for wrapper syntax, evidence packaging, and timestamp hygiene.
- package and folder `README.md` files under `apps/`, `src/`, `prompts/`, `skills/`, `context/`, and `docs/`.

## Recommended bootstrap workflow

1. Generate a docstring catalog:
   ```bash
   python scripts/aggregate_project_docstrings.py --root . --output context/project_docstrings_catalog.json
   ```
2. Generate a markdown inventory for review:
   ```bash
   python scripts/audit_docstrings.py --scan-root scripts --scan-root tests --output build/automation_contract/docstring_inventory.md
   ```
3. Pair the generated artifacts with:
   - `docs/master_documentation_index.md`
   - `docs/agent_bootstrap/operator_context_injection.md`
   - the domain or workflow doc relevant to the task
   - the package README for the target folder
   - the current checklist entry being worked

## Operational prompt, recipe, and skill assets

- `prompts/task_recipes/`: copy-ready repository-execution prompt assets for repo audits, quality remediation, checklist audits, PR evidence packaging, and scaffold bootstrap.
- `context/recipes/`: wrapper-first session recipes for remediation, documentation parity, release prep, and PR evidence packaging.
- `skills/project/`: reusable `SKILL.md` playbooks for high-frequency project workflows.

These assets are advisory guidance stored in source control. They do not replace `AGENTS.md`, wrapper output, or the checklist.

## Related governance references

- `../troubleshooting.md`: wrapper-failure signatures and remediation paths.
- `../generated_artifact_contracts.md`: commit policy for generated artifacts and local evidence.
- `../source_boundary_manifest.md`: source-versus-local boundary classification.
- `../context_trigger_matrix.md`: workflow-to-context load-order matrix.
- `../runtime_target_support_matrix.md`: runtime support boundaries.
