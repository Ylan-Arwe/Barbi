"""
Purpose:
- Typed schemas for slot proposals, interview plans, bookings, reminders, and scorecards.

Planned public functions, classes, endpoints, workers, or components:
- `SlotProposalResponse`
- `InterviewPlanResponse`
- `BookingRequest`
- `ScorecardSubmission`

Major collaborators and dependencies:
- `api/scheduling_routes.py`
- `services/scheduling_service.py`
- `services/interview_planning_service.py`

Inputs, outputs, and boundaries:
- Inputs: scheduling and interview payloads. Outputs: typed scheduling schemas.

Implementation sequencing notes:
- Implement alongside scheduling routes.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `docs/03_architecture/data_model_and_domain_objects.md`
- `Final-Productization-Checklist.md`
"""
