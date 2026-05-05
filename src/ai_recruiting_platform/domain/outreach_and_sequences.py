"""
Purpose:
- Localize templates, sequence steps, enrollment rules, deliverability-related state, approvals, and campaign metrics concepts.

Planned public functions, classes, endpoints, workers, or components:
- `OutreachSequence`
- `SequenceStep`
- `TemplateVersion`
- `EnrollmentRule`
- `CampaignRecord`
- `can_enroll_candidate()`

Major collaborators and dependencies:
- `services/outreach_service.py`
- `schemas/outreach_schemas.py`
- `api/outreach_routes.py`
- `notifications/`

Inputs, outputs, and boundaries:
- Inputs: approved candidates, templates, sender policy, suppression state, deliverability signals. Outputs: sequence definitions and enrollment decisions. Boundary: message transport stays in integrations or notification layers.

Implementation sequencing notes:
- Implement after suppression, consent, and basic profile/contact state are modeled.

Related docs and checklist references:
- `docs/03_architecture/data_model_and_domain_objects.md`
- `docs/03_architecture/code_localization_plan.md`
- `Final-Productization-Checklist.md`
"""
