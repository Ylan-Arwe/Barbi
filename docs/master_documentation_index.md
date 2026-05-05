# Master documentation index

This file is the main crosswalk between repository docs, placeholder code roots, and the open build checklist for AI Recruiting Platform (working title).

## What this index is for

Use this file when you need to answer one of three questions quickly:
1. Which document should I read next?
2. Which folder should own the work?
3. What other docs or modules must stay synchronized when I change something?

The blueprint remains the upstream planning source, but the repository docs listed here are the working execution layer for humans and stateless coding agents.

## Start here

- [Root README](../README.md): project summary, quickstart, wrapper policy, and copyable coding-agent prompt.
- [New user onboarding](new_user_onboarding.md): practical explanation of repo state and reading order.
- [AGENTS](../AGENTS.md): mandatory workflow rules, quality gates, checklist ordination, and project-specific guardrails.
- [Final Productization Checklist](../Final-Productization-Checklist.md): open bounded work.
- [Final Optimization Checklist](../Final-Optimization-Checklist.md): only for latency-budget exceptions.

## Recommended reading order for humans

1. `README.md`
2. `docs/new_user_onboarding.md`
3. `AGENTS.md`
4. `docs/01_product/platform_overview_and_build_thesis.md`
5. `docs/01_product/end_to_end_workflow_map.md`
6. `docs/02_experience/ux_specification.md` and `docs/02_experience/information_architecture_and_navigation.md`
7. `docs/03_architecture/system_architecture.md`, `docs/03_architecture/repository_asset_map.md`, and `docs/03_architecture/code_localization_plan.md`
8. `docs/04_ai_automation/` and `docs/05_governance_trust/` docs that relate to your work
9. `docs/06_delivery_operations/implementation_roadmap_and_phase_plan.md`
10. `Final-Productization-Checklist.md`

## Recommended reading order for stateless coding agents

1. `AGENTS.md`
2. `docs/master_documentation_index.md`
3. `docs/03_architecture/repository_asset_map.md`
4. `docs/03_architecture/code_localization_plan.md`
5. the domain or workflow doc relevant to the target checklist entry
6. the package README for the target folder under `apps/`, `src/`, `prompts/`, or `skills/`
7. `Final-Productization-Checklist.md`
8. the placeholder module(s) named in the checklist entry

## Documentation inventory

