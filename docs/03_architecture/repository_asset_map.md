# Repository asset map

**Purpose:** Give humans and agents a top-level map of where product concerns live in the repository after the scaffold conversion.

**Audience:** Any contributor entering the repo for the first time.

**How to use this document:** Use this document when you need to locate the right folder before reading a module-level placeholder or choosing a checklist task.

**Relation to the blueprint:** Synthesizes the blueprint into repository structure rather than corresponding to one single blueprint section.

**Relation to the repository tree:** Owns the top-level crosswalk between product concepts and repository paths.

**Neighboring documents:**
- [Master documentation index](../master_documentation_index.md)
- [Code localization plan](../03_architecture/code_localization_plan.md)
- [Root README](../../README.md)
- [AGENTS](../../AGENTS.md)

## Concise thesis

The repository is intentionally split so that docs explain intent, placeholders reserve implementation homes, and checklists sequence the work. This file is the fast path for orienting to that structure.

## Design problem this document addresses

A stateless agent cannot rely on hidden context or prior memory. It needs a concrete asset map that says where workflow logic, governance docs, prompts, and future app shells belong.

## Top-level folders and their jobs

Top-level ownership is:
- `docs/` for repository-native design, architecture, governance, and delivery docs;
- `apps/` for deployable surface contracts and future app entrypoints;
- `src/ai_recruiting_platform/` for product logic packages and typed internal interfaces;
- `prompts/` for future system prompts and task recipes;
- `skills/` for future reusable execution guidance and agent skills;
- existing template roots such as `scripts/`, `tests/`, `config/`, and `context/` for wrapper-first automation and generated context support.

## Why placeholders exist

The placeholder Python modules are not decorative. They localize responsibility so future agents know where to implement a feature and what neighboring modules it must coordinate with. Their docstrings define ownership, boundaries, and sequencing without pretending implementation exists yet.

## How to navigate from concept to file

Start with the workflow or product concept, move to the relevant doc family in `docs/`, then use the code localization plan and package READMEs to reach the correct placeholder module. Do not jump directly from blueprint concept to random file creation; the scaffold already names likely homes for major functionality.

## Phased implementation notes

Keep this asset map synchronized with any new top-level roots or major package reorganizations. If a new folder appears, update this document, the master index, and the checklist in the same session.
