"""
Purpose:
- Define the append-oriented audit log contract for user, system, and agent actions.

Planned public functions, classes, endpoints, workers, or components:
- `AuditRecord`
- `AuditActor`
- `append_audit_record()`

Major collaborators and dependencies:
- `domain/audit_and_provenance.py`
- `services/privacy_and_suppression_service.py`

Inputs, outputs, and boundaries:
- Inputs: sensitive actions, actor metadata, object references. Outputs: durable audit records.

Implementation sequencing notes:
- Implement early.

Related docs and checklist references:
- `docs/05_governance_trust/compliance_privacy_and_ai_governance.md`
- `docs/05_governance_trust/security_trust_and_candidate_rights.md`
- `Final-Productization-Checklist.md`
"""
