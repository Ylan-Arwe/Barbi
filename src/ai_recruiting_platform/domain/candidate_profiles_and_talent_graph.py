"""
Purpose:
- Localize the unified candidate profile, source provenance, timeline, skills, experience, education, certifications, and relationship state.

Planned public functions, classes, endpoints, workers, or components:
- `Candidate`
- `CandidateProfile`
- `CandidateSource`
- `CandidateExperience`
- `CandidateSkill`
- `merge_profile_updates()`

Major collaborators and dependencies:
- `services/enrichment_service.py`
- `schemas/candidates_schemas.py`
- `data_quality/`

Inputs, outputs, and boundaries:
- Inputs: ATS records, enrichment results, uploaded documents, recruiter notes, provenance metadata. Outputs: normalized profile state. Boundary: scoring and outreach state remain in their own domains.

Implementation sequencing notes:
- Implement before explainability, outreach, or high-confidence rediscovery work.

Related docs and checklist references:
- `docs/03_architecture/data_model_and_domain_objects.md`
- `docs/03_architecture/code_localization_plan.md`
- `Final-Productization-Checklist.md`
"""
