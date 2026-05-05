"""
Purpose:
- Typed schemas for dashboards, metric definitions, report exports, and ROI summary views.

Planned public functions, classes, endpoints, workers, or components:
- `DashboardResponse`
- `MetricDefinitionResponse`
- `ReportExportRequest`
- `ROIInsightResponse`

Major collaborators and dependencies:
- `api/analytics_routes.py`
- `services/analytics_service.py`

Inputs, outputs, and boundaries:
- Inputs: reporting filters and export payloads. Outputs: typed analytics schemas.

Implementation sequencing notes:
- Implement alongside analytics routes.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `docs/03_architecture/data_model_and_domain_objects.md`
- `Final-Productization-Checklist.md`
"""
