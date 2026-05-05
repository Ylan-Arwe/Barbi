"""
Purpose:
- Typed schemas for score runs, score results, explanation payloads, overrides, and versioned ranking views.

Planned public functions, classes, endpoints, workers, or components:
- `ScoreRunRequest`
- `ScoreResponse`
- `ExplanationResponse`
- `ScoreOverrideRequest`

Major collaborators and dependencies:
- `api/scoring_routes.py`
- `services/scoring_service.py`
- `services/explainability_service.py`

Inputs, outputs, and boundaries:
- Inputs: scoring requests and review actions. Outputs: typed scoring schemas.

Implementation sequencing notes:
- Implement alongside scoring routes.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `docs/03_architecture/data_model_and_domain_objects.md`
- `Final-Productization-Checklist.md`
"""
