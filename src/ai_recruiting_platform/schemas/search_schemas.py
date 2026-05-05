"""
Purpose:
- Typed schemas for search queries, filters, saved searches, rediscovery actions, and search explanations.

Planned public functions, classes, endpoints, workers, or components:
- `SearchRequest`
- `SearchFilterSet`
- `SearchResult`
- `SavedSearchRecord`

Major collaborators and dependencies:
- `api/search_routes.py`
- `services/search_service.py`

Inputs, outputs, and boundaries:
- Inputs: search and rediscovery payloads. Outputs: typed search schemas.

Implementation sequencing notes:
- Implement alongside search routes.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `docs/03_architecture/data_model_and_domain_objects.md`
- `Final-Productization-Checklist.md`
"""
