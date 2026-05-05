# Billing, packaging, and usage

**Purpose:** Describe how plans, entitlements, usage meters, and credit-bound actions should eventually be represented without inventing unsupported pricing claims.

**Audience:** Product maintainers, billing contributors, admins, and agents implementing plan enforcement or usage reporting.

**How to use this document:** Use this document when implementing entitlements, usage accounting, or admin billing surfaces, and when deciding whether a workflow consumes billable credits.

**Relation to the blueprint:** Derived from blueprint section 22.

**Relation to the repository tree:** Maps to `domain/billing_and_entitlements.py`, `services/billing_service.py`, `billing/`, `api/billing_routes.py`, and related analytics surfaces.

**Neighboring documents:**
- [Analytics and ROI measurement](../06_delivery_operations/analytics_and_roi_measurement.md)
- [Integration design](../06_delivery_operations/integration_design.md)
- [Security, trust, and candidate rights](../05_governance_trust/security_trust_and_candidate_rights.md)
- [Billing package README](../../src/ai_recruiting_platform/billing/README.md)

## Concise thesis

Usage and plan enforcement should be productized as transparent entitlements, not as mysterious back-office behavior. Billing logic needs the same clarity as workflow logic because it changes what users can do and what buyers can approve.

## Design problem this document addresses

It is easy to invent pricing before the actual billable units are understood. This document keeps billing and packaging aligned with real product surfaces and measurable usage.

## Likely billable units

The blueprint implies future billing around seats, plan tiers, enrichment or contact credits, AI or agent usage, integrations, and API or webhook volume. The scaffold reserves the data model and service roots for these concepts without committing commercial terms yet.

## Entitlement design principles

Entitlements should be explicit, inspectable, and enforceable at the service boundary. Admin views should later show current plan, seats, consumption, overage warnings, and blocked actions with clear explanations. Hidden usage rules create support debt and buyer distrust.

## Pricing caution

This repository should not invent exact pricing, packaging promises, or enterprise controls beyond what the blueprint supports. Future commercial details belong in reviewed product or sales artifacts after the underlying usage model is implemented.

## Phased implementation notes

Build billing support after the relevant operational workflows exist, not before. Usage meters should be attached to real service actions and validated in tests before any external packaging claims are made.
