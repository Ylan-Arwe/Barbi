# New user onboarding: AI Recruiting Platform (working title)

This repository is the scaffolded starting state for building an AI recruiting platform while preserving the original template's wrapper-first discipline, strict quality gates, and carry-forward checklist workflow.

## What exists now

The repo currently contains:
- rewritten root docs and a documentation spine split out of the recruiting-platform blueprint;
- a master documentation index for human and agent navigation;
- placeholder Python modules with docstrings that reserve implementation ownership;
- initial project-execution prompt recipes, session recipes, and skill assets for stateless work;
- generated-artifact governance docs covering local evidence, committed ledgers, and source boundaries;
- the original wrapper-first automation and test discipline from the template.

The repo does **not** yet contain business logic, working runtime surfaces, or completed external trust artifacts. Treat it as an implementation-ready scaffold, not a finished product.

## Read first

1. `README.md`
2. `AGENTS.md`
3. `docs/agent_bootstrap/operator_context_injection.md`
4. `docs/master_documentation_index.md`
5. `docs/03_architecture/repository_asset_map.md`
6. `docs/03_architecture/code_localization_plan.md`
7. `Final-Productization-Checklist.md`

After that, read the domain-specific docs and package READMEs that match your task.

## Canonical working commands

Use the existing wrappers and quality rules:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt

python scripts/run_precommit_suite.py
python scripts/run_tests.py
```

While iterating on a subset of files, keep using targeted wrapper runs rather than direct tool invocations:

```bash
python scripts/run_precommit_suite.py --scope paths --paths <file1> <file2>
python scripts/run_tests.py --scope paths --select <pytest-selector>
```

## Operational guidance surfaces

Use these docs when you need workflow help instead of guessing:

- `docs/troubleshooting.md` for wrapper/tooling failure signatures and recovery paths.
- `docs/security_hygiene.md` for secrets, local evidence, and deny-path rules.
- `docs/generated_artifact_contracts.md` and `docs/source_boundary_manifest.md` for commit-boundary decisions.
- `docs/context_trigger_matrix.md` for workflow-specific context loading.
- `prompts/task_recipes/` and `context/recipes/` for copy-ready repo workflow recipes.
- `skills/project/` for reusable `SKILL.md` playbooks.

## How the scaffold is organized

- `docs/`: execution-facing knowledge base split from the blueprint.
- `apps/`: deployable app-surface contracts for web, API, worker, and extension runtimes.
- `src/ai_recruiting_platform/`: internal platform package scaffold.
- `prompts/`: system-prompt placeholders plus repository-execution task recipes.
- `skills/`: reusable project and agent skill assets.
- `context/`: generated docstring catalogs and reusable session recipes.
- `scripts/`: canonical automation wrappers and support utilities.
- `config/precommit_store/`: wrapper-managed ledgers and cached diagnostics.

## What not to assume

Do not assume:
- the placeholder modules imply completed runtime behavior;
- runtime dependencies beyond the current tooling set are approved;
- privacy, explainability, auditability, or security claims are complete just because the docs plan for them;
- direct `pytest` or `pre-commit run <hook>` calls are acceptable substitutes for the wrappers.
