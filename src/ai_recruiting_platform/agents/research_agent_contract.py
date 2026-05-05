"""
Purpose:
- Describe the research agent's remit: summarize candidate and company context, gather evidence, and flag unsupported claims.

Planned public functions, classes, endpoints, workers, or components:
- `summarize_candidate()`
- `summarize_company_context()`
- `flag_unsupported_claims()`

Major collaborators and dependencies:
- `services/enrichment_service.py`
- `ai/model_gateway_contract.py`
- `audit/`

Inputs, outputs, and boundaries:
- Inputs: candidate profile, public context sources allowed by policy, provenance metadata. Outputs: summaries and evidence bundles. Boundary: no hidden fact invention or unauthorized scraping.

Implementation sequencing notes:
- Implement after profile and provenance systems exist.

Related docs and checklist references:
- `docs/04_ai_automation/agent_system_and_governance.md`
- `Final-Productization-Checklist.md`
"""
