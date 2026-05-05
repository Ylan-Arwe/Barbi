# Final Productization Checklist

**Use this file to track unresolved quality, tooling, or release-readiness work that should be carried into a later session.**

# **MANDATORY CHECKLIST POLICY**
**FOLLOW THE BELOW DIRECTIVES WHEN ADDRESSING *ANY* ENTRY BELOW**
- Record only open work. When a task is finished, **delete it** so only unresolved entries remain.
- Rewrite partially completed tasks as explicit, actionable “remaining work” items.
- Run remediation loops through `python scripts/run_precommit_suite.py` (never direct hook calls).
- Source of truth for current pylint diagnostics is `config/precommit_store/pylint_failures.json`.
- Each entry should represent a specific action / goal / gap to address in the scope of a session.
- Every entry should specify the remaining work to be done for that specific task, so that when the work is complete, the entry is addressed and iterative sessions will not continually work on the same entries, annotating progress.

**Entries in `Final-Productization-Checklist.md` can be responsible for task churn, specifically entries that contain the words:**
```
all
continue
every
each
remaining
across
etc
```
Poor wording in these entries can keep each checklist entry from being specific, actionable, and granular in scope, and encourage iterative churn, annotations of incremental progress, and multiple executions inside of a single entry.

## Permanent Checklist Entry - *NEVER CLOSE THIS*
> Use the Checklist Entry Template to create new tasks.
- [ ] For checklist entries that are worded in these nonspecific terms, above, *unless the checklist entry is a scoped audit*, perform the relevant audit so the entry can be expanded with EXACT SCOPE AND STEPS, AFFECTED FILES, AND `DONE WHEN` CRITERIA, each having their OWN entry. You may only proceed to other tasks when this condition is fulfilled. If all entries in this checklist currently adhere to this policy above the `Only Proceed To This Task If No Entries Above Exist` line, then proceed to address entries, as directed.

### Checklist Entry Template (Use for every new actionable item)
```
- Required fields for each entry:
  - `Scope:` exact problem boundary.
  - `Context:` why the task exists and what larger workflow or risk it supports.
  - `Target Files:` explicit relative paths to edit or audit.
  - `Dependencies:` prerequisite checklist items or `None`.
  - `DONE WHEN:` objective completion condition that can be verified.

Example format:
- [ ] **Task title**
  - Scope: <one bounded task>
  - Context: <why this task matters>
  - Target Files: `<path1>`, `<path2>`
  - Dependencies: <entry title or `None`>
  - DONE WHEN: <verifiable outcome>
```

> CHECK FOR VIOLATIONS OF THE ABOVE ENTRY BEFORE ADVANCING TO ANY OTHER CHECKLIST ENTRIES IN OTHER SECTIONS.

---

## Outstanding Tasks

### Phase 0 - Runtime foundation and executable project bootstrap

- [ ] **Choose and document the concrete runtime stack for web, API, worker, persistence, queueing, search, and auth**
  - Scope: Turn the proposed technology architecture into explicit implementation decisions or narrowly scoped approved defaults for the first build lane.
  - Context: The scaffold deliberately avoided speculative runtime dependencies. Before framework code appears, the repo needs an explicit stack decision record and matching checklist sequencing.
  - Target Files: `docs/03_architecture/technology_architecture.md`, `docs/06_delivery_operations/implementation_roadmap_and_phase_plan.md`, `README.md`, `pyproject.toml`
  - Dependencies: None
  - DONE WHEN: The selected stack for the first implementation wave is documented with rationale, rejected alternatives, and any needed pyproject or README updates, and no contradictory stack assumptions remain in the docs.

- [ ] **Implement typed runtime settings and environment-loading support**
  - Scope: Replace the settings placeholder with real typed configuration loading for API, worker, integrations, AI, analytics, notifications, and governance-sensitive defaults.
  - Context: Every app shell and service slice will need a shared settings surface before framework bootstrapping or provider wiring can happen safely.
  - Target Files: `src/ai_recruiting_platform/config/runtime_and_settings.py`, `src/ai_recruiting_platform/config/README.md`, `.env.example`, `docs/03_architecture/technology_architecture.md`
  - Dependencies: `Choose and document the concrete runtime stack for web, API, worker, persistence, queueing, search, and auth`
  - DONE WHEN: A typed settings implementation exists, `.env.example` documents required keys, package docs explain the boundary, and wrapper checks pass for the new code roots.

- [ ] **Create initial migration and persistence scaffolding for transactional platform data**
  - Scope: Establish the persistence root, migration tooling, and a first migration plan for tenancy, users, jobs, candidates, audit, and rights-state tables.
  - Context: The domain docs describe the data model, but implementation cannot begin in earnest until migrations and persistence conventions exist.
  - Target Files: `pyproject.toml`, `migrations/README.md`, `migrations/versions/`, `docs/03_architecture/data_model_and_domain_objects.md`, `docs/03_architecture/technology_architecture.md`
  - Dependencies: `Choose and document the concrete runtime stack for web, API, worker, persistence, queueing, search, and auth`
  - DONE WHEN: A migration tool and folder structure exist, the first schema plan is codified, and the docs explain how transactional tables will evolve.

- [ ] **Bootstrap the API, worker, and web app shells using the chosen runtime stack**
  - Scope: Turn the app-surface contract files into real framework entrypoints with minimal boot logic, health checks, and placeholder route or job registration.
  - Context: The repo already reserves `apps/api`, `apps/worker`, and `apps/web`. They need executable shells before domain slices can be wired end to end.
  - Target Files: `apps/api/api_surface_contract.py`, `apps/worker/worker_surface_contract.py`, `apps/web/web_surface_contract.py`, `apps/api/README.md`, `apps/worker/README.md`, `apps/web/README.md`
  - Dependencies: `Choose and document the concrete runtime stack for web, API, worker, persistence, queueing, search, and auth`, `Implement typed runtime settings and environment-loading support`
  - DONE WHEN: Each app root has a real bootstrap module or minimal runtime entrypoint, health-check behavior is documented, and the package READMEs describe how those shells connect to the internal package.

- [ ] **Add local development orchestration for the chosen app and data stack**
  - Scope: Create reproducible local startup instructions and any required dev-container or compose assets for API, worker, data stores, and supporting services.
  - Context: A stateless agent can scaffold code, but humans still need a reproducible way to run the system locally as real implementation begins.
  - Target Files: `README.md`, `CONTRIBUTING.md`, `docker-compose.yml`, `.dockerignore`, `docs/new_user_onboarding.md`
  - Dependencies: `Choose and document the concrete runtime stack for web, API, worker, persistence, queueing, search, and auth`, `Bootstrap the API, worker, and web app shells using the chosen runtime stack`
  - DONE WHEN: A documented local run path exists for the selected stack, new contributors can start the essential services, and docs no longer describe local execution as purely theoretical.

### Phase 1 - Identity, tenancy, and admin control plane

- [ ] **Implement tenant, workspace, user, team, role, and permission persistence models**
  - Scope: Create the first transactional models and persistence logic for tenancy and access control.
  - Context: Every route, workflow, audit record, and analytics event depends on tenant and role context; this is a prerequisite for safe multi-actor behavior.
  - Target Files: `src/ai_recruiting_platform/domain/tenancy_and_access.py`, `src/ai_recruiting_platform/schemas/auth_identity_schemas.py`, `migrations/versions/`, `docs/03_architecture/data_model_and_domain_objects.md`
  - Dependencies: `Create initial migration and persistence scaffolding for transactional platform data`
  - DONE WHEN: Transactional models and migrations exist for tenancy and access state, the domain contract is implemented or replaced with real code, and downstream routes can consume typed access objects.

- [ ] **Implement session, login, and identity-provider integration foundations**
  - Scope: Build the first auth and session workflows, including a local developer auth path and the interface for future SSO or provisioning support.
  - Context: The blueprint expects SSO and enterprise identity later, but the first workflow slices still need a real authenticated actor model.
  - Target Files: `src/ai_recruiting_platform/api/auth_and_identity_routes.py`, `apps/api/api_surface_contract.py`, `apps/web/web_surface_contract.py`, `docs/05_governance_trust/security_trust_and_candidate_rights.md`
  - Dependencies: `Implement tenant, workspace, user, team, role, and permission persistence models`, `Bootstrap the API, worker, and web app shells using the chosen runtime stack`
  - DONE WHEN: Users can establish a session through the chosen first-step auth path, route protection is enforceable, and future SSO support is documented without being falsely claimed as complete.

- [ ] **Implement RBAC enforcement and object-scope guards across route families**
  - Scope: Add reusable permission checks that enforce tenant, workspace, job, candidate, analytics, compliance, and admin boundaries.
  - Context: The platform cannot safely expose candidate data, outreach actions, or analytics without consistent object-level access enforcement.
  - Target Files: `src/ai_recruiting_platform/domain/tenancy_and_access.py`, `src/ai_recruiting_platform/api/auth_and_identity_routes.py`, `src/ai_recruiting_platform/api/jobs_routes.py`, `src/ai_recruiting_platform/api/candidates_routes.py`, `tests/`
  - Dependencies: `Implement tenant, workspace, user, team, role, and permission persistence models`, `Implement session, login, and identity-provider integration foundations`
  - DONE WHEN: Shared access guards exist, protected routes enforce them, and tests prove denial and allow behavior for representative role and object combinations.

- [ ] **Implement admin user and access-management surfaces with audit hooks**
  - Scope: Create admin APIs and first web surfaces for managing users, roles, teams, and access changes, with append-only audit logging for sensitive actions.
  - Context: Admins and recruiting operations need a real control plane before the platform can support multi-user workflow execution or enterprise review.
  - Target Files: `src/ai_recruiting_platform/api/auth_and_identity_routes.py`, `src/ai_recruiting_platform/audit/audit_log_contract.py`, `apps/web/web_surface_contract.py`, `docs/02_experience/screen_inventory.md`
  - Dependencies: `Implement RBAC enforcement and object-scope guards across route families`
  - DONE WHEN: Admin access-management routes and starter screens exist, sensitive changes create audit records, and the docs show how these controls fit into the broader platform.