| Path | What it is for | Why it matters |
| --- | --- | --- |
| `docs/01_product/end_to_end_workflow_map.md` | End-to-end workflow map | Connected workflow from setup through ROI and governance. |
| `docs/01_product/feature_inventory_and_prioritization.md` | Feature inventory and prioritization | Feature families grouped by launch band and dependency order. |
| `docs/01_product/platform_overview_and_build_thesis.md` | Platform overview and build thesis | High-level product thesis and repo discipline. |
| `docs/01_product/product_principles_personas_and_jobs.md` | Product principles, personas, and jobs | Principles and persona constraints translated into implementation behavior. |
| `docs/02_experience/information_architecture_and_navigation.md` | Information architecture and navigation | Navigation groups and role-aware route ownership. |
| `docs/02_experience/screen_inventory.md` | Screen inventory | Screen families and their intended code ownership. |
| `docs/02_experience/ux_specification.md` | UX specification | Recruiter-first UX posture and interaction rules. |
| `docs/03_architecture/api_design_and_webhooks.md` | API design and webhooks | Route philosophy, schema rules, and webhook expectations. |
| `docs/03_architecture/code_localization_plan.md` | Code localization plan | Explicit mapping from workflow responsibilities to placeholder files. |
| `docs/03_architecture/data_model_and_domain_objects.md` | Data model and domain objects | Domain aggregates, boundary rules, and privacy-sensitive object families. |
| `docs/03_architecture/repository_asset_map.md` | Repository asset map | Top-level folder crosswalk for humans and agents. |
| `docs/03_architecture/system_architecture.md` | System architecture | Runtime layers, control flow, and component separation. |
| `docs/03_architecture/technology_architecture.md` | Technology architecture | Stack direction, dependency policy, and explicit undecided areas. |
| `docs/04_ai_automation/agent_system_and_governance.md` | Agent system and governance | Governed agent operating model and controls. |
| `docs/04_ai_automation/ai_ml_design.md` | AI and ML design | Allowed AI behavior, evidence obligations, and guardrail posture. |
| `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md` | Prompt recipes, skills, and context injection plan | How prompts, skills, and generated context should be organized. |
| `docs/05_governance_trust/compliance_privacy_and_ai_governance.md` | Compliance, privacy, and AI governance | Governance constraints for privacy, AI, and evidence-backed claims. |
| `docs/05_governance_trust/documentation_launch_and_public_artifacts.md` | Documentation, launch, and public artifacts | Plan for public, buyer, and launch-facing artifacts. |
| `docs/05_governance_trust/security_trust_and_candidate_rights.md` | Security, trust, and candidate rights | Security posture, trust-center expectations, and candidate-rights principles. |
| `docs/06_delivery_operations/analytics_and_roi_measurement.md` | Analytics and ROI measurement | Metric taxonomy, event design, and ROI evidence posture. |
| `docs/06_delivery_operations/billing_packaging_and_usage.md` | Billing, packaging, and usage | Plans, entitlements, and usage-meter design. |
| `docs/06_delivery_operations/implementation_roadmap_and_phase_plan.md` | Implementation roadmap and phase plan | Phase narrative that matches the current scaffold state. |
| `docs/06_delivery_operations/integration_design.md` | Integration design | Connector, mapping, sync, and admin-debugging design. |
| `docs/06_delivery_operations/observability_operations_and_support.md` | Observability, operations, and support | Signals, runbooks, and support-readiness expectations. |
| `docs/06_delivery_operations/stateless_coding_agent_handoff.md` | Stateless coding agent handoff | Operational instructions for stateless agent navigation and execution. |
| `docs/06_delivery_operations/testing_quality_assurance_and_eval_strategy.md` | Testing, quality assurance, and eval strategy | Quality strategy spanning static checks, tests, and AI evals. |

## Crosswalk from documentation families to repo folders

| Documentation family | Primary docs | Primary repo roots | Typical implementation homes |
| --- | --- | --- | --- |
| Product and workflow intent | `docs/01_product/` | `docs/02_experience/`, `docs/03_architecture/` | `src/ai_recruiting_platform/domain/`, `services/`, `apps/web/` |
| Experience and screen planning | `docs/02_experience/` | `apps/web/`, `apps/extension/` | `src/ai_recruiting_platform/api/`, `schemas/`, `services/` |
| System, data, API, and file ownership | `docs/03_architecture/` | `apps/`, `src/ai_recruiting_platform/` | `domain/`, `api/`, `schemas/`, `integrations/`, `analytics/`, `audit/` |
| AI, agents, prompts, and skills | `docs/04_ai_automation/` | `src/ai_recruiting_platform/ai/`, `agents/`, `prompts/`, `skills/`, `context/` | `services/`, `audit/`, `analytics/` |
| Governance, trust, and launch discipline | `docs/05_governance_trust/` | `src/ai_recruiting_platform/compliance/`, `audit/` | `apps/web/`, future public-artifact work` |
| Delivery, integrations, analytics, roadmap | `docs/06_delivery_operations/` | `integrations/`, `analytics/`, `billing/`, `notifications/` | `apps/api/`, `apps/worker/`, checklist phases` |

## Folder-level orientation paths

- [apps/README.md](../apps/README.md): deployable surface contracts and future app entrypoints.
- [src/README.md](../src/README.md): internal platform package map.
- [prompts/README.md](../prompts/README.md): future system prompts and task recipes.
- [skills/README.md](../skills/README.md): future reusable execution skills.
- [context/README.md](../context/README.md): generated context artifacts and bootstrap policy.
- [docs/agent_bootstrap/README.md](agent_bootstrap/README.md): how to generate bootstrap context from the repo itself.

## Synchronization rule

When a change affects project behavior, update:
1. the implementation file or placeholder owner;
2. the nearest package README;
3. the nearest architecture or workflow doc;
4. the checklist if open work remains;
5. release notes when the change is user-facing or workflow-relevant.

This is how the repository stays navigable for contributors who do not retain hidden continuity.
