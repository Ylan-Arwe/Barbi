"""
Purpose:
- Define usage meters, credit transactions, and blocked-action reasoning for billable actions.

Planned public functions, classes, endpoints, workers, or components:
- `UsageMeter`
- `CreditLedgerEntry`
- `record_usage()`

Major collaborators and dependencies:
- `services/billing_service.py`
- `analytics/`

Inputs, outputs, and boundaries:
- Inputs: billable workflow events. Outputs: usage records and credit deltas.

Implementation sequencing notes:
- Implement after billable actions are chosen.

Related docs and checklist references:
- `docs/06_delivery_operations/billing_packaging_and_usage.md`
- `Final-Productization-Checklist.md`
"""