### Phase 2 - Job intake and hiring-manager calibration

- [ ] **Implement job, criteria, and rubric data models plus core schemas**
  - Scope: Create the first persisted job, criteria, rubric, and approval-state models and their typed API schemas.
  - Context: Job and calibration state are the upstream inputs for search, scoring, comparison, and hiring-manager collaboration.
  - Target Files: `src/ai_recruiting_platform/domain/jobs_and_calibration.py`, `src/ai_recruiting_platform/schemas/jobs_schemas.py`, `migrations/versions/`
  - Dependencies: `Create initial migration and persistence scaffolding for transactional platform data`, `Implement RBAC enforcement and object-scope guards across route families`
  - DONE WHEN: Job and rubric entities exist with typed schemas and migrations, and downstream services can rely on stable approved-criteria state.

- [ ] **Implement job intake APIs and the first recruiter-facing job intake flow**
  - Scope: Build the route, service, and initial web flow for creating a job, extracting criteria inputs, editing them, and moving the job toward approval.
  - Context: The shortest useful platform lane begins with a real requisition and approved criteria, not with search in the abstract.
  - Target Files: `src/ai_recruiting_platform/services/job_intake_service.py`, `src/ai_recruiting_platform/api/jobs_routes.py`, `apps/web/web_surface_contract.py`, `docs/02_experience/ux_specification.md`
  - Dependencies: `Implement job, criteria, and rubric data models plus core schemas`, `Bootstrap the API, worker, and web app shells using the chosen runtime stack`
  - DONE WHEN: Recruiters can create and edit jobs through a real API and starter UI flow, and the job moves into a documented calibration or approval state.

- [ ] **Implement hiring-manager calibration and approval loops**
  - Scope: Create the limited-permission surfaces and APIs required for hiring-manager criteria approval, rubric review, and search-strategy feedback.
  - Context: The blueprint treats hiring-manager calibration as a workflow module, not an email side channel. It must exist before explainable shortlist work can claim alignment.
  - Target Files: `src/ai_recruiting_platform/domain/jobs_and_calibration.py`, `src/ai_recruiting_platform/api/jobs_routes.py`, `apps/web/web_surface_contract.py`, `docs/01_product/product_principles_personas_and_jobs.md`
  - Dependencies: `Implement job intake APIs and the first recruiter-facing job intake flow`
  - DONE WHEN: Hiring managers can review and approve criteria through limited-scope interfaces, approval state is persisted, and search or scoring work can reference that state.

- [ ] **Implement market-feasibility and search-strategy generation support**
  - Scope: Create the first services and views that estimate pool feasibility, surface skill adjacency, and propose search expansion from approved criteria.
  - Context: Fast shortlist creation depends on more than raw search. The platform must translate approved criteria into a workable sourcing strategy.
  - Target Files: `src/ai_recruiting_platform/domain/search_and_rediscovery.py`, `src/ai_recruiting_platform/services/search_service.py`, `apps/web/web_surface_contract.py`, `docs/01_product/end_to_end_workflow_map.md`
  - Dependencies: `Implement hiring-manager calibration and approval loops`
  - DONE WHEN: A recruiter can move from approved criteria to a generated search strategy or feasibility view, and the resulting state is available to the search layer.

### Phase 3 - Candidate profile, provenance, and data quality foundations

- [ ] **Implement normalized candidate, profile, and provenance persistence models**
  - Scope: Create candidate identity, profile, source, provenance, freshness, and relationship-history models plus their migrations.
  - Context: Search, explainability, outreach, privacy rights, and data-quality workflows all depend on a normalized candidate core with provenance.
  - Target Files: `src/ai_recruiting_platform/domain/candidate_profiles_and_talent_graph.py`, `src/ai_recruiting_platform/schemas/candidates_schemas.py`, `migrations/versions/`
  - Dependencies: `Create initial migration and persistence scaffolding for transactional platform data`, `Implement RBAC enforcement and object-scope guards across route families`
  - DONE WHEN: Candidate entities, provenance-bearing profile structures, and core schemas exist in storage and code, and the docs remain aligned with the implemented boundary.

- [ ] **Implement profile ingestion, resume parsing, and profile update orchestration**
  - Scope: Build the service layer that ingests ATS or uploaded candidate records, normalizes them, and preserves source provenance.
  - Context: The platform's evidence-backed posture depends on candidate data that can be traced to source and updated without destroying lineage.
  - Target Files: `src/ai_recruiting_platform/services/enrichment_service.py`, `src/ai_recruiting_platform/domain/candidate_profiles_and_talent_graph.py`, `src/ai_recruiting_platform/api/candidates_routes.py`, `docs/03_architecture/data_model_and_domain_objects.md`
  - Dependencies: `Implement normalized candidate, profile, and provenance persistence models`, `Create initial migration and persistence scaffolding for transactional platform data`
  - DONE WHEN: Candidate ingestion and normalization work through a real service flow, provenance metadata is persisted, and route consumers can retrieve unified profiles.

- [ ] **Implement freshness, confidence, duplicate-detection, and merge-review support**
  - Scope: Turn the data-quality placeholders into real scoring and merge-review behavior for stale records and duplicate candidates.
  - Context: Bad data kills recruiter trust, outreach quality, and ROI metrics. Data quality must be operationalized early rather than deferred.
  - Target Files: `src/ai_recruiting_platform/data_quality/freshness_and_confidence_scoring.py`, `src/ai_recruiting_platform/data_quality/deduplication_and_merge_review.py`, `src/ai_recruiting_platform/services/enrichment_service.py`, `apps/web/web_surface_contract.py`
  - Dependencies: `Implement profile ingestion, resume parsing, and profile update orchestration`
  - DONE WHEN: Candidate freshness and duplicate-review behaviors exist, recruiter or admin review surfaces can access them, and merge actions are bounded and auditable.

- [ ] **Implement recruiter-facing candidate profile and card surfaces**
  - Scope: Expose unified candidate cards and profile views that show evidence-bearing profile data, contact state placeholders, and provenance-aware field presentation.
  - Context: Recruiters should not need multiple tabs or systems to understand a candidate; this is core to the platform's UX promise.
  - Target Files: `src/ai_recruiting_platform/api/candidates_routes.py`, `apps/web/web_surface_contract.py`, `docs/02_experience/screen_inventory.md`, `docs/02_experience/ux_specification.md`
  - Dependencies: `Implement profile ingestion, resume parsing, and profile update orchestration`, `Implement freshness, confidence, duplicate-detection, and merge-review support`
  - DONE WHEN: Recruiters can retrieve and view candidate profiles and card-level summaries through real routes and starter UI surfaces, with provenance and freshness visible where available.

### Phase 4 - Search and rediscovery

- [ ] **Implement search indexing and query contracts**
  - Scope: Build the indexing pipeline and typed search request or result contracts needed for lexical and structured search.
  - Context: Search must be a first-class workflow, not a side effect of candidate storage. The indexing contract is its backbone.
  - Target Files: `src/ai_recruiting_platform/search/indexing_contract.py`, `src/ai_recruiting_platform/search/relevance_and_ranking_contract.py`, `src/ai_recruiting_platform/schemas/search_schemas.py`, `docs/03_architecture/system_architecture.md`
  - Dependencies: `Implement normalized candidate, profile, and provenance persistence models`, `Implement market-feasibility and search-strategy generation support`
  - DONE WHEN: Normalized candidate or job records can be published into the chosen search store, and typed search schemas and ranking contracts exist for route and service use.

- [ ] **Implement recruiter search APIs and starter search result surfaces**
  - Scope: Build the first search endpoints and recruiter-facing results view for query text, filters, and saved-search state.
  - Context: Fast shortlist creation requires a real search loop that recruiters can drive, not just a future search placeholder.
  - Target Files: `src/ai_recruiting_platform/services/search_service.py`, `src/ai_recruiting_platform/api/search_routes.py`, `apps/web/web_surface_contract.py`, `docs/02_experience/information_architecture_and_navigation.md`
  - Dependencies: `Implement search indexing and query contracts`, `Implement recruiter-facing candidate profile and card surfaces`
  - DONE WHEN: Recruiters can run a search through real endpoints, inspect results in a starter UI, and persist saved-search or filter state.

- [ ] **Implement semantic search support behind the chosen retrieval strategy**
  - Scope: Add the first semantic or embedding-backed retrieval path, including versioned query handling and fallback behavior when semantic retrieval is unavailable.
  - Context: The blueprint expects semantic search, but it should enter only after basic indexing and candidate normalization are stable.
  - Target Files: `src/ai_recruiting_platform/search/semantic_search_contract.py`, `src/ai_recruiting_platform/ai/model_gateway_contract.py`, `src/ai_recruiting_platform/services/search_service.py`, `docs/04_ai_automation/ai_ml_design.md`
  - Dependencies: `Choose and document the concrete runtime stack for web, API, worker, persistence, queueing, search, and auth`, `Implement search indexing and query contracts`
  - DONE WHEN: A semantic retrieval path exists behind typed contracts, its limitations are documented, and the search service can combine it with baseline search behavior.

- [ ] **Implement ATS rediscovery and re-engagement eligibility checks**
  - Scope: Build rediscovery logic for prior applicants or silver-medalist candidates, including cooldown, suppression, and ATS-status checks.
  - Context: Rediscovery is one of the fastest paths to measurable shortlist improvement, but only if it respects prior contact and candidate-rights state.
  - Target Files: `src/ai_recruiting_platform/services/rediscovery_service.py`, `src/ai_recruiting_platform/domain/search_and_rediscovery.py`, `src/ai_recruiting_platform/api/search_routes.py`, `docs/01_product/feature_inventory_and_prioritization.md`
  - Dependencies: `Implement recruiter search APIs and starter search result surfaces`, `Implement privacy, suppression, and unsubscribe persistence models`
  - DONE WHEN: Rediscovery recommendations are available through the search workflow, and eligibility rules prevent inappropriate resurfacing of candidates.

### Phase 5 - Scoring and explainability

