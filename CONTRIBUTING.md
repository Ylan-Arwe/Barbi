# Contributing

This repository is the scaffolded starting state for AI Recruiting Platform (working title). It preserves the original template's wrapper-first automation and quality discipline while adding project-specific docs, placeholder modules, and build sequencing guidance.

All contributors must follow [AGENTS.md](AGENTS.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Local setup

1. Create and activate a Python 3.13 virtual environment (the repository pins `>=3.13,<3.14`).
2. Install the shared development tooling:
   ```bash
   python -m pip install --upgrade pip
   python -m pip install -r requirements-dev.txt
   ```
3. Optionally install Git hooks:
   ```bash
   pre-commit install
   ```

## Read before editing

A new contributor should read, in order:

1. `README.md`
2. `AGENTS.md`
3. `docs/master_documentation_index.md`
4. `docs/03_architecture/repository_asset_map.md`
5. `docs/03_architecture/code_localization_plan.md`
6. `Final-Productization-Checklist.md`

Do not start by improvising file placement from the blueprint or from memory. The scaffold already localizes where work belongs.

## Required quality workflow

### While iterating on a subset of files

Run the targeted pre-commit suite for every file you touch:

```bash
python scripts/run_precommit_suite.py --scope paths --paths <file1> <file2>
```

You can focus on a single hook with:

```bash
python scripts/run_precommit_suite.py --only <hook> --scope paths --paths <file1> <file2>
```

### Before opening a pull request or closing a session

Run the full automation sequence in this order:

```bash
python scripts/run_precommit_suite.py
python scripts/run_tests.py
```

Each runner writes a copy-ready summary block under `build/automation_contract/`. Use those blocks in review summaries instead of partial progress logs.

## Project-specific implementation expectations

- Expand placeholder Python modules in place rather than creating new roots casually.
- Keep package READMEs, architecture docs, and checklist entries synchronized with implementation changes.
- Do not add runtime dependencies, public claims, or compliance assertions speculatively.
- Treat candidate rights, suppression, explainability, and auditability as build constraints, not backlog decoration.

## Release notes and docs

Update [docs/release_notes.md](docs/release_notes.md) whenever project-facing behavior or workflow expectations change. If implementation forces a change in file ownership or roadmap order, update the relevant doc in `docs/` and the affected package README in the same session.
