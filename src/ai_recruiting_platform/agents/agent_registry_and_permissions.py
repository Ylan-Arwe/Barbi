"""
Purpose:
- Define how agents are registered, permission-scoped, enabled, disabled, and associated with tool allowlists and approval policies.

Planned public functions, classes, endpoints, workers, or components:
- `AgentRegistry`
- `AgentPermissionSet`
- `ToolAllowlist`
- `resolve_agent_policy()`

Major collaborators and dependencies:
- `docs/04_ai_automation/agent_system_and_governance.md`
- `audit/`
- `compliance/`

Inputs, outputs, and boundaries:
- Inputs: tenant policy, role permissions, agent definitions. Outputs: usable runtime policy for agent execution. Boundary: agent business logic belongs in agent contracts and services.

Implementation sequencing notes:
- Implement before any runnable agent is exposed.

Related docs and checklist references:
- `docs/04_ai_automation/agent_system_and_governance.md`
- `Final-Productization-Checklist.md`
"""
