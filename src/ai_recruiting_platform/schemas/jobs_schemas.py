"""
Purpose:
- Typed request, response, and event schemas for job intake, criteria, calibration, and approval workflows.

Planned public functions, classes, endpoints, workers, or components:
- `JobCreateRequest`
- `JobResponse`
- `CriteriaApprovalRequest`
- `JobEvent`

Major collaborators and dependencies:
- `api/jobs_routes.py`
- `services/job_intake_service.py`

Inputs, outputs, and boundaries:
- Inputs: job and calibration payloads. Outputs: typed schemas shared across routes, services, and tests.

Implementation sequencing notes:
- Implement alongside job routes.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `docs/03_architecture/data_model_and_domain_objects.md`
- `Final-Productization-Checklist.md`
"""
