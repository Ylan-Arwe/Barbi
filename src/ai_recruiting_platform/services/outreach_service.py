"""
Purpose:
- Coordinate template rendering, sequence enrollment, approvals, deliverability checks, send preparation, and campaign accounting.

Planned public functions, classes, endpoints, workers, or components:
- `draft_outreach()`
- `enroll_sequence()`
- `prepare_send_batch()`
- `record_campaign_outcome()`

Major collaborators and dependencies:
- `domain/outreach_and_sequences.py`
- `domain/compliance_privacy_and_suppression.py`
- `schemas/outreach_schemas.py`

Inputs, outputs, and boundaries:
- Inputs: candidate and job context, template state, sender settings, suppression state. Outputs: drafts, enrollment decisions, send jobs, campaign records.

Implementation sequencing notes:
- Implement only after suppression and consent logic exist.

Related docs and checklist references:
- `docs/03_architecture/code_localization_plan.md`
- `docs/06_delivery_operations/testing_quality_assurance_and_eval_strategy.md`
- `Final-Productization-Checklist.md`
"""
