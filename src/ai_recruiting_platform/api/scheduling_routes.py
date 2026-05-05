"""
Purpose:
- Reserve route-group ownership for scheduling links, slot proposals, booking, interview-plan retrieval, and scorecard submission.

Planned public functions, classes, endpoints, workers, or components:
- `register_scheduling_routes()`
- `get_slots()`
- `book_interview()`
- `submit_scorecard()`

Major collaborators and dependencies:
- `services/scheduling_service.py`
- `services/interview_planning_service.py`
- `schemas/scheduling_schemas.py`

Inputs, outputs, and boundaries:
- Inputs: scheduling and interview actions. Outputs: schedules, plans, and scorecards. Boundary: calendar provider calls remain outside the route layer.

Implementation sequencing notes:
- Implement after scheduling services and schemas exist.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `Final-Productization-Checklist.md`
"""