- [ ] **Implement scoring persistence, rubric evaluation, and score-version tracking**
  - Scope: Create the first real score-run flow that evaluates candidates against approved criteria and persists score and version metadata.
  - Context: The platform's scoring promise depends on approved criteria, durable score records, and later reconstruction support.
  - Target Files: `src/ai_recruiting_platform/domain/scoring_and_explainability.py`, `src/ai_recruiting_platform/services/scoring_service.py`, `src/ai_recruiting_platform/schemas/scoring_schemas.py`, `migrations/versions/`
  - Dependencies: `Implement job, criteria, and rubric data models plus core schemas`, `Implement normalized candidate, profile, and provenance persistence models`
  - DONE WHEN: A score run can be created against approved criteria, version metadata is persisted, and later explanation or override workflows can reference the stored records.

- [ ] **Implement evidence extraction and explanation payload generation**
  - Scope: Build explanation logic that ties score components back to candidate or job evidence and exposes missing-evidence or confidence conditions.
  - Context: Explainable scoring is a core governance promise and should ship with score creation, not after it.
  - Target Files: `src/ai_recruiting_platform/services/explainability_service.py`, `src/ai_recruiting_platform/ai/evaluation_and_guardrails_contract.py`, `src/ai_recruiting_platform/schemas/scoring_schemas.py`, `docs/04_ai_automation/ai_ml_design.md`
  - Dependencies: `Implement scoring persistence, rubric evaluation, and score-version tracking`
  - DONE WHEN: Explanation payloads include evidence references or explicit missing-evidence states, and scoring outputs no longer behave like opaque rankings.

- [ ] **Implement scoring APIs, shortlist review, and recruiter override actions**
  - Scope: Expose score runs, explanation views, shortlist review, and human override capture through routes and starter UI surfaces.
  - Context: The platform's human-in-the-loop posture only becomes real once recruiters can review and override scoring through audited flows.
  - Target Files: `src/ai_recruiting_platform/api/scoring_routes.py`, `apps/web/web_surface_contract.py`, `docs/02_experience/ux_specification.md`, `docs/01_product/end_to_end_workflow_map.md`
  - Dependencies: `Implement evidence extraction and explanation payload generation`, `Implement recruiter search APIs and starter search result surfaces`
  - DONE WHEN: Recruiters can review scores, inspect explanations, create a shortlist, and record overrides through real APIs and starter interface flows.

- [ ] **Implement bias-support exports and score reconstruction groundwork**
  - Scope: Create the internal export structures and data contracts needed to reconstruct scores and support later bias or adverse-impact review.
  - Context: The blueprint calls for bias-support readiness and score reconstruction, but those claims need real exports and logs before they are credible.
  - Target Files: `src/ai_recruiting_platform/compliance/audit_export_and_bias_support.py`, `src/ai_recruiting_platform/audit/provenance_and_traceability_contract.py`, `src/ai_recruiting_platform/domain/audit_and_provenance.py`, `docs/05_governance_trust/compliance_privacy_and_ai_governance.md`
  - Dependencies: `Implement scoring persistence, rubric evaluation, and score-version tracking`, `Implement evidence extraction and explanation payload generation`
  - DONE WHEN: Internal export and reconstruction payloads exist for scores and evidence, and the docs clearly describe them as support tooling rather than completed compliance certification.

### Phase 6 - Privacy, suppression, unsubscribe, and audit foundations

- [ ] **Implement privacy, suppression, and unsubscribe persistence models**
  - Scope: Create the storage and domain state for privacy requests, suppression records, unsubscribe handling, and candidate consent state.
  - Context: These controls are prerequisites for safe outreach and for candidate-rights workflows. They cannot remain theoretical while messaging features move ahead.
  - Target Files: `src/ai_recruiting_platform/domain/compliance_privacy_and_suppression.py`, `src/ai_recruiting_platform/compliance/privacy_requests_and_candidate_rights.py`, `src/ai_recruiting_platform/compliance/suppression_and_unsubscribe_registry.py`, `migrations/versions/`
  - Dependencies: `Create initial migration and persistence scaffolding for transactional platform data`, `Implement normalized candidate, profile, and provenance persistence models`
  - DONE WHEN: Privacy, suppression, and unsubscribe state are modeled in storage and code, and downstream services can enforce them before contact or export actions.

- [ ] **Implement candidate-rights request workflows and verification handling**
  - Scope: Build the first APIs and service flows for access, correction, deletion, or opt-out requests, including identity-verification state and auditability.
  - Context: The platform should productize rights workflows rather than leave them to ad hoc support handling.
  - Target Files: `src/ai_recruiting_platform/services/privacy_and_suppression_service.py`, `src/ai_recruiting_platform/api/compliance_routes.py`, `apps/web/web_surface_contract.py`, `docs/05_governance_trust/compliance_privacy_and_ai_governance.md`
  - Dependencies: `Implement privacy, suppression, and unsubscribe persistence models`, `Implement RBAC enforcement and object-scope guards across route families`
  - DONE WHEN: A rights request can be submitted, verified, processed, and audited through real APIs and starter admin or candidate-facing surfaces.

- [ ] **Implement append-only audit logging for sensitive workflow actions**
  - Scope: Replace the audit placeholder with real append-only logging for identity, scoring, outreach, privacy, integration, and export actions.
  - Context: Auditability is a core proof-backed requirement that many later features depend on for trust and reconstruction.
  - Target Files: `src/ai_recruiting_platform/audit/audit_log_contract.py`, `src/ai_recruiting_platform/domain/audit_and_provenance.py`, `src/ai_recruiting_platform/services/privacy_and_suppression_service.py`, `migrations/versions/`
  - Dependencies: `Implement tenant, workspace, user, team, role, and permission persistence models`, `Implement privacy, suppression, and unsubscribe persistence models`
  - DONE WHEN: Sensitive workflow actions create durable audit records with actor, object, action, timestamp, and context fields, and downstream review surfaces can query them.

- [ ] **Implement suppression checks as blocking dependencies in contact and send workflows**
  - Scope: Integrate suppression, unsubscribe, and consent checks into the earliest contact-reveal and outreach paths so inappropriate contact is impossible by default.
  - Context: The blueprint explicitly requires suppression before outreach automation. This task enforces that sequence in code.
  - Target Files: `src/ai_recruiting_platform/services/outreach_service.py`, `src/ai_recruiting_platform/services/enrichment_service.py`, `src/ai_recruiting_platform/compliance/suppression_and_unsubscribe_registry.py`, `tests/`
  - Dependencies: `Implement privacy, suppression, and unsubscribe persistence models`, `Implement append-only audit logging for sensitive workflow actions`
  - DONE WHEN: Contact reveal or outreach preparation paths fail safely for blocked candidates, the failure reason is visible to authorized users, and tests prove the block behavior.

### Phase 7 - Outreach, replies, and deliverability

- [ ] **Implement contact reveal, verification, and enrichment-credit accounting**
  - Scope: Turn the enrichment and contact-reveal placeholders into a real flow that reveals contact data, verifies it, and records any billable or usage-sensitive actions.
  - Context: Outreach quality depends on contact accuracy, provenance, and transparent usage accounting.
  - Target Files: `src/ai_recruiting_platform/services/enrichment_service.py`, `src/ai_recruiting_platform/schemas/candidates_schemas.py`, `src/ai_recruiting_platform/billing/usage_and_credits.py`, `apps/web/web_surface_contract.py`
  - Dependencies: `Implement profile ingestion, resume parsing, and profile update orchestration`, `Implement suppression checks as blocking dependencies in contact and send workflows`
  - DONE WHEN: Authorized users can reveal and verify contact data through real routes or services, usage is recorded, and provenance or freshness remains visible.

- [ ] **Implement template, sequence, and campaign persistence models**
  - Scope: Create storage and schemas for templates, sequences, enrollment rules, campaign state, and stop conditions.
  - Context: The platform's outreach workflow needs typed, reviewable campaign state before drafts and sends can become real.
  - Target Files: `src/ai_recruiting_platform/domain/outreach_and_sequences.py`, `src/ai_recruiting_platform/schemas/outreach_schemas.py`, `migrations/versions/`
  - Dependencies: `Implement privacy, suppression, and unsubscribe persistence models`, `Create initial migration and persistence scaffolding for transactional platform data`
  - DONE WHEN: Templates, sequences, campaigns, and enrollment rules are modeled in storage and code and are available to routes and services.

- [ ] **Implement outreach drafting, approval, and send preparation workflows**
  - Scope: Build the service and route flows that draft messages, require approval, apply suppression checks, and prepare send jobs without directly sending unsanctioned outreach.
  - Context: The product promise is governed outreach, not unconstrained automation. Approval and blocking logic need to be first-class.
  - Target Files: `src/ai_recruiting_platform/services/outreach_service.py`, `src/ai_recruiting_platform/api/outreach_routes.py`, `apps/web/web_surface_contract.py`, `docs/04_ai_automation/ai_ml_design.md`
  - Dependencies: `Implement template, sequence, and campaign persistence models`, `Implement suppression checks as blocking dependencies in contact and send workflows`
  - DONE WHEN: Recruiters can draft and approve outreach through real APIs and starter UI surfaces, and send preparation respects blocking policy and audit requirements.

- [ ] **Implement email delivery, bounce, unsubscribe, and thread-sync connector support**
  - Scope: Create the first email connector path for sending, bounce handling, reply sync, and unsubscribe state propagation.
  - Context: Reply classification and campaign analytics depend on real delivery and thread state rather than draft-only workflow.
  - Target Files: `src/ai_recruiting_platform/integrations/email_and_calendar_connectors_contract.py`, `src/ai_recruiting_platform/services/integration_sync_service.py`, `src/ai_recruiting_platform/services/outreach_service.py`, `apps/worker/worker_surface_contract.py`
  - Dependencies: `Implement outreach drafting, approval, and send preparation workflows`, `Bootstrap the API, worker, and web app shells using the chosen runtime stack`
  - DONE WHEN: The chosen email provider is wired through a connector contract, send jobs can be executed, and bounce or unsubscribe events update workflow state.

