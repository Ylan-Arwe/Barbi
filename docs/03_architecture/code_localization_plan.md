# Code localization plan

**Purpose:** Map major workflow responsibilities to the exact placeholder modules and folders where implementation should be added later.

**Audience:** Coding agents, maintainers reviewing code placement, and contributors splitting work across sessions.

**How to use this document:** Use this document before creating a new Python file or expanding a placeholder so that implementation lands in the intended file family and not in a convenient but semantically wrong location.

**Relation to the blueprint:** Synthesizes blueprint sections 11 through 18 into repository file placement guidance.

**Relation to the repository tree:** Owns the explicit crosswalk between workflow modules and the placeholder file tree under `apps/` and `src/ai_recruiting_platform/`.

**Neighboring documents:**
- [Repository asset map](../03_architecture/repository_asset_map.md)
- [End-to-end workflow map](../01_product/end_to_end_workflow_map.md)
- [Prompt recipes, skills, and context injection plan](../04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md)
- [Final Productization Checklist](../../Final-Productization-Checklist.md)

## Concise thesis

One of the main goals of this scaffold is to stop future agents from inventing file placement. Work should expand the documented placeholders before new roots are created.

## Design problem this document addresses

Even a strong blueprint fails as an execution substrate if it does not tell contributors where functions, services, schemas, agents, integrations, and analytics responsibilities should live.

## Localization rules

Use these rules before writing code:
- domain modules own invariant business concepts and lifecycle state, not framework glue;
- service modules orchestrate domain behavior, integration calls, and side effects;
- route modules expose transport-layer contracts and permission boundaries;
- schema modules define request, response, and event typing;
- `ai/` owns gateway, registry, evaluation, and ranking contracts;
- `agents/` own governed agent definitions and permissions;
- `integrations/` own provider abstractions and connector contracts;
- `analytics/`, `audit/`, `billing/`, `notifications/`, and `data_quality/` own their corresponding cross-cutting systems.

## Workflow-to-module crosswalk

Representative mappings:
- job intake and calibration → `domain/jobs_and_calibration.py`, `services/job_intake_service.py`, `schemas/jobs_schemas.py`, `api/jobs_routes.py`;
- candidate profile assembly → `domain/candidate_profiles_and_talent_graph.py`, `services/enrichment_service.py`, `data_quality/*`, `schemas/candidates_schemas.py`;
- search and rediscovery → `domain/search_and_rediscovery.py`, `search/*`, `services/search_service.py`, `services/rediscovery_service.py`, `api/search_routes.py`;
- scoring and explainability → `domain/scoring_and_explainability.py`, `ai/ranking_and_matching_contract.py`, `services/scoring_service.py`, `services/explainability_service.py`, `api/scoring_routes.py`;
- outreach and replies → `domain/outreach_and_sequences.py`, `domain/replies_and_conversations.py`, `services/outreach_service.py`, `services/reply_classification_service.py`, `api/outreach_routes.py`;
- scheduling and interviews → `domain/scheduling_and_interviews.py`, `services/scheduling_service.py`, `services/interview_planning_service.py`, `api/scheduling_routes.py`;
- privacy, suppression, and audit → `domain/compliance_privacy_and_suppression.py`, `compliance/*`, `audit/*`, `api/compliance_routes.py`;
- integrations and sync → `domain/integrations_and_sync.py`, `integrations/*`, `services/integration_sync_service.py`, `api/integrations_routes.py`;
- analytics and billing → the corresponding domain, service, package, and route modules.

## When new files are justified

Create a new file only when:
- the responsibility does not fit an existing placeholder without violating boundaries;
- the new file has a clear neighbor set and checklist task;
- the package README and this localization plan are updated in the same session.

Otherwise, extend the existing placeholder and keep the repo's conceptual map stable.

## Phased implementation notes

Treat this file as a hard placement guide. If implementation pressure suggests a different file structure, update this plan first and explain why the original localization no longer fits.
