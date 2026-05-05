# Security, trust, and candidate rights

**Purpose:** Describe the security posture, trust-center expectations, and candidate-respect requirements that should shape implementation and public claims.

**Audience:** Security-minded contributors, admins, procurement reviewers, and agents touching auth, audit, communications, or candidate-facing flows.

**How to use this document:** Use this document before implementing identity, audit, exports, security settings, trust-center content, or candidate-facing rights surfaces.

**Relation to the blueprint:** Derived from blueprint section 20 plus supporting privacy and documentation sections.

**Relation to the repository tree:** Connects auth, access, audit, retention, trust-center planning, and candidate-facing rights flows to the package structure and future public docs.

**Neighboring documents:**
- [Compliance, privacy, and AI governance](../05_governance_trust/compliance_privacy_and_ai_governance.md)
- [Documentation, launch, and public artifacts](../05_governance_trust/documentation_launch_and_public_artifacts.md)
- [Observability, operations, and support](../06_delivery_operations/observability_operations_and_support.md)
- [Auth and identity routes](../../src/ai_recruiting_platform/api/README.md)

## Concise thesis

Security posture in this repo should mean concrete implementation and documentation work: identity controls, auditability, retention, incident readiness, and candidate-respect defaults. It does not mean vague certification theater.

## Design problem this document addresses

If trust is described only as a future legal page, the platform will fail both procurement scrutiny and candidate expectations. Security and candidate-rights design must shape the actual product surface.

## Security foundations

The scaffold assumes future support for SSO, MFA, SCIM, RBAC, least privilege, audit logs, encryption, secret handling, retention controls, and incident-support artifacts. Those capabilities need code roots, docs, and tests before they become sellable claims.

## Candidate rights and respect

Candidate-facing obligations include accessible scheduling and notice flows, unsubscribe and suppression behavior, privacy-request handling, and communication patterns that do not hide source, context, or rights. Candidate trust is a product behavior, not merely a policy page.

## Trust-center discipline

A trust center should eventually assemble reviewed artifacts such as privacy policy, terms, DPA, subprocessor list, security overview, responsible-AI guidance, and known limitations. Until those assets exist and are reviewed, the scaffold should present them as work products to be created, not as completed promises.

## Phased implementation notes

Implement internal security and rights workflows before polishing public trust surfaces. When public docs are added, keep them linked to their underlying control owners and update them in the same sessions as the code or operations changes they describe.