- [ ] **Implement reply classification, triage, and stop-rule enforcement**
  - Scope: Build inbound reply ingestion, structured classification, recruiter queueing, and sequence stop behavior for interested, not-interested, unsubscribe, and bounce outcomes.
  - Context: Reply handling is a major time-saver and compliance dependency. It must be grounded in message state, not inferred by recruiters manually.
  - Target Files: `src/ai_recruiting_platform/services/reply_classification_service.py`, `src/ai_recruiting_platform/domain/replies_and_conversations.py`, `src/ai_recruiting_platform/api/outreach_routes.py`, `apps/web/web_surface_contract.py`
  - Dependencies: `Implement email delivery, bounce, unsubscribe, and thread-sync connector support`
  - DONE WHEN: Replies are ingested and classified through real services, stop rules update campaign state, and recruiter-facing triage surfaces can act on the results.

### Phase 8 - Scheduling and interviews

- [ ] **Implement scheduling persistence models and typed booking schemas**
  - Scope: Create interview, availability, booking, reminder, and scorecard models plus their schemas.
  - Context: Scheduling requires explicit persisted state before calendar connectors or candidate-facing booking links can behave predictably.
  - Target Files: `src/ai_recruiting_platform/domain/scheduling_and_interviews.py`, `src/ai_recruiting_platform/schemas/scheduling_schemas.py`, `migrations/versions/`
  - Dependencies: `Create initial migration and persistence scaffolding for transactional platform data`, `Implement privacy, suppression, and unsubscribe persistence models`
  - DONE WHEN: Scheduling and interview entities exist with typed schemas and storage support.

- [ ] **Implement calendar availability and interview-booking connectors for the first provider set**
  - Scope: Build the first read or write integration path for calendars, availability lookup, and event creation.
  - Context: Scheduling automation is impossible without a real calendar integration path and the corresponding worker or sync support.
  - Target Files: `src/ai_recruiting_platform/integrations/email_and_calendar_connectors_contract.py`, `src/ai_recruiting_platform/services/scheduling_service.py`, `apps/worker/worker_surface_contract.py`, `docs/06_delivery_operations/integration_design.md`
  - Dependencies: `Implement scheduling persistence models and typed booking schemas`, `Implement email delivery, bounce, unsubscribe, and thread-sync connector support`
  - DONE WHEN: Availability can be queried and interview events can be created or updated through the chosen calendar provider path.

- [ ] **Implement self-scheduling, recruiter booking, and reschedule workflows**
  - Scope: Expose scheduling routes and starter UI flows for slot proposal, booking, rescheduling, and cancellation.
  - Context: Coordinators and recruiters need a real scheduling loop to realize the platform's time-saving claims.
  - Target Files: `src/ai_recruiting_platform/services/scheduling_service.py`, `src/ai_recruiting_platform/api/scheduling_routes.py`, `apps/web/web_surface_contract.py`, `docs/02_experience/screen_inventory.md`
  - Dependencies: `Implement calendar availability and interview-booking connectors for the first provider set`, `Implement reply classification, triage, and stop-rule enforcement`
  - DONE WHEN: Authorized users can generate slots, book interviews, and reschedule or cancel through real routes and UI surfaces.

- [ ] **Implement interview planning, scorecards, and structured debrief workflows**
  - Scope: Turn the interview-planning placeholders into real plan, stage, rubric, and scorecard support with hiring-panel context.
  - Context: The recruiting workflow should continue past scheduling into structured evaluation and debrief, not fall back to unstructured notes.
  - Target Files: `src/ai_recruiting_platform/services/interview_planning_service.py`, `src/ai_recruiting_platform/api/scheduling_routes.py`, `apps/web/web_surface_contract.py`, `docs/01_product/end_to_end_workflow_map.md`
  - Dependencies: `Implement self-scheduling, recruiter booking, and reschedule workflows`, `Implement scoring persistence, rubric evaluation, and score-version tracking`
  - DONE WHEN: Interview plans, scorecards, and debrief-related state are represented in code and reachable through starter workflow surfaces.

### Phase 9 - Integrations and sync health

- [ ] **Implement the first ATS connector with field and stage mapping support**
  - Scope: Choose and build the first ATS integration path for jobs, candidates, stages, and notes, including explicit field and stage maps.
  - Context: The platform's integration-first posture depends on a real ATS slice rather than generic integration claims.
  - Target Files: `src/ai_recruiting_platform/integrations/ats_connectors_contract.py`, `src/ai_recruiting_platform/services/integration_sync_service.py`, `src/ai_recruiting_platform/api/integrations_routes.py`, `apps/web/web_surface_contract.py`
  - Dependencies: `Implement job intake APIs and the first recruiter-facing job intake flow`, `Implement normalized candidate, profile, and provenance persistence models`, `Bootstrap the API, worker, and web app shells using the chosen runtime stack`
  - DONE WHEN: One ATS provider can sync the minimum job and candidate objects through explicit mappings, and the route or admin layer can inspect connection and mapping state.

- [ ] **Implement sync-job execution, retries, dead-letter handling, and webhook ingestion**
  - Scope: Create worker flows and persistent sync-job state for scheduled syncs, webhook processing, retries, and failure capture.
  - Context: A connector without durable sync-job handling is just a brittle demo. Operational reliability needs real async orchestration.
  - Target Files: `src/ai_recruiting_platform/services/integration_sync_service.py`, `src/ai_recruiting_platform/domain/integrations_and_sync.py`, `apps/worker/worker_surface_contract.py`, `src/ai_recruiting_platform/integrations/webhooks_and_public_api_contract.py`
  - Dependencies: `Implement the first ATS connector with field and stage mapping support`, `Bootstrap the API, worker, and web app shells using the chosen runtime stack`
  - DONE WHEN: Sync jobs are persisted, webhook events can be ingested or replayed, retries and dead-letter behavior are explicit, and failures remain diagnosable.

- [ ] **Implement admin-facing integration health and mapping diagnostics**
  - Scope: Build APIs and starter web surfaces that let admins inspect connector health, mappings, recent failures, and replay or retry options.
  - Context: The blueprint requires admin-diagnosable integration failures rather than engineering-only visibility.
  - Target Files: `src/ai_recruiting_platform/api/integrations_routes.py`, `apps/web/web_surface_contract.py`, `docs/06_delivery_operations/observability_operations_and_support.md`, `docs/02_experience/screen_inventory.md`
  - Dependencies: `Implement sync-job execution, retries, dead-letter handling, and webhook ingestion`
  - DONE WHEN: Admins can see integration status, recent failures, and mapping state through real routes and starter UI surfaces.

- [ ] **Implement public API key and webhook subscription groundwork**
  - Scope: Create the internal data models and starter routes for API keys, webhook subscriptions, signed event envelopes, and replay-safe event delivery.
  - Context: Developer-facing extensibility is in scope, but it should follow the same auth, audit, and event discipline as first-party integrations.
  - Target Files: `src/ai_recruiting_platform/integrations/webhooks_and_public_api_contract.py`, `src/ai_recruiting_platform/api/integrations_routes.py`, `migrations/versions/`, `docs/03_architecture/api_design_and_webhooks.md`
  - Dependencies: `Implement sync-job execution, retries, dead-letter handling, and webhook ingestion`
  - DONE WHEN: API key and webhook subscription structures exist, signed event-envelope rules are documented in code, and the developer-facing surface can be expanded without inventing a new integration model.

### Phase 10 - Analytics, ROI, and operational reporting

- [ ] **Implement the event taxonomy and workflow-event emission across core slices**
  - Scope: Turn the analytics placeholders into a real event taxonomy and add event emission to job, search, scoring, outreach, scheduling, privacy, and integration workflows.
  - Context: The platform's ROI claims depend on event capture. Retroactive instrumentation is a fast route to broken metrics and false savings stories.
  - Target Files: `src/ai_recruiting_platform/analytics/event_taxonomy_contract.py`, `src/ai_recruiting_platform/services/analytics_service.py`, `src/ai_recruiting_platform/services/job_intake_service.py`, `src/ai_recruiting_platform/services/search_service.py`, `src/ai_recruiting_platform/services/outreach_service.py`, `src/ai_recruiting_platform/services/scheduling_service.py`
  - Dependencies: `Implement job intake APIs and the first recruiter-facing job intake flow`, `Implement recruiter search APIs and starter search result surfaces`, `Implement outreach drafting, approval, and send preparation workflows`, `Implement self-scheduling, recruiter booking, and reschedule workflows`
  - DONE WHEN: Named events and minimum event payloads exist across the core workflow slices, and analytics services can ingest them consistently.

- [ ] **Implement metric definitions and dashboard aggregation for shortlist, outreach, scheduling, and sync health**
  - Scope: Build the first aggregate metric layer and expose it through typed analytics routes.
  - Context: Core ROI and operational views should start with a narrow but defensible metric set rather than a giant dashboard that invents meaning.
  - Target Files: `src/ai_recruiting_platform/analytics/metrics_catalog_contract.py`, `src/ai_recruiting_platform/services/analytics_service.py`, `src/ai_recruiting_platform/api/analytics_routes.py`, `docs/06_delivery_operations/analytics_and_roi_measurement.md`
  - Dependencies: `Implement the event taxonomy and workflow-event emission across core slices`
  - DONE WHEN: The initial metric catalog is implemented, dashboard routes return real aggregates, and the docs define the caveats and formulas for the exposed metrics.

- [ ] **Implement recruiter, operations, and executive analytics starter surfaces**
  - Scope: Expose starter views for recruiter productivity, pipeline movement, source yield, contact quality, and integration or campaign health.
  - Context: Metrics are only valuable if the right audiences can use them through role-aware surfaces.
  - Target Files: `src/ai_recruiting_platform/api/analytics_routes.py`, `apps/web/web_surface_contract.py`, `docs/02_experience/information_architecture_and_navigation.md`, `docs/06_delivery_operations/analytics_and_roi_measurement.md`
  - Dependencies: `Implement metric definitions and dashboard aggregation for shortlist, outreach, scheduling, and sync health`
  - DONE WHEN: Role-appropriate analytics surfaces exist and are backed by real route responses rather than static placeholders.

