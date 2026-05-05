"""
Purpose:
- Typed schemas for privacy requests, suppression records, notices, model cards, and audit exports.

Planned public functions, classes, endpoints, workers, or components:
- `PrivacyRequestSubmission`
- `SuppressionRecordResponse`
- `AuditExportResponse`
- `ModelCardResponse`

Major collaborators and dependencies:
- `api/compliance_routes.py`
- `services/privacy_and_suppression_service.py`

Inputs, outputs, and boundaries:
- Inputs: candidate-rights and compliance payloads. Outputs: typed governance schemas.

Implementation sequencing notes:
- Implement alongside compliance routes.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `docs/03_architecture/data_model_and_domain_objects.md`
- `Final-Productization-Checklist.md`
"""
