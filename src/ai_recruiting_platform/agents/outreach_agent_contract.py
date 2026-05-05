"""
Purpose:
- Describe the outreach agent's remit: draft messages and sequence suggestions that still require approval and suppression checks.

Planned public functions, classes, endpoints, workers, or components:
- `draft_message()`
- `suggest_sequence()`
- `prepare_follow_up()`

Major collaborators and dependencies:
- `services/outreach_service.py`
- `domain/compliance_privacy_and_suppression.py`
- `notifications/`

Inputs, outputs, and boundaries:
- Inputs: candidate, job, template, and policy context. Outputs: drafts and suggested campaigns. Boundary: no sending without explicit approval and policy checks.

Implementation sequencing notes:
- Implement after outreach approvals and suppression are real.

Related docs and checklist references:
- `docs/04_ai_automation/agent_system_and_governance.md`
- `Final-Productization-Checklist.md`
"""
