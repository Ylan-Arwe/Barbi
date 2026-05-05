# AI and ML design

**Purpose:** Define what AI is allowed to do, what evidence it must produce, and how model-mediated behavior should be versioned, tested, and constrained.

**Audience:** AI contributors, backend authors, compliance reviewers, and agents implementing model-facing interfaces.

**How to use this document:** Use this document before building model prompts, retrieval flows, ranking logic, or any AI-mediated user surface.

**Relation to the blueprint:** Derived from blueprint section 15 and cross-referenced with the governance and testing sections.

**Relation to the repository tree:** Owns the behavioral requirements that should later be implemented in `src/ai_recruiting_platform/ai/`, service modules, analytics/eval modules, and compliance artifacts.

**Neighboring documents:**
- [Agent system and governance](../04_ai_automation/agent_system_and_governance.md)
- [Compliance, privacy, and AI governance](../05_governance_trust/compliance_privacy_and_ai_governance.md)
- [Testing, quality assurance, and eval strategy](../06_delivery_operations/testing_quality_assurance_and_eval_strategy.md)
- [Model gateway contract](../../src/ai_recruiting_platform/ai/README.md)

## Concise thesis

AI in this platform is a constrained subsystem for search translation, summarization, scoring support, explainability, drafting, classification, and planning. It is not permission to replace human judgment or invent unsupported candidate claims.

## Design problem this document addresses

Without an explicit AI design policy, future implementations will drift toward black-box convenience, overclaiming, and irreversible workflow automation that the blueprint explicitly rejects.

## Allowed capability families

The scaffold reserves space for natural-language search translation, semantic search support, candidate summarization, fit-gap analysis, score explanation, outreach drafting, reply classification, interview planning, compliance-risk detection, and agent planning. All of these capabilities are useful only if they are grounded in available evidence and represented through typed contracts rather than free-form text blobs.

## Evidence and versioning requirements

AI outputs should later be tied to:
- source evidence or retrieval context;
- approved criteria or rubrics where scoring is involved;
- model version;
- prompt or recipe version;
- evaluation or guardrail policy version where applicable;
- human review state for consequential outputs.

This is why the scaffold includes explicit placeholder modules for model gateways, prompt registries, evaluations, ranking contracts, audits, and agent run logs.

## Explicit prohibitions

The platform should not, by default:
- autonomously reject candidates;
- infer protected attributes for selection;
- present unsupported claims as fact;
- hide uncertainty when evidence is missing;
- bypass human review for materially consequential actions.

Those prohibitions should become testable guardrails, not just prose in documentation.

## Phased implementation notes

Implement AI features behind typed gateways and evaluation suites before exposing them as user-facing automation. Add model providers only when the relevant workflow, guardrail, and evaluation tasks are active in the checklist.
