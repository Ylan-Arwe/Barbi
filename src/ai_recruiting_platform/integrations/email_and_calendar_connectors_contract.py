"""
Purpose:
- Define connector expectations for outbound email, inbound reply sync, signatures, availability reads, calendar writes, and reminder metadata.

Planned public functions, classes, endpoints, workers, or components:
- `EmailConnector`
- `CalendarConnector`
- `SendRequest`
- `AvailabilityWindow`

Major collaborators and dependencies:
- `services/outreach_service.py`
- `services/scheduling_service.py`

Inputs, outputs, and boundaries:
- Inputs: sender settings, message payloads, availability requests. Outputs: normalized email and calendar operations.

Implementation sequencing notes:
- Implement with the first email and calendar providers.

Related docs and checklist references:
- `docs/06_delivery_operations/integration_design.md`
- `Final-Productization-Checklist.md`
"""
