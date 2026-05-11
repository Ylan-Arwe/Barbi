# Prompt library

This folder stores durable prompt assets that belong in the repository rather than in chat history or checklist prose.

## Current structure

- `system/`: product- or surface-level system prompts that should ship with the platform once implemented.
- `task_recipes/`: copy-ready repository-execution prompt recipes for audits, remediation loops, PR evidence packaging, and scaffold bootstrap.

## Usage rules

- Prompt assets should reference canonical docs instead of replacing them.
- Repository-execution prompt recipes must preserve wrapper-first commands and checklist governance from `AGENTS.md`.
- If a prompt asset changes contributor workflow or makes new repo claims, update `docs/release_notes.md` and the relevant docs in the same session.
