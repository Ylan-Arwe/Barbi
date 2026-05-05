# Agent system and governance

**Purpose:** Define the operating model for governed agents: scope, permissions, tool access, approvals, logging, analytics, and failure controls.

**Audience:** Maintainers building agent behaviors, compliance reviewers, and stateless agents implementing agent runtime surfaces.

**How to use this document:** Use this document when adding or expanding agent-facing modules, approval queues, run logs, or tool-allowlist logic.

**Relation to the blueprint:** Derived from blueprint section 16 and the stateless handoff expectations later in the blueprint.

**Relation to the repository tree:** Maps to `src/ai_recruiting_platform/agents/`, `apps/worker/`, `apps/api/`, `audit/`, and related analytics and compliance modules.

**Neighboring documents:**
- [AI and ML design](../04_ai_automation/ai_ml_design.md)
- [Prompt recipes, skills, and context injection plan](../04_ai_automation/prompt_recipes_skills_and_context_injection_plan.md)
- [Compliance, privacy, and AI governance](../05_governance_trust/compliance_privacy_and_ai_governance.md)
- [Stateless coding agent handoff](../06_delivery_operations/stateless_coding_agent_handoff.md)

## Concise thesis

Agent capability is only a differentiator if it is governable. Every agent must have explicit scope, permissions, tool access, human approval rules, logs, metrics, and kill switches before it deserves to be treated as a product capability.

## Design problem this document addresses

The word “agent” is a magnet for shallow implementations. This document exists to keep agent work anchored to policy, observability, and bounded tool use rather than vague autonomy claims.

## Reserved agent families

The scaffold reserves named homes for sourcing, research, outreach, scheduling, compliance, data quality, hiring-manager calibration, and ROI-insights agents. Each should remain permission-aware and workflow-specific rather than becoming a single all-purpose assistant with unrestricted reach.

## Governance controls

Every agent should later expose:
- scope selection and object boundaries;
- explicit tool allowlists;
- prohibited actions;
- cost and rate limits;
- approval requirements for destructive, outbound, or materially consequential actions;
- run history with input and output references;
- tenant, job, user, and global kill switches.

This governs both backend design and recruiter/admin UI design.

## Metrics that matter

Agent value should be measured through acceptance rate, override rate, error rate, time saved, and blocked-policy events. Vanity metrics such as “number of autonomous runs” are not substitutes for workflow improvement or safety.

## Phased implementation notes

Do not implement agents as a separate universe. Build them on top of the same domain, service, audit, analytics, and compliance contracts that the rest of the platform uses, and require explicit approval flows before they can act beyond recommendation mode.
