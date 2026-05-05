"""
Purpose:
- Define ATS-specific connector expectations for jobs, candidates, applications, stage mapping, notes, and interview sync.

Planned public functions, classes, endpoints, workers, or components:
- `ATSConnector`
- `ATSObjectMap`
- `StageMappingContract`
- `sync_candidate_record()`

Major collaborators and dependencies:
- `services/integration_sync_service.py`
- `api/integrations_routes.py`

Inputs, outputs, and boundaries:
- Inputs: ATS objects and mapping state. Outputs: normalized ATS synchronization behavior.

Implementation sequencing notes:
- Implement with the first ATS provider.

Related docs and checklist references:
- `docs/06_delivery_operations/integration_design.md`
- `Final-Productization-Checklist.md`
"""
