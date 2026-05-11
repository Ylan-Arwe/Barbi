# Stateless coding agent handoff

**Purpose:** Explain how a stateless coding agent should read this repository, interpret the placeholders, and execute work without hidden continuity.

**Audience:** Coding agents and humans preparing tasks for them.

**How to use this document:** Use this document as the operational bridge between the repo's docs, placeholders, checklists, and wrapper-first workflow.

**Relation to the blueprint:** Derived from blueprint section 27 and the user requirement that the scaffold become agent-usable across many separate sessions.

**Relation to the repository tree:** Owns the handoff logic connecting `README.md`, `AGENTS.md`, the master documentation index, package READMEs, prompt/skill folders, and the checklist.

**Neighboring documents:**
- [AGENTS](../../AGENTS.md)
- [Master documentation index](../master_documentation_index.md)
- [Agent bootstrap playbook](../agent_bootstrap/operator_context_injection.md)
- [Code localization plan](../03_architecture/code_localization_plan.md)
- [Prompt recipes, skills, and context injection plan](../04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md)

## Concise thesis

A stateless agent succeeds here by following explicit reading order, file placement guidance, wrapper-first remediation, and checklist ordination. The repo is designed to carry continuity in docs and artifacts rather than in hidden model memory.

## Design problem this document addresses

Agents fail when they guess where work belongs, ignore prerequisites, invent dependencies, or treat placeholder modules as arbitrary text. This document prevents those failure modes from being normal.

## Reading order for agents

Recommended order:
1. `AGENTS.md`
2. `docs/master_documentation_index.md`
3. `docs/03_architecture/repository_asset_map.md`
4. `docs/03_architecture/code_localization_plan.md`
5. the domain- or workflow-specific doc relevant to the task
6. package README(s) for the target folder
7. `Final-Productization-Checklist.md`
8. the placeholder module(s) named in the checklist entry.
9. the relevant recipe under `context/recipes/` or skill under `skills/project/` when the task matches one of those workflows.

## How to treat placeholder modules

A placeholder Python file is a contract, not a completed implementation. Agents should expand the documented responsibilities in place, preserve the file's ownership boundaries, and update the relevant docs if the implementation forces a legitimate change in localization. They should not relocate logic casually because a different file feels more convenient.

## Execution expectations

Agents should:
- work top-down from the checklist and docs;
- preserve wrapper-first execution and evidence capture;
- add or refine checklist entries when new bounded work is discovered;
- avoid speculative runtime dependencies until the roadmap and checklist justify them;
- preserve candidate-rights, explainability, and evidence-backed claim discipline.

Agents should not:
- mark large feature families complete after minimal implementation;
- invent public-trust claims or legal compliance;
- bypass policy gates because the scaffold is still early.

## Phased implementation notes

Keep this document aligned with `AGENTS.md`, the master index, and package READMEs. When new roots or agent-facing assets appear, update this handoff doc in the same session so the repo stays self-orienting.
