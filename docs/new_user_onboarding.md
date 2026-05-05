# New user onboarding: AI Recruiting Platform (working title)

This repository is no longer a generic coding-agent template. It is now the scaffolded starting state for building an AI recruiting platform while preserving the template's wrapper-first discipline, strict quality gates, and carry-forward checklist workflow.

## What exists now

The repo currently contains:
- rewritten root docs and a documentation spine split out of the recruiting-platform blueprint;
- a master documentation index for human and agent navigation;
- placeholder Python modules with docstrings that reserve implementation ownership;
- major folder READMEs for new code, prompt, and skill roots;
- an expanded productization checklist ordered by prerequisite;
- the original wrapper-first automation and test discipline from the template.

The repo does **not** yet contain business logic, working runtime surfaces, or completed external trust artifacts. Treat it as an implementation-ready scaffold, not a finished product.

## What to read first

1. `README.md`
2. `AGENTS.md`
3. `docs/master_documentation_index.md`
4. `docs/03_architecture/repository_asset_map.md`
5. `docs/03_architecture/code_localization_plan.md`
6. `Final-Productization-Checklist.md`

After that, read the domain-specific docs and package READMEs that match your task.

## How to work inside this repo

Use the template's existing wrappers and quality rules:
```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt

python scripts/run_precommit_suite.py
python scripts/run_tests.py
```

While iterating on a subset of files, keep using targeted wrapper runs rather than direct tool invocations. The repo still depends on wrapper-managed manifests, summary artifacts, and policy enforcement.

## How the new scaffold is organized

- `docs/`: the execution-facing knowledge base split from the blueprint.
- `apps/`: deployable app-surface contracts for web, API, worker, and extension runtimes.
- `src/ai_recruiting_platform/`: the internal package tree where future implementation belongs.
- `prompts/`: future prompt assets and reusable task recipes.
- `skills/`: future project and agent skills.
- `context/`: generated context bundles and docstring catalogs.

## What not to assume

Do not assume:
- a final frontend or backend framework has already been selected;
- runtime dependencies beyond the template tooling are approved;
- compliance or security artifacts already exist just because the docs describe them;
- a placeholder module means the behavior is implemented.

Use the checklist and roadmap to determine what work is still open. If a needed step is missing, add a bounded checklist entry instead of improvising hidden project law.
