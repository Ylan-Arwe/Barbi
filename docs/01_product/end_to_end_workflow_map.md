# End-to-end workflow map

**Purpose:** Map the full recruiting lifecycle into concrete workflow stages, ownership boundaries, and the files that should eventually implement each stage.

**Audience:** Workflow designers, full-stack contributors, integration authors, and agents planning bounded implementation slices.

**How to use this document:** Use this document when scoping a feature lane or checking whether a proposed task actually connects to an upstream and downstream workflow rather than creating isolated functionality.

**Relation to the blueprint:** Derived from blueprint section 6 and the downstream workflow-specific sections in 17 through 18.

**Relation to the repository tree:** Crosswalks product workflow stages to route contracts in `apps/`, domain and service modules in `src/ai_recruiting_platform/`, and the execution phases in the checklist.

**Neighboring documents:**
- [Feature inventory and prioritization](../01_product/feature_inventory_and_prioritization.md)
- [Code localization plan](../03_architecture/code_localization_plan.md)
- [Integration design](../06_delivery_operations/integration_design.md)
- [Stateless coding agent handoff](../06_delivery_operations/stateless_coding_agent_handoff.md)

## Concise thesis

The platform should behave like one connected pipeline, not a cluster of disconnected recruiter tools. Each stage must persist usable state, emit events, respect permissions, and leave downstream steps in a recoverable condition.

## Design problem this document addresses

Without an explicit workflow map, agents can build screens or services that look sensible in isolation but fail to move the recruiting process forward or ignore policy gates that should have blocked the action.

## Workflow spine

The intended spine is:
workspace and access setup → integration setup → job intake → hiring-manager calibration → market feasibility and search strategy → talent search and rediscovery → profile enrichment and provenance checks → scoring and shortlist review → approved contact reveal and suppression checks → outreach sequencing and reply handling → scheduling and interviews → ATS synchronization → analytics, audit export, and continuous improvement.

Each of those stages owns both user-visible state and background operational behavior. The repository therefore localizes implementation across API routes, services, worker contracts, analytics events, and governance modules rather than a single “workflow engine” file.

## Stage-by-stage ownership

A practical ownership pattern is:
- setup, identity, and access: `domain/tenancy_and_access.py`, `api/auth_and_identity_routes.py`, future identity integration tasks;
- job and calibration flows: `domain/jobs_and_calibration.py`, `services/job_intake_service.py`, `api/jobs_routes.py`;
- search and rediscovery: `domain/search_and_rediscovery.py`, `search/`, `services/search_service.py`, `services/rediscovery_service.py`;
- profiles, provenance, and enrichment: `domain/candidate_profiles_and_talent_graph.py`, `services/enrichment_service.py`, `data_quality/`;
- scoring and explainability: `domain/scoring_and_explainability.py`, `services/scoring_service.py`, `services/explainability_service.py`, `ai/`;
- outreach and replies: `domain/outreach_and_sequences.py`, `domain/replies_and_conversations.py`, `services/outreach_service.py`, `services/reply_classification_service.py`;
- scheduling and interviews: `domain/scheduling_and_interviews.py`, `services/scheduling_service.py`, `services/interview_planning_service.py`;
- governance and audit: `domain/compliance_privacy_and_suppression.py`, `compliance/`, `audit/`, `agents/compliance_agent_contract.py`;
- integrations, analytics, and billing: the corresponding domain, service, and package modules.

## Cross-cutting workflow obligations

Every stage should eventually support the same cross-cutting obligations:
- permission checks and tenant isolation;
- audit log emission for sensitive actions;
- analytics event emission for outcome measurement;
- graceful failure handling and retry where external systems are involved;
- human review state where AI or agent actions affect material workflow decisions.

These obligations are not side notes. They are part of what makes the platform “operating system” rather than “feature inventory.”

## Phased implementation notes

Implement and test the workflow from left to right in thin vertical slices. A stage should not be considered complete until its upstream inputs, local state transitions, downstream outputs, events, and audit obligations are all represented in docs, placeholders, and checklist tasks.
