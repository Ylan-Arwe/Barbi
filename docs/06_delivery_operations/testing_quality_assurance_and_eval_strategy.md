# Testing, quality assurance, and eval strategy

**Purpose:** Define the test, validation, and evaluation layers required to make the platform trustworthy as implementation expands.

**Audience:** Backend, frontend, AI, QA, and security contributors plus stateless agents responsible for closing checklist items safely.

**How to use this document:** Use this document before adding tests, changing quality gates, or claiming a workflow is complete.

**Relation to the blueprint:** Derived from blueprint section 24 and aligned with the existing wrapper-first automation scaffold.

**Relation to the repository tree:** Owns the strategy that should later inform `tests/`, future app-specific test roots, AI eval fixtures, integration mocks, and checklist `DONE WHEN` criteria.

**Neighboring documents:**
- [AGENTS](../../AGENTS.md)
- [Analytics and ROI measurement](../06_delivery_operations/analytics_and_roi_measurement.md)
- [AI and ML design](../04_ai_automation/ai_ml_design.md)
- [Observability, operations, and support](../06_delivery_operations/observability_operations_and_support.md)

## Concise thesis

Quality in this repo is multi-layered: static analysis, route and service tests, integration mocks, end-to-end workflow validation, accessibility checks, security checks, and AI evaluation. A feature is not done because a happy path works once.

## Design problem this document addresses

The blueprint's product claims depend on testable workflow correctness, trustworthy AI behavior, privacy controls, and enterprise-facing evidence. This document turns those expectations into validation layers.

## Validation layers

The expected validation stack includes:
- unit tests for domain logic and helpers;
- integration tests for routes, persistence, and service orchestration;
- end-to-end workflow tests for job-to-shortlist, outreach, scheduling, and rights workflows;
- provider mocks and sandbox tests for integrations;
- AI evaluations for schema adherence, evidence coverage, and unsupported-claim handling;
- accessibility, security, tenant-isolation, and audit-log verification;
- load or latency checks when real systems justify them.

## Wrapper-first fit

The existing template wrappers remain the canonical quality and test surface. Future implementation should extend the repository under those wrappers rather than inventing a second operating model. New test roots, fixtures, or eval assets should therefore be added in ways that the wrappers can still orchestrate and summarize.

## Definition of done implications

Checklist items should use test language that matches this strategy. “Done” should usually mean the relevant route, service, UI, analytics, audit, and policy behaviors have tests or evaluation coverage appropriate to the risk of the feature, not merely that code compiles.

## Phased implementation notes

Expand validation in lockstep with implementation. When a new workflow slice is built, add its static checks, service tests, integration mocks, and any policy-sensitive evals in the same phase rather than deferring them to a generic hardening sprint.
