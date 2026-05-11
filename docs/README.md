# Documentation index

Use this index to find repository-native design, governance, and operational guidance for AI Recruiting Platform (working title).

## Primary entry points

- [`master_documentation_index.md`](master_documentation_index.md): full crosswalk between docs, repo folders, and placeholder code roots.
- [`new_user_onboarding.md`](new_user_onboarding.md): practical orientation to the scaffold's current state.
- [`agent_bootstrap/README.md`](agent_bootstrap/README.md): how to generate bootstrap context and load the minimum context pack.
- [`release_notes.md`](release_notes.md): changes to repo shape, workflow, and contributor-facing behavior.
- [`troubleshooting.md`](troubleshooting.md): common wrapper/tooling failure signatures and remediation paths.

## Operational governance docs

- [`generated_artifact_contracts.md`](generated_artifact_contracts.md): commit policy for generated ledgers and local evidence.
- [`source_boundary_manifest.md`](source_boundary_manifest.md): source-versus-generated boundary classification.
- [`security_hygiene.md`](security_hygiene.md): secret-handling and local-evidence rules.
- [`context_trigger_matrix.md`](context_trigger_matrix.md): task-to-context load-order matrix for stateless workflows.
- [`runtime_target_support_matrix.md`](runtime_target_support_matrix.md): runtime support boundaries for local contributors, terminal agents, Claude, Copilot, and CI.
- [`examples/README.md`](examples/README.md): good and bad examples for checklist quality and evidence packaging.

## Documentation families

- [`01_product/README.md`](01_product/README.md): product thesis, personas, workflow, and feature priorities.
- [`02_experience/README.md`](02_experience/README.md): UX, navigation, and screen planning.
- [`03_architecture/README.md`](03_architecture/README.md): system, data, API, and file-ownership design.
- [`04_ai_automation/README.md`](04_ai_automation/README.md): AI, agent, prompt, skill, and context-injection planning.
- [`05_governance_trust/README.md`](05_governance_trust/README.md): compliance, security, candidate rights, and public-artifact planning.
- [`06_delivery_operations/README.md`](06_delivery_operations/README.md): integrations, analytics, billing, testing, operations, roadmap, and stateless-agent execution.

## Adjacent repository surfaces

- [`../AGENTS.md`](../AGENTS.md): mandatory execution policy and quality gates.
- [`../CONTRIBUTING.md`](../CONTRIBUTING.md): contributor workflow, commit/PR discipline, and evidence packaging.
- [`../scripts/README.md`](../scripts/README.md): canonical wrapper command surfaces and utilities.
- [`../context/README.md`](../context/README.md): recipe and generated-context index.
- [`../prompts/task_recipes/README.md`](../prompts/task_recipes/README.md): repository-execution prompt assets.
- [`../skills/project/README.md`](../skills/project/README.md): reusable project execution skills.
- [`../.github/workflows/quality-gates.yml`](../.github/workflows/quality-gates.yml): CI enforcement for wrapper-driven pre-commit and test suites.
- [`../.github/PULL_REQUEST_TEMPLATE.md`](../.github/PULL_REQUEST_TEMPLATE.md): PR evidence template requiring scoped commands and summary blocks.

## How this folder should be used

Read the family README for orientation, then use the master index and code localization plan to reach the right package README or placeholder module. These docs are intended to replace blueprint scavenger hunts with explicit repository guidance.
