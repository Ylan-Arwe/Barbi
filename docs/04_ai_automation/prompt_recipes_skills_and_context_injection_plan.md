# Prompt recipes, skills, and context injection plan

**Purpose:** Explain how future prompt artifacts, reusable skills, and generated context packs should be organized so that agents can operate on this repository without relying on hidden continuity.

**Audience:** Maintainers authoring agent instructions, prompt assets, bootstrap context, or session recipes.

**How to use this document:** Use this document when creating assets under `prompts/`, `skills/`, or `context/`, or when updating bootstrap workflows in `docs/agent_bootstrap/README.md`.

**Relation to the blueprint:** Derived from the blueprint's stateless-agent handoff expectations and the user requirement to scaffold prompt, skill, and context assets explicitly.

**Relation to the repository tree:** Owns the relationship between `prompts/`, `skills/`, `context/`, the docstring-aggregation scripts, and the documentation index.

**Neighboring documents:**
- [Agent bootstrap build plan](../agent_bootstrap/README.md)
- [Context README](../../context/README.md)
- [Agent system and governance](../04_ai_automation/agent_system_and_governance.md)
- [Stateless coding agent handoff](../06_delivery_operations/stateless_coding_agent_handoff.md)

## Concise thesis

A stateless agent needs three kinds of support: durable repository docs, reusable execution skills, and generated context packets that can compress current implementation state without hiding source-of-truth files. This plan gives each support type a home.

## Design problem this document addresses

Without an explicit plan, prompt assets, ad hoc notes, and generated context dumps tend to appear in random folders, become stale, and silently compete with canonical docs.

## Prompt asset strategy

Use `prompts/system/` for durable system-level instructions tied to platform roles or surfaces, and `prompts/task_recipes/` for bounded, copyable work recipes such as implementing a route family, auditing a trust document, or building a search service slice. Prompt assets should reference canonical docs, not replace them.

## Skill asset strategy

Use `skills/project/` for repo-specific execution skills such as wrapper-first remediation, checklist ordination, documentation parity work, and bootstrap generation. Use `skills/agents/` for agent-role skills such as governed sourcing, compliance review, or analytics interpretation. Skills should teach repeatable working methods, not store project facts that belong in docs.

## Context injection strategy

Use `context/` for generated machine-readable or human-readable context packs such as docstring catalogs, targeted module inventories, or temporary bootstrap bundles. Generated context should always identify its source inputs and should never become more authoritative than the repository files it summarizes.

The existing template scripts already support JSON docstring aggregation and markdown inventories. Future checklist work can extend that into narrower context bundles for route families, domain slices, or compliance artifacts.

## Phased implementation notes

Build prompt, skill, and context assets only when a checklist task requires them. Keep them cross-linked to the master documentation index and regenerate or revise them whenever the underlying code or docs materially change.
