# AI Recruiting Platform (working title)
> **A wrapper-first scaffold for building a recruiter-first, evidence-backed AI recruiting operating system**

---

**Start here:** [New user onboarding](docs/new_user_onboarding.md) for a practical orientation, then [master documentation index](docs/master_documentation_index.md) for the full doc and file crosswalk.

---

## What this repository is becoming

This repository is the scaffolded starting state for an AI recruiting platform that aims to unify:

- job intake and hiring-manager calibration;
- talent search and rediscovery;
- candidate profiles, provenance, and enrichment;
- explainable scoring and governed AI support;
- outreach, replies, scheduling, and interview coordination;
- ATS, email, calendar, CRM, and developer-facing integrations;
- analytics, ROI measurement, privacy controls, and auditability.

The platform is intentionally being built with a proof-backed posture. Claims about AI, outreach automation, candidate data, and enterprise trust should only move as fast as the repository's code, logs, tests, and docs can support them.

## What exists now

This repo is still a scaffold, not a finished product. It currently includes:

- a documentation spine split from the original recruiting-platform blueprint;
- a package and app tree populated with docstring-only Python placeholders;
- a prerequisite-ordered `Final-Productization-Checklist.md`;
- the original template's wrapper-first automation, strict quality gates, and test discipline;
- prompt, skill, and context roots prepared for later build-out.

There is no real application logic yet. The purpose of this state is to make future coding sessions bounded, navigable, and explicit about where work belongs.

## Canonical reading order

1. [AGENTS.md](AGENTS.md)
2. [docs/master_documentation_index.md](docs/master_documentation_index.md)
3. [docs/03_architecture/repository_asset_map.md](docs/03_architecture/repository_asset_map.md)
4. [docs/03_architecture/code_localization_plan.md](docs/03_architecture/code_localization_plan.md)
5. [Final-Productization-Checklist.md](Final-Productization-Checklist.md)

## Prompting coding agents

### Copyable execution prompt for this project

Use the following prompt when handing work to a stateless coding agent:

```text
# Execute bounded implementation work for the AI Recruiting Platform scaffold

Read `AGENTS.md`, `docs/master_documentation_index.md`, `docs/03_architecture/repository_asset_map.md`, `docs/03_architecture/code_localization_plan.md`, and the highest-priority open entries in `Final-Productization-Checklist.md`.

Your job is to implement meaningful bounded work, not to minimally annotate the checklist.

Rules:
- Preserve wrapper-first workflow.
- Use `python scripts/run_precommit_suite.py` for quality remediation.
- Use `python scripts/run_tests.py` for tests.
- Respect checklist ordination and prerequisites.
- Expand placeholder modules in place rather than inventing new roots casually.
- Do not invent runtime dependencies, public claims, legal compliance, or finished trust artifacts.
- Keep docs, package READMEs, and checklist entries in sync with any implementation changes.
- If a task surfaces new bounded work, add a granular checklist entry with scope, context, target files, dependencies, and DONE WHEN criteria.

Before closing the session:
- run the full pre-commit wrapper;
- run the full test wrapper;
- update release notes if workflow-relevant behavior changed;
- remove completed checklist items and rewrite partial items as remaining work.
```

## Quickstart

Create and activate a virtual environment, then install development tooling:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
```

Canonical closing checks:

```bash
python scripts/run_precommit_suite.py
python scripts/run_tests.py
```

## Wrapper-first execution model

The template's execution philosophy remains in force.

- Quality remediation goes through `python scripts/run_precommit_suite.py`
- Tests go through `python scripts/run_tests.py`
- Direct `pre-commit run <hook>` or naked `pytest` bypass repository policy and should be treated as the wrong control surface

This matters because the wrappers coordinate scoped execution, skip-ledger refresh, summary artifacts, checklist validation, and repository-specific policy that direct tool calls do not preserve.

## Repository map

- `docs/`: repository-native design, architecture, governance, and delivery docs
- `apps/`: future app-surface entrypoints and contracts for API, web, worker, and extension runtimes
- `src/ai_recruiting_platform/`: internal platform package tree and placeholder ownership map
- `prompts/`: future system prompts and task recipes
- `skills/`: future reusable project and agent skills
- `context/`: generated context bundles and docstring catalogs
- `scripts/`: canonical automation wrappers and supporting quality utilities
- `tests/`: wrapper and policy verification for the repository itself
- `config/precommit_store/`: skip ledgers and cached diagnostics used by wrapper flows
- `Final-Productization-Checklist.md`: open build work, ordered by prerequisite
- `Final-Optimization-Checklist.md`: latency exceptions only

## Documentation navigation

- [docs/master_documentation_index.md](docs/master_documentation_index.md): full crosswalk
- [docs/new_user_onboarding.md](docs/new_user_onboarding.md): practical repo introduction
- [docs/01_product/README.md](docs/01_product/README.md): product intent and workflow
- [docs/03_architecture/README.md](docs/03_architecture/README.md): architecture and code placement
- [docs/04_ai_automation/README.md](docs/04_ai_automation/README.md): AI, agent, prompt, and skill planning
- [docs/05_governance_trust/README.md](docs/05_governance_trust/README.md): governance and trust posture
- [docs/06_delivery_operations/README.md](docs/06_delivery_operations/README.md): delivery, operations, and roadmap

## Dependency posture

The repo keeps template development tooling intact. Runtime dependencies for the actual recruiting platform are intentionally conservative at this stage and should be added only through checklist-driven implementation work once the corresponding framework or provider decision is explicit.

## Docstring automation support

This repository inherits two useful automation aids from the template:

- `python scripts/aggregate_project_docstrings.py` for a machine-readable catalog of Python docstrings
- `python scripts/audit_docstrings.py` for a human-readable inventory used in documentation parity review

Those scripts are especially useful here because the scaffold uses docstring-only placeholder modules to localize future implementation responsibility without pretending code exists yet.

## Release notes

Update [docs/release_notes.md](docs/release_notes.md) whenever project-facing behavior, documentation navigation, or workflow expectations change.
