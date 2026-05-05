# context/

Generated context payloads and derivative repository snapshots used to help agents and reviewers navigate AI Recruiting Platform (working title).

## Policy

- Treat this folder as generated-artifact staging, not as a second source of truth.
- Generated context should identify the docs and code roots it was built from.
- Do not commit large or stale generated artifacts unless a checklist task explicitly requires a reproducible snapshot.

## Expected artifact types

- JSON docstring catalogs from `scripts/aggregate_project_docstrings.py`
- targeted markdown inventories generated for review sessions
- future context bundles that summarize a route family, domain slice, or governance surface for a bounded implementation task

## Recommended generation commands

```bash
python scripts/aggregate_project_docstrings.py --root . --output context/project_docstrings_catalog.json
python scripts/audit_docstrings.py --scan-root apps --scan-root src --scan-root scripts --scan-root tests --output build/automation_contract/docstring_inventory.md
```

## Relationship to prompts and skills

- canonical repo facts belong in `docs/` and package READMEs;
- reusable execution guidance belongs in `skills/`;
- task or system prompt assets belong in `prompts/`;
- generated context bundles belong here only when they compress those canonical sources for a specific session or automation workflow.