- [ ] **Implement QBR-export and ROI-summary groundwork**
  - Scope: Create the first report-package structures and export flows for customer-ready or internal QBR summaries.
  - Context: The blueprint's measurable-ROI posture requires durable reporting artifacts rather than just interactive dashboards.
  - Target Files: `src/ai_recruiting_platform/analytics/reporting_and_qbr_contract.py`, `src/ai_recruiting_platform/services/analytics_service.py`, `src/ai_recruiting_platform/api/analytics_routes.py`, `docs/05_governance_trust/documentation_launch_and_public_artifacts.md`
  - Dependencies: `Implement metric definitions and dashboard aggregation for shortlist, outreach, scheduling, and sync health`
  - DONE WHEN: Typed report-package structures exist, exports can be generated from real metrics, and the documentation explains their intended internal or buyer-facing use.

### Phase 11 - Billing and entitlement enforcement

- [ ] **Implement plan, seat, and entitlement persistence plus admin billing APIs**
  - Scope: Create the first persisted billing state and routes for plan lookup, seats, and entitlements.
  - Context: Billing does not need pricing theater yet, but it does need real plan and entitlement mechanics before usage-sensitive workflows can enforce limits.
  - Target Files: `src/ai_recruiting_platform/domain/billing_and_entitlements.py`, `src/ai_recruiting_platform/billing/entitlements_and_plans.py`, `src/ai_recruiting_platform/api/billing_routes.py`, `migrations/versions/`
  - Dependencies: `Create initial migration and persistence scaffolding for transactional platform data`, `Implement metric definitions and dashboard aggregation for shortlist, outreach, scheduling, and sync health`
  - DONE WHEN: Plan and entitlement state are modeled in storage and exposed through admin-safe routes.

- [ ] **Implement usage metering for enrichment, AI, outreach, API, and integration-sensitive actions**
  - Scope: Attach real usage accounting to the workflow actions that should later affect plan limits or credits.
  - Context: Usage should be measured from service behavior, not guessed later for billing or analytics.
  - Target Files: `src/ai_recruiting_platform/billing/usage_and_credits.py`, `src/ai_recruiting_platform/services/enrichment_service.py`, `src/ai_recruiting_platform/services/outreach_service.py`, `src/ai_recruiting_platform/services/analytics_service.py`
  - Dependencies: `Implement plan, seat, and entitlement persistence plus admin billing APIs`, `Implement contact reveal, verification, and enrichment-credit accounting`
  - DONE WHEN: Billable or quota-sensitive actions emit usage records through real service flows, and billing routes can summarize the resulting state.

- [ ] **Implement entitlement enforcement in blocked-action paths and admin visibility**
  - Scope: Apply plan and entitlement checks to the workflows that should be limited by seats, credits, integrations, or API usage, and surface the reason to admins or authorized users.
  - Context: The repo should not allow hidden billing logic. Enforcement needs an explicit boundary and visible failure mode.
  - Target Files: `src/ai_recruiting_platform/services/billing_service.py`, `src/ai_recruiting_platform/services/enrichment_service.py`, `src/ai_recruiting_platform/services/outreach_service.py`, `src/ai_recruiting_platform/api/billing_routes.py`
  - Dependencies: `Implement usage metering for enrichment, AI, outreach, API, and integration-sensitive actions`
  - DONE WHEN: Blocked or warned actions respect entitlement checks, users receive clear explanations, and admin billing views reflect the same logic.

### Phase 12 - Governed agent runtime

- [ ] **Implement the agent registry, permission resolution, and kill-switch control plane**
  - Scope: Turn the agent registry placeholder into real persisted policy and runtime-control state for enabling, disabling, scoping, and killing agents.
  - Context: Agent behavior should not exist without an explicit control plane that says which agents are allowed to operate and under what boundaries.
  - Target Files: `src/ai_recruiting_platform/agents/agent_registry_and_permissions.py`, `src/ai_recruiting_platform/api/agents_routes.py`, `migrations/versions/`, `docs/04_ai_automation/agent_system_and_governance.md`
  - Dependencies: `Implement RBAC enforcement and object-scope guards across route families`, `Implement append-only audit logging for sensitive workflow actions`
  - DONE WHEN: Agent policy state exists in storage and code, agent routes can resolve permissions, and kill-switch behavior is represented explicitly.

- [ ] **Implement agent-run persistence, audit records, and approval queues**
  - Scope: Create durable records for agent runs, tool calls, approvals, errors, and blocked actions, plus starter routes or worker support for approval workflows.
  - Context: Governed agent claims are only credible if run state and approval actions are reconstructable.
  - Target Files: `src/ai_recruiting_platform/agents/agent_registry_and_permissions.py`, `src/ai_recruiting_platform/audit/audit_log_contract.py`, `apps/worker/worker_surface_contract.py`, `src/ai_recruiting_platform/api/agents_routes.py`
  - Dependencies: `Implement the agent registry, permission resolution, and kill-switch control plane`
  - DONE WHEN: Agent runs and approval events are persisted, auditable, and retrievable through internal APIs or worker logs.

- [ ] **Implement the first governed sourcing and research agent flows**
  - Scope: Choose one sourcing-oriented and one research-oriented agent slice and implement them in recommendation mode with explicit logs and review boundaries.
  - Context: The first agent work should deepen recruiter workflow rather than automate outreach or decisions prematurely.
  - Target Files: `src/ai_recruiting_platform/agents/sourcing_agent_contract.py`, `src/ai_recruiting_platform/agents/research_agent_contract.py`, `src/ai_recruiting_platform/services/search_service.py`, `src/ai_recruiting_platform/services/enrichment_service.py`, `apps/worker/worker_surface_contract.py`
  - Dependencies: `Implement agent-run persistence, audit records, and approval queues`, `Implement recruiter search APIs and starter search result surfaces`
  - DONE WHEN: At least one sourcing-style and one research-style agent flow can run in a governed recommendation mode, produce logs, and respect scope and policy boundaries.

- [ ] **Implement the first outreach or scheduling agent flow behind explicit approvals**
  - Scope: Choose one outbound or coordination agent slice and implement it only with approval gating, policy checks, and visible kill-switch behavior.
  - Context: This is where the repo proves that agent automation does not outrun governance or candidate-rights safeguards.
  - Target Files: `src/ai_recruiting_platform/agents/outreach_agent_contract.py`, `src/ai_recruiting_platform/agents/scheduling_agent_contract.py`, `src/ai_recruiting_platform/services/outreach_service.py`, `src/ai_recruiting_platform/services/scheduling_service.py`, `src/ai_recruiting_platform/api/agents_routes.py`
  - Dependencies: `Implement the first governed sourcing and research agent flows`, `Implement self-scheduling, recruiter booking, and reschedule workflows`, `Implement outreach drafting, approval, and send preparation workflows`
  - DONE WHEN: One outbound or coordination agent can operate only through approved actions, policy blocks are enforced, and users can inspect the resulting run history.

### Phase 13 - Frontend and user-surface depth

- [ ] **Implement the Today dashboard and recruiter operating queue**
  - Scope: Build the first cross-workflow dashboard that surfaces priority jobs, new matches, replies needing action, interviews, approvals, and operational blockers.
  - Context: The recruiter-first product promise depends on a real daily operating surface, not just separate feature screens.
  - Target Files: `apps/web/web_surface_contract.py`, `docs/02_experience/ux_specification.md`, `docs/02_experience/screen_inventory.md`, `src/ai_recruiting_platform/api/analytics_routes.py`
  - Dependencies: `Implement recruiter search APIs and starter search result surfaces`, `Implement reply classification, triage, and stop-rule enforcement`, `Implement self-scheduling, recruiter booking, and reschedule workflows`
  - DONE WHEN: A recruiter can open a Today-style view backed by real data and navigate to the next meaningful action without switching through disconnected screens.

- [ ] **Implement pipeline, shortlist, and comparison surfaces**
  - Scope: Create recruiter-facing views for shortlists, candidate comparison, pipeline movement, and stage review.
  - Context: Search and scoring only become usable when recruiters can act on the resulting candidates through a coherent review surface.
  - Target Files: `apps/web/web_surface_contract.py`, `src/ai_recruiting_platform/api/candidates_routes.py`, `src/ai_recruiting_platform/api/scoring_routes.py`, `docs/02_experience/screen_inventory.md`
  - Dependencies: `Implement scoring APIs, shortlist review, and recruiter override actions`
  - DONE WHEN: Recruiters can review shortlists, compare candidates, and move them through a starter pipeline flow with real persisted state.

- [ ] **Implement limited-permission hiring-manager review surfaces**
  - Scope: Build hiring-manager views for shortlist review, candidate comparison, structured feedback, and debrief participation under limited scope.
  - Context: The platform's calibration and collaboration story depends on giving hiring managers a focused portal rather than informal side channels.
  - Target Files: `apps/web/web_surface_contract.py`, `src/ai_recruiting_platform/api/jobs_routes.py`, `src/ai_recruiting_platform/api/scoring_routes.py`, `docs/02_experience/information_architecture_and_navigation.md`
  - Dependencies: `Implement hiring-manager calibration and approval loops`, `Implement pipeline, shortlist, and comparison surfaces`
  - DONE WHEN: Hiring managers can review candidates and leave structured feedback through real limited-permission surfaces without receiving broad recruiter access.

- [ ] **Implement admin and compliance workbench surfaces**
  - Scope: Build starter web surfaces for integration health, privacy requests, suppression management, audit review, and billing visibility.
  - Context: Admins and reviewers need operational views that match the platform's governance and integration-first posture.
  - Target Files: `apps/web/web_surface_contract.py`, `src/ai_recruiting_platform/api/integrations_routes.py`, `src/ai_recruiting_platform/api/compliance_routes.py`, `src/ai_recruiting_platform/api/billing_routes.py`
  - Dependencies: `Implement admin-facing integration health and mapping diagnostics`, `Implement candidate-rights request workflows and verification handling`, `Implement plan, seat, and entitlement persistence plus admin billing APIs`
  - DONE WHEN: Admin or reviewer surfaces exist for the key control-plane workflows, and they are backed by real routes rather than doc-only claims.

