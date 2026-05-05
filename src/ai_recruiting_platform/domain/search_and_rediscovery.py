"""
Purpose:
- Localize search inputs, saved searches, rediscovery eligibility, cooldown rules, and query expansion concepts.

Planned public functions, classes, endpoints, workers, or components:
- `SearchQuery`
- `SavedSearch`
- `RediscoveryEligibility`
- `CooldownWindow`
- `expand_search_strategy()`

Major collaborators and dependencies:
- `search/`
- `services/search_service.py`
- `services/rediscovery_service.py`
- `api/search_routes.py`

Inputs, outputs, and boundaries:
- Inputs: approved criteria, recruiter filters, search history, ATS and candidate state. Outputs: search instructions and eligibility decisions. Boundary: actual indexing or ranking algorithms live in `search/` and `ai/`.

Implementation sequencing notes:
- Implement after job calibration and profile normalization basics exist.

Related docs and checklist references:
- `docs/03_architecture/data_model_and_domain_objects.md`
- `docs/03_architecture/code_localization_plan.md`
- `Final-Productization-Checklist.md`
"""
