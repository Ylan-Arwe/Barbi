"""
Purpose:
- Describe the compliance agent's remit: detect risky criteria, assemble audit packages, and surface policy conflicts for human review.

Planned public functions, classes, endpoints, workers, or components:
- `scan_for_policy_risk()`
- `build_audit_package()`
- `flag_notice_gaps()`

Major collaborators and dependencies:
- `compliance/`
- `audit/`
- `services/privacy_and_suppression_service.py`

Inputs, outputs, and boundaries:
- Inputs: job criteria, outreach plans, AI configuration, rights workflow state. Outputs: findings and review packages. Boundary: no legal conclusions or autonomous enforcement beyond documented rules.

Implementation sequencing notes:
- Implement after compliance and audit foundations exist.

Related docs and checklist references:
- `docs/04_ai_automation/agent_system_and_governance.md`
- `Final-Productization-Checklist.md`
"""