- [ ] **Implement extension-assisted profile capture and copy-ready message support**
  - Scope: Turn the extension contract into a minimal browser-assisted workflow for profile capture and copy-ready messaging without violating policy boundaries.
  - Context: The extension is optional for MVP, but the blueprint explicitly reserves this workflow. The first slice should stay manual-assist oriented rather than over-automated.
  - Target Files: `apps/extension/extension_surface_contract.py`, `src/ai_recruiting_platform/api/candidates_routes.py`, `src/ai_recruiting_platform/api/outreach_routes.py`, `docs/06_delivery_operations/integration_design.md`
  - Dependencies: `Implement recruiter-facing candidate profile and card surfaces`, `Implement outreach drafting, approval, and send preparation workflows`
  - DONE WHEN: A minimal extension-assisted flow exists for saving a candidate or copying an approved message draft, and the docs clearly state any remaining limits.

### Phase 14 - Testing, evals, and quality hardening

- [ ] **Create fixture strategy for tenants, jobs, candidates, suppression, outreach, and scheduling**
  - Scope: Build reusable test fixtures and factories that cover the first vertical workflow slices and governance-sensitive edge cases.
  - Context: The current tests only validate the template wrappers. Product implementation will need representative fixtures to stay maintainable.
  - Target Files: `tests/fixtures/`, `tests/conftest.py`, `docs/06_delivery_operations/testing_quality_assurance_and_eval_strategy.md`
  - Dependencies: `Implement the Today dashboard and recruiter operating queue`
  - DONE WHEN: Reusable fixtures exist for the main workflow entities and are referenced by route, service, and workflow tests.

- [ ] **Add integration tests for job-to-shortlist, outreach, reply, and scheduling flows**
  - Scope: Create route and service integration tests for the first real workflow slices, including permission and audit assertions.
  - Context: The platform's core value proposition depends on end-to-end workflow correctness, not isolated utility tests.
  - Target Files: `tests/integration/`, `src/ai_recruiting_platform/api/jobs_routes.py`, `src/ai_recruiting_platform/api/search_routes.py`, `src/ai_recruiting_platform/api/outreach_routes.py`, `src/ai_recruiting_platform/api/scheduling_routes.py`
  - Dependencies: `Create fixture strategy for tenants, jobs, candidates, suppression, outreach, and scheduling`
  - DONE WHEN: Representative workflow slices have integration coverage that asserts state changes, audit emission, and expected failures.

- [ ] **Add AI evaluation coverage for search, scoring, summarization, and unsupported-claim handling**
  - Scope: Create evaluation fixtures and checks for schema adherence, evidence coverage, and guardrail behavior across the first AI-enabled slices.
  - Context: Evidence-backed AI is part of the platform's thesis. It needs evaluation assets, not just model calls behind routes.
  - Target Files: `tests/ai_evals/`, `src/ai_recruiting_platform/ai/evaluation_and_guardrails_contract.py`, `docs/04_ai_automation/ai_ml_design.md`
  - Dependencies: `Implement evidence extraction and explanation payload generation`, `Implement the first governed sourcing and research agent flows`
  - DONE WHEN: AI-enabled workflow slices have evaluation assets that exercise schema, evidence, and unsupported-claim behavior, and failures are visible in the test or eval outputs.

- [ ] **Add accessibility, tenant-isolation, and security-focused workflow tests**
  - Scope: Create targeted tests for keyboard and semantic behavior in critical screens, tenant isolation in routes and queries, and sensitive action denial paths.
  - Context: Accessibility and security are launch-blocking expectations in the blueprint and should be encoded in tests before trust materials are drafted.
  - Target Files: `tests/e2e/`, `tests/integration/`, `docs/06_delivery_operations/testing_quality_assurance_and_eval_strategy.md`, `docs/05_governance_trust/security_trust_and_candidate_rights.md`
  - Dependencies: `Add integration tests for job-to-shortlist, outreach, reply, and scheduling flows`
  - DONE WHEN: Critical surfaces and route families have targeted accessibility, tenant-isolation, and security tests that fail loudly on regression.

### Phase 15 - Public launch, trust, and documentation readiness

- [ ] **Draft internal trust-center source docs for security overview, responsible AI, privacy, and known limitations**
  - Scope: Create the internal source documents that will later feed public trust-center or buyer-facing materials.
  - Context: The platform's proof-backed posture depends on documentation artifacts that lag implementation only slightly, not by quarters.
  - Target Files: `docs/public/security_overview.md`, `docs/public/responsible_ai_guide.md`, `docs/public/privacy_rights_guide.md`, `docs/public/known_limitations.md`
  - Dependencies: `Add accessibility, tenant-isolation, and security-focused workflow tests`, `Implement candidate-rights request workflows and verification handling`
  - DONE WHEN: Internal source docs exist for the major trust-center artifact families, each identifies dependencies and does not overstate readiness.

- [ ] **Draft integration setup guides and developer reference sources for the implemented provider set**
  - Scope: Create the internal docs that explain provider setup, scopes, mappings, and operational caveats for the connectors that are actually implemented.
  - Context: Integration claims should be backed by setup guides and not just route or connector code.
  - Target Files: `docs/integrations/`, `docs/06_delivery_operations/integration_design.md`, `docs/master_documentation_index.md`
  - Dependencies: `Implement the first ATS connector with field and stage mapping support`, `Implement email delivery, bounce, unsubscribe, and thread-sync connector support`
  - DONE WHEN: The implemented provider set has setup or caveat documentation, and the master index points to it.

- [ ] **Draft onboarding and implementation guides for pilot customers or internal rollout**
  - Scope: Create internal deployment, onboarding, and implementation guides that reflect the implemented first-use workflows and integration path.
  - Context: The repo needs a credible handoff path for humans, not just agents. Pilot readiness depends on setup and rollout docs.
  - Target Files: `docs/implementation_guide.md`, `docs/onboarding_checklist.md`, `docs/new_user_onboarding.md`, `docs/release_notes.md`
  - Dependencies: `Implement the Today dashboard and recruiter operating queue`, `Implement admin-facing integration health and mapping diagnostics`
  - DONE WHEN: An operator can follow the onboarding or implementation docs to understand setup, roles, integrations, and first-use workflow expectations.

- [ ] **Prepare buyer or procurement evidence bundles from implemented controls**
  - Scope: Assemble the internal source package for buyer security, privacy, audit, and responsible-AI review based only on implemented controls and reviewed docs.
  - Context: Procurement readiness should emerge from the repo's actual controls and docs, not from improvised sales narratives.
  - Target Files: `docs/buyer_security_package.md`, `docs/05_governance_trust/security_trust_and_candidate_rights.md`, `docs/05_governance_trust/documentation_launch_and_public_artifacts.md`, `docs/release_notes.md`
  - Dependencies: `Draft internal trust-center source docs for security overview, responsible AI, privacy, and known limitations`
  - DONE WHEN: A buyer-facing source bundle exists for the controls actually implemented, and no unsupported claims appear in the package.

### Phase 16 - Prompt recipes, skills, and context bootstrap assets

- [ ] **Implement the first project execution skills for wrapper-first remediation and checklist-driven work**
  - Scope: Create durable skill files that teach future agents how to operate in this repo's wrapper, checklist, and documentation model.
  - Context: The scaffold reserves `skills/` specifically so repetitive execution knowledge does not live only in root docs or human memory.
  - Target Files: `skills/project/README.md`, `skills/project/wrapper_first_execution.md`, `skills/project/checklist_driven_implementation.md`, `AGENTS.md`
  - Dependencies: `Draft onboarding and implementation guides for pilot customers or internal rollout`
  - DONE WHEN: At least two reusable project skill files exist, are cross-linked from the folder README or AGENTS, and accurately reflect the repo's operating model.

- [ ] **Implement the first agent-role skills for governed sourcing and compliance review**
  - Scope: Create reusable skill files for at least one recruiter-facing agent role and one governance-facing role.
  - Context: As agent work deepens, role-specific execution guidance should exist outside ad hoc prompts.
  - Target Files: `skills/agents/README.md`, `skills/agents/governed_sourcing.md`, `skills/agents/compliance_review.md`, `docs/04_ai_automation/agent_system_and_governance.md`
  - Dependencies: `Implement the first governed sourcing and research agent flows`, `Implement the first outreach or scheduling agent flow behind explicit approvals`
  - DONE WHEN: Role-specific skills exist for at least one sourcing-style agent and one compliance-style agent, and they reference the canonical governance docs.

- [ ] **Implement the first system prompts and bounded task-recipe assets**
  - Scope: Create prompt assets under `prompts/system/` and `prompts/task_recipes/` that correspond to implemented workflow slices and repo execution needs.
  - Context: The prompt registry placeholder implies prompt assets will later be first-class. The scaffold should start with a few durable, high-value examples.
  - Target Files: `prompts/system/README.md`, `prompts/system/recruiter_workbench_system_prompt.md`, `prompts/task_recipes/vertical_slice_delivery.md`, `prompts/task_recipes/documentation_parity_audit.md`
  - Dependencies: `Implement the first project execution skills for wrapper-first remediation and checklist-driven work`
  - DONE WHEN: Prompt assets exist for at least one system-level workflow and one bounded task recipe, and they are cross-linked from the prompt folder READMEs and relevant docs.

- [ ] **Implement generated context bundles for domain- and route-level bootstrap**
  - Scope: Extend the bootstrap workflow so agents can generate focused context packets for a domain slice, route family, or governance surface without replacing canonical docs.
  - Context: The repo already supports docstring aggregation. Focused context bundles will make later agent sessions more efficient without centralizing hidden continuity.
  - Target Files: `context/README.md`, `docs/agent_bootstrap/README.md`, `scripts/aggregate_project_docstrings.py`, `scripts/audit_docstrings.py`
  - Dependencies: `Implement the first system prompts and bounded task-recipe assets`
  - DONE WHEN: The bootstrap docs and scripts support at least one focused context-generation mode beyond the full docstring catalog, and the derivative-artifact policy stays explicit.

