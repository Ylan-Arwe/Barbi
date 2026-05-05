# Compliance, privacy, and AI governance

**Purpose:** Turn the blueprint's governance expectations into repository-level controls, documentation boundaries, and implementation obligations without pretending legal compliance has already been achieved.

**Audience:** Compliance-minded contributors, backend authors, security reviewers, and any agent touching candidate data, outreach, scoring, or rights workflows.

**How to use this document:** Use this document before implementing privacy-sensitive features, scoring logic, outreach automation, model summaries, or public trust claims.

**Relation to the blueprint:** Derived from blueprint section 19 and cross-referenced with AI design, security design, and public-artifact planning.

**Relation to the repository tree:** Owns the governance expectations that should be reflected in domain modules, compliance packages, audit logs, candidate-facing surfaces, and trust documentation tasks.

**Neighboring documents:**
- [AI and ML design](../04_ai_automation/ai_ml_design.md)
- [Security, trust, and candidate rights](../05_governance_trust/security_trust_and_candidate_rights.md)
- [Documentation, launch, and public artifacts](../05_governance_trust/documentation_launch_and_public_artifacts.md)
- [Privacy and suppression service](../../src/ai_recruiting_platform/compliance/README.md)

## Concise thesis

This repository may describe compliance readiness work, but it must not claim completed legal or regulatory compliance unless the corresponding controls, evidence, and reviewed artifacts actually exist. The platform's job is to make governance operational, not magical.

## Design problem this document addresses

Employment workflows, outreach automation, and AI ranking sit in legally and reputationally sensitive territory. The blueprint makes governance a product requirement; this doc translates that into build constraints.

## Privacy and candidate-rights baseline

The scaffold assumes future support for access, correction, deletion, and opt-out workflows, plus suppression and unsubscribe logic that blocks inappropriate outreach. Candidate rights and contact-state logic should be modeled explicitly and not hidden inside outreach tables or ATS sync metadata.

## AI-governance baseline

Scoring, ranking, summaries, and agent planning all require versioning, evidence, human oversight, and exportable logs. Model cards, evaluation runs, bias-support exports, and score reconstruction are planned artifacts, not optional extras. Until those controls exist, the repository should describe them as readiness work rather than finished capability.

## Documentation and claim discipline

Public and buyer-facing claims should trail implemented controls. Security, privacy, AI-governance, and candidate-rights statements should only move from internal planning docs to public artifacts when the checklist, docs, and code can jointly support them.

## Phased implementation notes

Treat governance requirements as gating conditions in checklist order. Build privacy, suppression, evidence, and audit foundations before expanding automation and before publishing broad trust claims.
