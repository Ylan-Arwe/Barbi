"""
Purpose:
- Reserve route-group ownership for score runs, explanation retrieval, overrides, and score-version views.

Planned public functions, classes, endpoints, workers, or components:
- `register_scoring_routes()`
- `run_scoring()`
- `get_explanation()`
- `override_score()`

Major collaborators and dependencies:
- `services/scoring_service.py`
- `services/explainability_service.py`
- `schemas/scoring_schemas.py`

Inputs, outputs, and boundaries:
- Inputs: scoring requests and reviewer actions. Outputs: score and explanation payloads. Boundary: scoring logic and model calls stay outside routes.

Implementation sequencing notes:
- Implement after scoring service and schemas exist.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `Final-Productization-Checklist.md`
"""
