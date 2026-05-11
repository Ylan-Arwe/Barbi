# Task recipe prompts

This folder contains copy-ready prompt assets for bounded repository workflows.

## Available assets

- `repo_audit_prompt.md`: full repository audit of docs plus implementation parity.
- `quality_remediation_prompt.md`: wrapper-first remediation for lint, type, security, and policy failures.
- `checklist_audit_prompt.md`: backlog hygiene and dependency-order audit.
- `pr_evidence_packaging_prompt.md`: prepare review notes with wrapper summary-block evidence.
- `scaffold_bootstrap_prompt.md`: first-session orientation and validation prompt for this scaffolded repository.

## How to use these prompts

1. Choose the prompt that matches your task objective.
2. Read the prompt's ingestion order and load the named files before running commands.
3. Execute only canonical wrapper commands from `scripts/`.
4. Capture evidence from `build/automation_contract/` and close or rewrite checklist entries.

## Closure requirement

A prompt run is complete only when required wrappers were executed with canonical syntax, unresolved issues were moved into granular checklist entries when necessary, and final evidence blocks were captured from `build/automation_contract/`.
