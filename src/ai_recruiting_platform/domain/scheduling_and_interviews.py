"""
Purpose:
- Localize availability, interview plans, scorecards, scheduling state, rescheduling, and accommodation-aware coordination.

Planned public functions, classes, endpoints, workers, or components:
- `SchedulingRequest`
- `InterviewPlan`
- `InterviewSlot`
- `InterviewScorecard`
- `ScheduleConflict`
- `propose_slots()`

Major collaborators and dependencies:
- `services/scheduling_service.py`
- `services/interview_planning_service.py`
- `schemas/scheduling_schemas.py`
- `api/scheduling_routes.py`

Inputs, outputs, and boundaries:
- Inputs: candidate availability, panel availability, interview templates, calendar state, accommodation requests. Outputs: schedule and interview-plan state. Boundary: calendar provider calls stay in integrations or services.

Implementation sequencing notes:
- Implement after identity, notifications, and basic outreach reply handling are stable enough to trigger scheduling.

Related docs and checklist references:
- `docs/03_architecture/data_model_and_domain_objects.md`
- `docs/03_architecture/code_localization_plan.md`
- `Final-Productization-Checklist.md`
"""