### Phase 17 - Optimization and operational maturity

- [ ] **Measure latency, queue behavior, and cost for the implemented workflow slices**
  - Scope: Add real timing and cost instrumentation for search, scoring, outreach, scheduling, integration sync, and agent runs where they now exist.
  - Context: Optimization should follow measured bottlenecks rather than intuition. The template already has an optimization checklist for test latency; product workflows need the same discipline.
  - Target Files: `docs/06_delivery_operations/observability_operations_and_support.md`, `src/ai_recruiting_platform/services/analytics_service.py`, `src/ai_recruiting_platform/services/search_service.py`, `src/ai_recruiting_platform/services/scoring_service.py`, `Final-Optimization-Checklist.md`
  - Dependencies: `Implement agent-run persistence, audit records, and approval queues`, `Implement metric definitions and dashboard aggregation for shortlist, outreach, scheduling, and sync health`
  - DONE WHEN: Measured latency and cost signals exist for the implemented workflow slices, and any new sustained latency exceptions are documented explicitly rather than hand-waved.

- [ ] **Implement support-ready status, incident, and diagnostic documentation for the running platform**
  - Scope: Create the first operational docs and status or incident source artifacts that support support, customer-success, or on-call workflows.
  - Context: Once real runtime surfaces and integrations exist, failures need support and communication material, not just engineering logs.
  - Target Files: `docs/status_page_source.md`, `docs/support_guide.md`, `docs/06_delivery_operations/observability_operations_and_support.md`, `docs/release_notes.md`
  - Dependencies: `Measure latency, queue behavior, and cost for the implemented workflow slices`
  - DONE WHEN: Status, support, and diagnostic source docs exist for the running slices, and they reflect the real operational surface rather than a fictional mature platform.

- [ ] **Audit roadmap, docs, and checklist for stale scaffold assumptions after the first full vertical lane ships**
  - Scope: Once the repo contains a genuine vertical slice, perform a deliberate audit to remove scaffold assumptions that are no longer true and add the next-wave tasks with better evidence.
  - Context: A successful scaffold should eventually become outdated. This task prevents the repo from preserving obsolete planning once implementation reaches a meaningful milestone.
  - Target Files: `README.md`, `AGENTS.md`, `docs/master_documentation_index.md`, `docs/06_delivery_operations/implementation_roadmap_and_phase_plan.md`, `Final-Productization-Checklist.md`
  - Dependencies: `Implement the Today dashboard and recruiter operating queue`, `Add integration tests for job-to-shortlist, outreach, reply, and scheduling flows`
  - DONE WHEN: The roadmap, docs, and checklist are refreshed against the first real shipping slice, and stale scaffold-only assumptions are removed or rewritten as current-state guidance.

---

## Only Proceed To This Task If No Entries Above Exist
> **INSTRUCTIONS:** AGENTS MAY NOT DELETE THE BELOW ENTRY OR THE DOCUMENTATION RUBRIC. ONLY THE USER MAY DELETE THIS SECTION. THIS TASK REMAINS OPEN UNTIL PROJECT COMPLETION.
- [ ] Populate the .md list for the `Create a checklist entry for every .md file in the repository HERE.` entry, below, in the `Documentation Inventory` section, for the `Documentation and Coding Audit` checklist process.

### Documentation and Coding Audit
> For All Files Listed Below, Perform a Coding Audit for any mentioned files and compare implementation to Documentation Copy as per the rubric below.

#### Execution quality examples for stateless agents
- ☑️ **Minimal unacceptable execution (do not do):** "Skim headings only, run a generic spell-check, update one sentence, and mark audit complete without verifying commands, links, ToC, implementation parity, or cross-document consistency."
- ✅ **Proper execution baseline (required):** "For each target file: verify ToC/anchor integrity, run command and path parity checks against implementation, confirm claims via code/tests, evaluate redundancy/cross-linking, expand mechanism explanations where shallow, and either apply fixes or create granular follow-up checklist entries with reproduction steps."
- ✅ **Coding Audit:** "Where a programmatic file is mentioned, investigate to ensure implementation and function. If you see areas for improvement or needed fixes, create appropriately actionable granular checklist tasks above the document audit, along with an embedded follow-up to correct documentation with your fix or improvement."

#### Documentation Parity Rubric (apply per file)
- ✅ **Coding Audit:** Where a programmatic file is mentioned, investigate to ensure implementation and function. If you see areas for improvement or needed fixes, create appropriately actionable granular checklist tasks above the document audit, along with an embedded follow-up to correct documentation with your fix or improvement.
- ✅ **Implementation truthfulness:** If a document is design-only or speculative, rewrite it to describe what is actually implemented now (or clearly move speculation into roadmap language).
- ✅ **Release-note handling:** If a document is iterative release-facing history (for example `docs/releases/CHANGELOG.md`) while the project is still unreleased, clear unreleased-facing content after verifying user-facing docs already capture relevant shipped behavior.
- ✅ **Operational usefulness:** Confirm the document enables a user or agent to execute or validate behavior, not just read a high-level overview.
- ✅ **Mechanism explanation depth:** Expand text to explain what mechanisms do, when to use them, inputs or outputs, and failure modes; not only that components exist.
- ✅ **Redundancy folding:** Merge or cross-link redundant documents and remove stale duplication.
- ✅ **README coverage by folder:** Verify every active top-level and major subfolder has an accurate `README.md`; add or update missing or inaccurate folder READMEs.
- ✅ **Navigation integrity:** Validate table of contents structure, local anchors, relative links, and cross-document references.
- ✅ **Command parity:** Verify documented commands match current CLI or script entry points and wrapper-first policy.
- ✅ **Evidence parity:** Validate claims against implementation paths or tests and remove stale or unverifiable assertions.
- ✅ **Agent continuity:** Ensure next-session contributors can act without hidden context (explicit prerequisites, paths, expected outputs, and remediation instructions).
- ✅ **UTF-8 and style policy:** Ensure text is UTF-8, avoids hidden characters or unintended escapes, and follows repository language or style constraints.

##### Documentation Inventory
> Create entries for the `Documentation Audit` here. Don't forget to follow the rubric above. If you discover issues, remediate them, or create new actionable granular tasks under `Outstanding Tasks` if you cannot remediate in-session.

