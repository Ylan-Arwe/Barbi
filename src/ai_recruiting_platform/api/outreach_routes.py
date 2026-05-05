"""
Purpose:
- Reserve route-group ownership for templates, sequences, drafts, sends, reply triage, and unsubscribe-aware workflow actions.

Planned public functions, classes, endpoints, workers, or components:
- `register_outreach_routes()`
- `draft_message()`
- `create_sequence()`
- `classify_reply()`
- `unsubscribe_candidate()`

Major collaborators and dependencies:
- `services/outreach_service.py`
- `services/reply_classification_service.py`
- `schemas/outreach_schemas.py`

Inputs, outputs, and boundaries:
- Inputs: recruiter outreach actions and inbound message events. Outputs: drafts, sequence state, reply classifications. Boundary: transport and delivery internals stay outside routes.

Implementation sequencing notes:
- Implement after suppression and outreach service basics.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `Final-Productization-Checklist.md`
"""
