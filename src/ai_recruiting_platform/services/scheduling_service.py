"""
Purpose:
- Coordinate availability gathering, slot proposal, self-scheduling links, reminders, and calendar write operations.

Planned public functions, classes, endpoints, workers, or components:
- `generate_schedule_options()`
- `book_interview()`
- `reschedule_interview()`
- `cancel_interview()`

Major collaborators and dependencies:
- `domain/scheduling_and_interviews.py`
- `integrations/email_and_calendar_connectors_contract.py`
- `schemas/scheduling_schemas.py`

Inputs, outputs, and boundaries:
- Inputs: recruiter, panel, and candidate availability; time-zone rules; calendar state. Outputs: interview events and reminder tasks.

Implementation sequencing notes:
- Implement after reply handling and notifications foundations exist.

Related docs and checklist references:
- `docs/03_architecture/code_localization_plan.md`
- `docs/06_delivery_operations/testing_quality_assurance_and_eval_strategy.md`
- `Final-Productization-Checklist.md`
"""
