"""
Purpose:
- Define the shared connector interface for provider auth, capability discovery, object sync, error normalization, and health reporting.

Planned public functions, classes, endpoints, workers, or components:
- `BaseConnector`
- `ConnectorCapabilities`
- `SyncContext`
- `ConnectorResult`

Major collaborators and dependencies:
- `services/integration_sync_service.py`
- `domain/integrations_and_sync.py`

Inputs, outputs, and boundaries:
- Inputs: provider credentials, mapping state, sync context. Outputs: normalized connector operations and health signals.

Implementation sequencing notes:
- Implement before provider-specific connectors.

Related docs and checklist references:
- `docs/06_delivery_operations/integration_design.md`
- `Final-Productization-Checklist.md`
"""
