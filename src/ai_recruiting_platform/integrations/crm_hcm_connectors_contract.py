"""
Purpose:
- Define connector expectations for CRM and HCM systems that share candidate, job, or organizational state.

Planned public functions, classes, endpoints, workers, or components:
- `CRMHCMConnector`
- `PersonSyncRecord`
- `OrgMappingContract`

Major collaborators and dependencies:
- `services/integration_sync_service.py`
- `domain/integrations_and_sync.py`

Inputs, outputs, and boundaries:
- Inputs: CRM or HCM payloads, mapping state. Outputs: normalized synchronization behavior.

Implementation sequencing notes:
- Implement after ATS and communication basics.

Related docs and checklist references:
- `docs/06_delivery_operations/integration_design.md`
- `Final-Productization-Checklist.md`
"""
