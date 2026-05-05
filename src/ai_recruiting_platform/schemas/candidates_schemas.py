"""
Purpose:
- Typed request, response, and event schemas for candidate profiles, provenance, notes, tags, and exports.

Planned public functions, classes, endpoints, workers, or components:
- `CandidateResponse`
- `CandidateUpdateRequest`
- `ProvenanceField`
- `CandidateEvent`

Major collaborators and dependencies:
- `api/candidates_routes.py`
- `services/enrichment_service.py`

Inputs, outputs, and boundaries:
- Inputs: candidate profile and mutation payloads. Outputs: typed candidate schemas.

Implementation sequencing notes:
- Implement alongside profile routes.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `docs/03_architecture/data_model_and_domain_objects.md`
- `Final-Productization-Checklist.md`
"""
