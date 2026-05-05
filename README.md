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
# Execute tasks and ensure no precommit script hook violations in project, maintain parity with documentation
* Read `AGENTS.md`, `docs/master_documentation_index.md`, `docs/03_architecture/repository_asset_map.md`, `docs/03_architecture/code_localization_plan.md`, and the highest-priority open entries in `Final-Productization-Checklist.md`.
* Address tasks described in `Final-Productization-Checklist.md` through remediation/implementation of described issues/goals to the maximum extent allowed by your session (no minimal executions, genuinely address a significant scope, not just checklist updates or diagnostics)  

## Following directives in `AGENTS.md` about pre-commit syntax, perform tasks as below
* Address tasks in `Final-Productization-Checklist.md`, starting with the tasks that must be completed before future tasks and implementation can be addressed.
* Diagnose/Resolve any surfacing failures/warnings/errors related to your execution to keep our progress momentum on any backlog of pre-commit violations.
* If you see multiple checklist entries or items that are easily combined into a single execution, it's helpful to address as many as you can in order to reduce the total number of needed sessions. 
* If you need to break a task into pieces and create new checklist entries for other agents to pick up where you left off, it's permitted, but make a genuine effort to complete work and address as many files as possible listed in the current phase, where possible.
* If, during the course of your work, you discover something that needs implementation, isn't working how it should be, or clearly is just a scaffolded idea that isn't been finished with logic, create new checklist entries for that surfaced task/gap, etc, as well.
* Pay attention to ordinality of tasks. If a task that's lower in the checklist depends on other checklist items to be complete to wire it properly, **DO NOT PROCESS THAT TASK FIRST** 
* If completion of your current task then adds more granularity to an existing checklist entry, update it, if completion surfaces a need for further implementation or steps, ensure that actionable checklist entry is created. 
* DO NOT TAKE SHORTCUTS when addressing problems or implementing design. Remediate issues properly, not by just circumventing or shimming around a problem, our suite is designed to surface problems, you are to remediate those problems, not simply silence warnings, errors, or failures, when something needs addressing. If you find such a workaround in use and a genuine problem is being hidden, remove whatever is silencing warnings, errors, or failures. 
* Only work on `Final-Optimization-Checklist.md` tasks if entries there indicate no current optimization and they exceed a latency budget of 0.30 s, unless directed to, specifically.
* As long as entries exist for tests above the latency budget, do not update them unless you are working on them. Rationale: This keeps you from "updating test times" and calling this an execution.
* Tests may ONLY be marked slow or to skip if rationale and justification is surfaced in `Final-Optimization-Checklist.md`. If you find something undocumented, document it, or release the skip or slow marker so it can be surfaced for remediation.

### Finishing Your Session
* Ensure you've removed checklist entries for completed work or stale entries, transforming entries that are partially addressed into what remains to be done rather than annotation of partial progress, which can lead to task churn. Ensure any updates to existing checklist entries that are affected by your execution are made and that any new tasks that have become evident from your execution are likewise created in the checklist for iterative-progress, needed improvements, and quality documentation.
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
