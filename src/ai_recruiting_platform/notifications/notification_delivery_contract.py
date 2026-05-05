"""
Purpose:
- Define notification payloads, preference handling, digest rules, and delivery result tracking for recruiter, admin, and operational alerts.

Planned public functions, classes, endpoints, workers, or components:
- `NotificationMessage`
- `NotificationPreference`
- `DeliveryResult`
- `queue_delivery()`

Major collaborators and dependencies:
- `services/notification_service.py`
- `apps/worker/worker_surface_contract.py`

Inputs, outputs, and boundaries:
- Inputs: workflow events, user preferences, urgency metadata. Outputs: queued notification deliveries and delivery records.

Implementation sequencing notes:
- Implement alongside the first approval or reminder flows that need notification support.

Related docs and checklist references:
- `docs/06_delivery_operations/observability_operations_and_support.md`
- `Final-Productization-Checklist.md`
"""