- [ ] **Documentation Audit: `AGENTS.md`**
  - Scope: Verify wrapper-first rules, reading order, guardrails, and checklist policy remain accurate and internally consistent.
  - Context: AGENTS.md is the authoritative workflow contract for stateless coding agents.
  - Target Files: `AGENTS.md`, `README.md`, `docs/master_documentation_index.md`, `Final-Productization-Checklist.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `CODE_OF_CONDUCT.md`**
  - Scope: Verify the code-of-conduct document is reachable from contributor docs and that referenced conduct channels still make sense for the project.
  - Context: The code of conduct is a root governance artifact that should stay linked and current.
  - Target Files: `CODE_OF_CONDUCT.md`, `README.md`, `CONTRIBUTING.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `CONTRIBUTING.md`**
  - Scope: Verify local setup, reading order, wrapper usage, and project-specific expectations remain accurate.
  - Context: CONTRIBUTING.md provides the contributor path for humans working in the repo.
  - Target Files: `CONTRIBUTING.md`, `README.md`, `AGENTS.md`, `docs/new_user_onboarding.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `Final-Optimization-Checklist.md`**
  - Scope: Verify optimization guidance still matches current latency policy and does not accumulate stale exceptions.
  - Context: The optimization checklist is the sanctioned place for justified latency exceptions.
  - Target Files: `Final-Optimization-Checklist.md`, `AGENTS.md`, `tests/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `Final-Productization-Checklist.md`**
  - Scope: Verify phase ordering, task granularity, dependency references, and documentation inventory coverage remain accurate.
  - Context: The productization checklist carries open work and sets execution order for future sessions.
  - Target Files: `Final-Productization-Checklist.md`, `AGENTS.md`, `docs/06_delivery_operations/implementation_roadmap_and_phase_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `README.md`**
  - Scope: Verify project summary, scaffold-status wording, quickstart commands, repo map, and cross-links against the current implementation and docs.
  - Context: The root README is the first project entry point for humans and coding agents.
  - Target Files: `README.md`, `AGENTS.md`, `docs/master_documentation_index.md`, `pyproject.toml`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `apps/README.md`**
  - Scope: Verify asset lists, runtime-boundary language, and neighboring-doc references still match the current app-shell design.
  - Context: App-folder READMEs must explain what the runtime shell owns and what must stay in the internal package.
  - Target Files: `apps/README.md`, `docs/03_architecture/repository_asset_map.md`, `docs/03_architecture/code_localization_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `apps/api/README.md`**
  - Scope: Verify asset lists, runtime-boundary language, and neighboring-doc references still match the current app-shell design.
  - Context: App-folder READMEs must explain what the runtime shell owns and what must stay in the internal package.
  - Target Files: `apps/api/README.md`, `docs/03_architecture/repository_asset_map.md`, `docs/03_architecture/code_localization_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `apps/extension/README.md`**
  - Scope: Verify asset lists, runtime-boundary language, and neighboring-doc references still match the current app-shell design.
  - Context: App-folder READMEs must explain what the runtime shell owns and what must stay in the internal package.
  - Target Files: `apps/extension/README.md`, `docs/03_architecture/repository_asset_map.md`, `docs/03_architecture/code_localization_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `apps/web/README.md`**
  - Scope: Verify asset lists, runtime-boundary language, and neighboring-doc references still match the current app-shell design.
  - Context: App-folder READMEs must explain what the runtime shell owns and what must stay in the internal package.
  - Target Files: `apps/web/README.md`, `docs/03_architecture/repository_asset_map.md`, `docs/03_architecture/code_localization_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `apps/worker/README.md`**
  - Scope: Verify asset lists, runtime-boundary language, and neighboring-doc references still match the current app-shell design.
  - Context: App-folder READMEs must explain what the runtime shell owns and what must stay in the internal package.
  - Target Files: `apps/worker/README.md`, `docs/03_architecture/repository_asset_map.md`, `docs/03_architecture/code_localization_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `config/README.md`**
  - Scope: Verify manifest-governance language and wrapper command references remain accurate.
  - Context: Config docs explain wrapper-state and manifest policy that agents must not bypass.
  - Target Files: `config/README.md`, `AGENTS.md`, `scripts/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `config/precommit_store/README.md`**
  - Scope: Verify manifest-governance language and wrapper command references remain accurate.
  - Context: Config docs explain wrapper-state and manifest policy that agents must not bypass.
  - Target Files: `config/precommit_store/README.md`, `AGENTS.md`, `scripts/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `context/README.md`**
  - Scope: Verify generation policy, source-of-truth language, and command references remain accurate.
  - Context: Context-folder docs govern derivative artifacts that can otherwise become stale or misleading.
  - Target Files: `context/README.md`, `docs/agent_bootstrap/README.md`, `scripts/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/01_product/README.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/01_product/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/01_product/end_to_end_workflow_map.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/01_product/end_to_end_workflow_map.md`, `docs/01_product/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/01_product/feature_inventory_and_prioritization.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/01_product/feature_inventory_and_prioritization.md`, `docs/01_product/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/01_product/platform_overview_and_build_thesis.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/01_product/platform_overview_and_build_thesis.md`, `docs/01_product/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/01_product/product_principles_personas_and_jobs.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/01_product/product_principles_personas_and_jobs.md`, `docs/01_product/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/02_experience/README.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/02_experience/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/02_experience/information_architecture_and_navigation.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/02_experience/information_architecture_and_navigation.md`, `docs/02_experience/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/02_experience/screen_inventory.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/02_experience/screen_inventory.md`, `docs/02_experience/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/02_experience/ux_specification.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/02_experience/ux_specification.md`, `docs/02_experience/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/03_architecture/README.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/03_architecture/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/03_architecture/api_design_and_webhooks.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/03_architecture/api_design_and_webhooks.md`, `docs/03_architecture/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/03_architecture/code_localization_plan.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/03_architecture/code_localization_plan.md`, `docs/03_architecture/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/03_architecture/data_model_and_domain_objects.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/03_architecture/data_model_and_domain_objects.md`, `docs/03_architecture/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/03_architecture/repository_asset_map.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/03_architecture/repository_asset_map.md`, `docs/03_architecture/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/03_architecture/system_architecture.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/03_architecture/system_architecture.md`, `docs/03_architecture/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/03_architecture/technology_architecture.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/03_architecture/technology_architecture.md`, `docs/03_architecture/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/04_ai_automation/README.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/04_ai_automation/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/04_ai_automation/agent_system_and_governance.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/04_ai_automation/agent_system_and_governance.md`, `docs/04_ai_automation/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/04_ai_automation/ai_ml_design.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/04_ai_automation/ai_ml_design.md`, `docs/04_ai_automation/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md`, `docs/04_ai_automation/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/05_governance_trust/README.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/05_governance_trust/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/05_governance_trust/compliance_privacy_and_ai_governance.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/05_governance_trust/compliance_privacy_and_ai_governance.md`, `docs/05_governance_trust/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/05_governance_trust/documentation_launch_and_public_artifacts.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/05_governance_trust/documentation_launch_and_public_artifacts.md`, `docs/05_governance_trust/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/05_governance_trust/security_trust_and_candidate_rights.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/05_governance_trust/security_trust_and_candidate_rights.md`, `docs/05_governance_trust/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/06_delivery_operations/README.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/06_delivery_operations/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/06_delivery_operations/analytics_and_roi_measurement.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/06_delivery_operations/analytics_and_roi_measurement.md`, `docs/06_delivery_operations/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/06_delivery_operations/billing_packaging_and_usage.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/06_delivery_operations/billing_packaging_and_usage.md`, `docs/06_delivery_operations/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/06_delivery_operations/implementation_roadmap_and_phase_plan.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/06_delivery_operations/implementation_roadmap_and_phase_plan.md`, `docs/06_delivery_operations/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/06_delivery_operations/integration_design.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/06_delivery_operations/integration_design.md`, `docs/06_delivery_operations/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/06_delivery_operations/observability_operations_and_support.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/06_delivery_operations/observability_operations_and_support.md`, `docs/06_delivery_operations/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/06_delivery_operations/stateless_coding_agent_handoff.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/06_delivery_operations/stateless_coding_agent_handoff.md`, `docs/06_delivery_operations/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/06_delivery_operations/testing_quality_assurance_and_eval_strategy.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/06_delivery_operations/testing_quality_assurance_and_eval_strategy.md`, `docs/06_delivery_operations/README.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/README.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/agent_bootstrap/README.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/agent_bootstrap/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/master_documentation_index.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/new_user_onboarding.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/new_user_onboarding.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `docs/release_notes.md`**
  - Scope: Verify purpose, audience, usage guidance, cross-links, and repository-localization details remain accurate and specific.
  - Context: This file is part of the repository-native documentation spine and should stay aligned with implementation, neighboring docs, and package ownership.
  - Target Files: `docs/release_notes.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `prompts/README.md`**
  - Scope: Verify folder purpose, asset lists, and prompt-governance references remain accurate.
  - Context: Prompt-folder docs should explain how prompt assets relate to canonical docs and the future prompt registry.
  - Target Files: `prompts/README.md`, `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `prompts/system/README.md`**
  - Scope: Verify folder purpose, asset lists, and prompt-governance references remain accurate.
  - Context: Prompt-folder docs should explain how prompt assets relate to canonical docs and the future prompt registry.
  - Target Files: `prompts/system/README.md`, `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `prompts/task_recipes/README.md`**
  - Scope: Verify folder purpose, asset lists, and prompt-governance references remain accurate.
  - Context: Prompt-folder docs should explain how prompt assets relate to canonical docs and the future prompt registry.
  - Target Files: `prompts/task_recipes/README.md`, `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `scripts/README.md`**
  - Scope: Verify wrapper commands, supported utilities, and policy language remain consistent with the actual scripts.
  - Context: Script docs describe the canonical automation surface for this repo.
  - Target Files: `scripts/README.md`, `AGENTS.md`, `README.md`, `tests/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `scripts/test_profiles/README.md`**
  - Scope: Verify wrapper commands, supported utilities, and policy language remain consistent with the actual scripts.
  - Context: Script docs describe the canonical automation surface for this repo.
  - Target Files: `scripts/test_profiles/README.md`, `AGENTS.md`, `README.md`, `tests/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `skills/README.md`**
  - Scope: Verify folder purpose, asset lists, and cross-links to agent workflow docs remain accurate.
  - Context: Skill-folder docs should explain how reusable execution guidance fits the repo's operating model.
  - Target Files: `skills/README.md`, `AGENTS.md`, `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `skills/agents/README.md`**
  - Scope: Verify folder purpose, asset lists, and cross-links to agent workflow docs remain accurate.
  - Context: Skill-folder docs should explain how reusable execution guidance fits the repo's operating model.
  - Target Files: `skills/agents/README.md`, `AGENTS.md`, `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `skills/project/README.md`**
  - Scope: Verify folder purpose, asset lists, and cross-links to agent workflow docs remain accurate.
  - Context: Skill-folder docs should explain how reusable execution guidance fits the repo's operating model.
  - Target Files: `skills/project/README.md`, `AGENTS.md`, `docs/04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/README.md`**
  - Scope: Verify the file remains accurate, well-linked, and consistent with neighboring docs and implementation.
  - Context: This markdown file should stay accurate, linked, and usable for humans and agents.
  - Target Files: `src/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/agents/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/agents/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/ai/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/ai/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/analytics/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/analytics/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/api/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/api/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/audit/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/audit/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/billing/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/billing/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/compliance/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/compliance/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/config/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/config/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/data_quality/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/data_quality/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/domain/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/domain/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/integrations/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/integrations/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/notifications/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/notifications/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/schemas/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/schemas/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/search/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/search/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `src/ai_recruiting_platform/services/README.md`**
  - Scope: Verify the package README accurately lists contained assets, responsibility boundaries, and relevant neighboring docs.
  - Context: Package READMEs and markdown assets under `src/` help stateless agents keep implementation in the intended file boundaries.
  - Target Files: `src/ai_recruiting_platform/services/README.md`, `docs/03_architecture/code_localization_plan.md`, `docs/master_documentation_index.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

- [ ] **Documentation Audit: `tests/README.md`**
  - Scope: Verify the test inventory and execution-policy wording match the current test layout.
  - Context: Test docs explain what the repository currently validates and how wrapper-based execution works.
  - Target Files: `tests/README.md`, `AGENTS.md`, `scripts/README.md`
  - Dependencies: None
  - DONE WHEN: Links resolve, commands and file references match the current repo, implementation claims are honest, and neighboring docs or package READMEs no longer contradict this file.

---

## Coding-Agent-Surfaced Execution Friction / What Will Make Agents Able To Navigate Your Project More Easily
> **INSTRUCTIONS:** Surface Coding-Agent Execution Friction Entries Here for User Approval. User will migrate entries to higher in the checklist if your suggestions are approved.

**USER INSTRUCTIONS:** You will need to add an entry to `AGENTS.md` authorizing Coding-Agents to make entries in this section, should you choose to allow Agents to make their own checklist entry suggestions for common problems they encounter. This is **NOT ENABLED BY DEFAULT**.

Example addition to `AGENTS.md`:
```
Agents are expected to create actionable granular scoped checklist entries that follow the checklist template in `Final-Productization-Checklist.md` in the `Coding-Agent-Surfaced Execution Friction` section of the checklist when they encounter problems or friction specific to agent navigation, script invocation syntax, needed context without investigation, prompt recipes, task recipes, workflow diagrams, bootstrap context, or other assets that will make project use smoother for Coding Agents. The user agrees to review all checklist entries in that section and move them to actionable tasks, if approved.
```

- Create suggestion checklist entries here, if directed by `AGENTS.md`

---
