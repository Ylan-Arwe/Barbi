"""
Purpose:
- Define candidate-rights request handling structures for access, correction, deletion, and opt-out workflows.

Planned public functions, classes, endpoints, workers, or components:
- `RightsRequest`
- `VerificationState`
- `RightsDecision`
- `start_rights_workflow()`

Major collaborators and dependencies:
- `services/privacy_and_suppression_service.py`
- `api/compliance_routes.py`

Inputs, outputs, and boundaries:
- Inputs: request submissions, verification context. Outputs: rights workflow state.

Implementation sequencing notes:
- Implement before candidate-facing rights portals.

Related docs and checklist references:
- `docs/05_governance_trust/compliance_privacy_and_ai_governance.md`
- `Final-Productization-Checklist.md`
"""
