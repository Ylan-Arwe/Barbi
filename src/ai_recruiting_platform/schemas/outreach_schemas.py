"""
Purpose:
- Typed schemas for templates, sequences, drafts, sends, replies, and unsubscribe-aware campaign state.

Planned public functions, classes, endpoints, workers, or components:
- `TemplateRequest`
- `SequenceResponse`
- `DraftMessageResponse`
- `ReplyClassificationResponse`

Major collaborators and dependencies:
- `api/outreach_routes.py`
- `services/outreach_service.py`
- `services/reply_classification_service.py`

Inputs, outputs, and boundaries:
- Inputs: outreach and reply payloads. Outputs: typed campaign and message schemas.

Implementation sequencing notes:
- Implement alongside outreach routes.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `docs/03_architecture/data_model_and_domain_objects.md`
- `Final-Productization-Checklist.md`
"""
