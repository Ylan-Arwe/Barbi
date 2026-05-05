"""
Purpose:
- Define the suppression, unsubscribe, and do-not-contact registries that must block inappropriate outreach.

Planned public functions, classes, endpoints, workers, or components:
- `SuppressionRegistry`
- `UnsubscribeRecord`
- `SuppressionConflict`
- `check_contact_block()`

Major collaborators and dependencies:
- `domain/compliance_privacy_and_suppression.py`
- `services/outreach_service.py`

Inputs, outputs, and boundaries:
- Inputs: candidate or domain identifiers, unsubscribe events, admin actions. Outputs: suppression decisions and conflicts.

Implementation sequencing notes:
- Implement before outbound outreach automation.

Related docs and checklist references:
- `docs/05_governance_trust/compliance_privacy_and_ai_governance.md`
- `Final-Productization-Checklist.md`
"""
