"""
Purpose:
- Define the catalog of KPI and ROI metrics, their definitions, caveats, and aggregation requirements.

Planned public functions, classes, endpoints, workers, or components:
- `MetricDefinition`
- `MetricFormula`
- `resolve_metric_definition()`

Major collaborators and dependencies:
- `services/analytics_service.py`
- `billing/`

Inputs, outputs, and boundaries:
- Inputs: event aggregates, usage records, workflow outcomes. Outputs: metric definitions and computation metadata.

Implementation sequencing notes:
- Implement alongside dashboard planning.

Related docs and checklist references:
- `docs/06_delivery_operations/analytics_and_roi_measurement.md`
- `Final-Productization-Checklist.md`
"""
