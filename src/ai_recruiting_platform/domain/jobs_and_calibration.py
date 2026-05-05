"""
Purpose:
- Localize job intake, criteria extraction, rubric approval, hiring-manager calibration, and job-version state.

Planned public functions, classes, endpoints, workers, or components:
- `Job`
- `JobCriteria`
- `JobRubric`
- `JobVersion`
- `CalibrationSession`
- `approve_criteria()`

Major collaborators and dependencies:
- `services/job_intake_service.py`
- `schemas/jobs_schemas.py`
- `api/jobs_routes.py`

Inputs, outputs, and boundaries:
- Inputs: requisition drafts, job descriptions, approval state, compensation and location signals. Outputs: approved job and calibration state. Boundary: search and scoring execution stay in their own modules.

Implementation sequencing notes:
- Implement before shortlist generation, scoring, or hiring-manager portal work.

Related docs and checklist references:
- `docs/03_architecture/data_model_and_domain_objects.md`
- `docs/03_architecture/code_localization_plan.md`
- `Final-Productization-Checklist.md`
"""
