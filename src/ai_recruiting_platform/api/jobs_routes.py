"""
Purpose:
- Reserve route-group ownership for jobs, criteria, calibration, approvals, and job lifecycle mutations.

Planned public functions, classes, endpoints, workers, or components:
- `register_job_routes()`
- `list_jobs()`
- `create_job()`
- `approve_job_criteria()`

Major collaborators and dependencies:
- `services/job_intake_service.py`
- `schemas/jobs_schemas.py`

Inputs, outputs, and boundaries:
- Inputs: requisition requests, calibration actions. Outputs: job records and approval state. Boundary: orchestration belongs in services.

Implementation sequencing notes:
- Implement in the first core workflow slice.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `Final-Productization-Checklist.md`
"""
