# AI Recruiting Platform (working title) Agent Charter

**Scope:** Applies to the entire repository unless a deeper `AGENTS.md` overrides it.

## Authoritative reading order for this repository

When entering the repo for the first time, read in this order:

1. `AGENTS.md`
2. `docs/master_documentation_index.md`
3. `docs/03_architecture/repository_asset_map.md`
4. `docs/03_architecture/code_localization_plan.md`
5. the workflow- or domain-specific doc relevant to the task
6. the target package or folder `README.md`
7. `Final-Productization-Checklist.md`

Use the root `README.md` and `docs/new_user_onboarding.md` for orientation, but treat this file and the master index as the main operating law for agents.

## Baseline conduct
- Write in American English and save files as UTF-8.
- Do not commit binary assets (screenshots, videos, archives). Share them separately in the session summary if needed.
- Mandatory quality gates: Ruff (format + lint, width 120), Pylint, Interrogate (100% docstring coverage), MyPy, Pyright, Deptry, Vulture, and Bandit. Never skip, weaken, or reconfigure them.
- It is **MANDATORY** that you use `scripts/run_precommit_suite.py` and not just individual invocations of tools for remediation and that you submit `.json` assets that change during your session so our script and filter do not become stale.
- The percentage notice shown by `scripts/run_precommit_suite.py` is convenience output, not a reason to interrupt the runner. Do **NOT** treat a stale percent estimate as evidence of a hang.
- Respect checklist ordination. If task `y` depends on task `x`, addressing `y` first is a policy violation even if `y` appears more interesting.
- Preserve the template's wrapper-first operating model. This repo is a project-specific scaffold, not a new excuse to invent a different process philosophy.

## Project-specific guardrails
- The project name in repository docs is a working title. Do not invent a canonical brand, founder story, certification status, or benchmark claim unless the repo later adds reviewed evidence.
- Treat placeholder Python files as ownership contracts. Expand them in place unless a documented architecture change justifies a new file or package.
- Do not present privacy, compliance, candidate-rights, or security readiness as complete unless the relevant controls, tests, logs, and docs exist.
- Do not build outreach automation before suppression, unsubscribe, and privacy-state handling is designed for that workflow slice.
- Do not build screening or ranking logic without explainability, evidence references, and human-review state.
- Do not turn internal planning docs into public-trust claims by implication. Internal readiness language must stay clearly internal until public artifacts are deliberately created.
- When implementing AI or agent behavior, preserve evidence-backed outputs, explicit permissions, audit logs, and kill-switch or approval semantics where the docs require them.

## Placeholder-file interpretation
- A placeholder module containing only a docstring is a valid scaffold asset.
- Its docstring identifies the responsibilities that belong there, likely collaborators, likely public functions or classes, and sequencing notes.
- Future implementation should fill that file instead of moving its responsibilities into a convenient unrelated module.
- If implementation pressure reveals that a placeholder boundary is wrong, update:
  1. the placeholder file;
  2. the nearest package `README.md`;
  3. `docs/03_architecture/code_localization_plan.md`;
  4. any affected checklist entries.

## **MANDATORY TIME AND DATE POLICY**
- Derive timestamps or datestamps from **Git metadata** or another trusted repository or workflow source whenever available.
- You **MUST NOT** rely on an unsynchronized model clock for naming folders, dating entries, or rewriting time-sensitive provenance.
- If no trusted source is available, prefer undated wording over invented precision.

