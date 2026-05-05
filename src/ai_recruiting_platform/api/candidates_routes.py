"""
Purpose:
- Reserve route-group ownership for candidate profile retrieval, mutation, notes, tags, and identity-safe exports.

Planned public functions, classes, endpoints, workers, or components:
- `register_candidate_routes()`
- `list_candidates()`
- `get_candidate_profile()`
- `update_candidate_metadata()`

Major collaborators and dependencies:
- `services/enrichment_service.py`
- `schemas/candidates_schemas.py`

Inputs, outputs, and boundaries:
- Inputs: recruiter and admin candidate actions. Outputs: candidate views and updates. Boundary: profile normalization stays in services and domain modules.

Implementation sequencing notes:
- Implement with profile and search slices.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `Final-Productization-Checklist.md`
"""
