"""
Purpose:
- Localize rubric-backed scoring concepts, score evidence, ranking runs, explainability payloads, and override state.

Planned public functions, classes, endpoints, workers, or components:
- `CandidateMatchScore`
- `ScoreEvidence`
- `RankingRun`
- `ExplainabilityPanel`
- `record_override()`

Major collaborators and dependencies:
- `ai/ranking_and_matching_contract.py`
- `services/scoring_service.py`
- `services/explainability_service.py`

Inputs, outputs, and boundaries:
- Inputs: approved criteria, candidate evidence, model and prompt versions, reviewer actions. Outputs: score and explanation state. Boundary: model-provider mechanics live in `ai/`; persistence and routes live elsewhere.

Implementation sequencing notes:
- Implement only after job criteria, candidate profiles, and provenance support are in place.

Related docs and checklist references:
- `docs/03_architecture/data_model_and_domain_objects.md`
- `docs/03_architecture/code_localization_plan.md`
- `Final-Productization-Checklist.md`
"""
