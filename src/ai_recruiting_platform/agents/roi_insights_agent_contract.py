"""
Purpose:
- Describe the ROI-insights agent's remit: summarize workflow results, QBR metrics, and improvement opportunities without inventing causality.

Planned public functions, classes, endpoints, workers, or components:
- `summarize_roi()`
- `prepare_qbr_notes()`
- `surface_improvement_opportunities()`

Major collaborators and dependencies:
- `analytics/`
- `services/analytics_service.py`
- `billing/`

Inputs, outputs, and boundaries:
- Inputs: measured workflow metrics, usage state, campaign and pipeline outcomes. Outputs: summaries and report drafts. Boundary: no fabricated savings or unsupported business claims.

Implementation sequencing notes:
- Implement after analytics and metric definitions are stable enough to support it.

Related docs and checklist references:
- `docs/04_ai_automation/agent_system_and_governance.md`
- `Final-Productization-Checklist.md`
"""
