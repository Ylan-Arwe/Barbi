"""
Purpose:
- Localize append-oriented audit records, provenance references, reconstruction views, and actor attribution.

Planned public functions, classes, endpoints, workers, or components:
- `AuditLogRecord`
- `ProvenanceReference`
- `ActorReference`
- `AuditExport`
- `record_sensitive_action()`

Major collaborators and dependencies:
- `audit/`
- `compliance/`
- `services/notification_service.py`
- `docs/05_governance_trust/compliance_privacy_and_ai_governance.md`

Inputs, outputs, and boundaries:
- Inputs: actor, action, object, workflow context, evidence references. Outputs: durable audit and provenance records. Boundary: storage engines and export transport stay outside the pure contract.

Implementation sequencing notes:
- Implement early because many later modules depend on auditability and provenance rather than merely benefiting from them.

Related docs and checklist references:
- `docs/03_architecture/data_model_and_domain_objects.md`
- `docs/03_architecture/code_localization_plan.md`
- `Final-Productization-Checklist.md`
"""
