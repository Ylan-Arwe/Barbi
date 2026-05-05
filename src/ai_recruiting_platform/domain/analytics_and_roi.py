"""
Purpose:
- Localize metric definitions, event categories, attribution logic, and ROI-reporting concepts.

Planned public functions, classes, endpoints, workers, or components:
- `AnalyticsEvent`
- `MetricDefinition`
- `ReportWindow`
- `ROIComputation`
- `record_workflow_event()`

Major collaborators and dependencies:
- `analytics/`
- `services/analytics_service.py`
- `api/analytics_routes.py`
- `docs/06_delivery_operations/analytics_and_roi_measurement.md`

Inputs, outputs, and boundaries:
- Inputs: workflow events, usage records, campaign outcomes, sync results, scheduling outcomes. Outputs: metric and report state. Boundary: warehouse or BI implementation details stay outside the pure domain model.

Implementation sequencing notes:
- Implement early enough that core workflow slices emit analyzable events from the first real lane.

Related docs and checklist references:
- `docs/03_architecture/data_model_and_domain_objects.md`
- `docs/03_architecture/code_localization_plan.md`
- `Final-Productization-Checklist.md`
"""