## Quality workflow
1. **While iterating, refresh the skip manifests for every touched file.**
   - Canonical command: `python scripts/run_precommit_suite.py --scope paths --paths <file1> <file2>`
   - Run a single hook in targeted mode with `python scripts/run_precommit_suite.py --only <hook> --scope paths --paths <file1> <file2>`.
   - Run a whole-project sweep with `python scripts/run_precommit_suite.py --scope all`.
   - Useful switches:
     - `--only <hook>` to focus on a single tool.
     - `--scope changed --diff-target <ref>` to scan staged or untracked changes versus a branch.
     - `--reset-baseline` to rebuild each manifest from tracked Python sources, clear all skip flags, and reseed the ledger.
     - `--filter-mode full` or `WRAPPER_NO_CACHE=1` to bypass the skip cache temporarily.
   - Each hook stores state in `config/precommit_store/<hook>.json`. New paths appear automatically with `"skip": "N"`. Passing runs flip the entry for a file to `"skip": "Y"`.
   - Manual hook aliases route back to `scripts/run_precommit_suite.py`. Use the unified runner instead of direct hook calls.
   - If you cancel the unified pre-commit runner before it completes, restart it later so the JSON ledger reflects a real attempt.
   - Remediation means fixing the files surfaced by the hook output. Never edit tool settings, ignore lists, or JSON manifests to hide failures.
- Never hand-edit `config/precommit_store/*.json`; use the runner to reset flags instead.
- Pylint failures are cached in `config/precommit_store/pylint_failures.json`. Commit the updated failure manifest when the runner changes it so later agents see consistent cached output.

2. **Session close:** run the complete automation suites back-to-back before summarizing or opening a PR:
   - `python scripts/run_precommit_suite.py`
   - `python scripts/run_tests.py`

3. **Capture the result blocks, not progress logs.**
   - Each suite writes a ready-to-copy snippet under `build/automation_contract/`.
   - When copying directly from the terminal, start at the final line and select upward until you include the banner and table.
   - Do **not** clip intermediate progress output.

## Testing expectations
- Run the pytest scope that covers the code you changed using `python scripts/run_tests.py`.
- If you modify a test file or create a new test, the per-test latency budget remains 0.20 seconds unless a justified entry is added to `Final-Optimization-Checklist.md`.
- Do not modify `Final-Optimization-Checklist.md` for unchanged tests unless specifically directed.
- New workflow slices should add the tests, mocks, or eval coverage appropriate to their risk profile. “Code exists” is not sufficient evidence of completion.

## Checklist policy
- Surface unresolved quality, tooling, implementation, documentation, or release-readiness work in `Final-Productization-Checklist.md`.
- New checklist tasks must stay granular, prerequisite-ordered, and explicit about scope, context, target files, dependencies, and `DONE WHEN` criteria.
- Do not collapse many future steps into one oversized checklist entry.
- When you partially complete a task, rewrite the entry as the remaining bounded work instead of appending a progress diary.
- If new work appears because of a code or doc change, add it to the checklist before ending the session.

## Documentation and continuity policy
- `docs/master_documentation_index.md` is the canonical crosswalk between docs and file roots.
- Folder-level `README.md` files under `apps/`, `src/`, `prompts/`, `skills/`, `context/`, and the docs families are part of the execution surface. Keep them current.
- Update `docs/release_notes.md` whenever workflow-relevant, user-facing, or repo-navigation behavior changes.
- Keep internal docs honest about scaffold status. Do not rewrite planned behavior as implemented fact.
- Use the docstring tooling when you need a compact implementation snapshot:
  - `python scripts/aggregate_project_docstrings.py`
  - `python scripts/audit_docstrings.py`

## Project-sensitive caution zones
- Candidate identity, contact data, consent, suppression state, privacy requests, and rights workflows are sensitive and must be handled accordingly.
- AI-generated summaries, scores, rankings, and agent actions require evidence, versioning, and review controls where the docs indicate.
- Outreach, scheduling, integrations, and analytics all need audit and operations signals, not just happy-path logic.
- Public-facing trust, security, or compliance artifacts should only be added when their underlying evidence is real.

## Operational hygiene
- Keep manifests, release indexes, and evidence logs consistent with your edits.
- If a new top-level or major subfolder is added, it must receive an accurate `README.md`.
- If package or route ownership changes, update the code localization plan and package README in the same session.

These directives keep human and agent contributors aligned while the scaffold turns into a real platform.
