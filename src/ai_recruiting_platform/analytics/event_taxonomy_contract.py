"""
Purpose:
- Define the canonical event names, categories, and minimum payload fields for workflow, governance, and operational analytics.

Planned public functions, classes, endpoints, workers, or components:
- `AnalyticsEventTaxonomy`
- `EventEnvelope`
- `validate_event_name()`

Major collaborators and dependencies:
- `services/analytics_service.py`
- `audit/`

Inputs, outputs, and boundaries:
- Inputs: workflow events and event metadata. Outputs: validated event envelopes and taxonomy references.

Implementation sequencing notes:
- Implement before large workflow slices ship.

Related docs and checklist references:
- `docs/06_delivery_operations/analytics_and_roi_measurement.md`
- `Final-Productization-Checklist.md`
"""
