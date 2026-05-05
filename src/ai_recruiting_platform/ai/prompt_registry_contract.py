"""
Purpose:
- Define how prompt recipes, system prompts, versions, approvals, and deprecation state should be stored and resolved.

Planned public functions, classes, endpoints, workers, or components:
- `PromptRegistry`
- `PromptVersion`
- `PromptSelectionPolicy`
- `resolve_prompt()`

Major collaborators and dependencies:
- `prompts/`
- `services/scoring_service.py`
- `agents/`

Inputs, outputs, and boundaries:
- Inputs: prompt identifiers, workflow context, version policies. Outputs: resolved prompt assets and metadata. Boundary: prompt content files live in `prompts/`, not here.

Implementation sequencing notes:
- Implement before workflows depend on mutable prompt behavior.

Related docs and checklist references:
- `docs/04_ai_automation/ai_ml_design.md`
- `Final-Productization-Checklist.md`
"""
