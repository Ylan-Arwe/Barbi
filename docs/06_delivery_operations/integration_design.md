# Integration design

**Purpose:** Define how ATS, CRM, HCM, email, calendar, and public API integrations should be represented, governed, and debugged.

**Audience:** Integration authors, backend contributors, admins, and agents implementing connector contracts or sync health flows.

**How to use this document:** Use this document before adding a provider connector, sync worker, mapping screen, or webhook consumer.

**Relation to the blueprint:** Derived from blueprint section 18 and reinforced by the API and system architecture sections.

**Relation to the repository tree:** Owns the design expectations for `integrations/`, sync-related services and workers, admin surfaces, and external-provider documentation tasks.

**Neighboring documents:**
- [API design and webhooks](../03_architecture/api_design_and_webhooks.md)
- [System architecture](../03_architecture/system_architecture.md)
- [Observability, operations, and support](../06_delivery_operations/observability_operations_and_support.md)
- [Integrations package README](../../src/ai_recruiting_platform/integrations/README.md)

## Concise thesis

Integration quality is a product feature. Provider setup, mapping, retries, drift detection, and admin-debuggable failure states must be designed explicitly or adoption will collapse under data inconsistency.

## Design problem this document addresses

The platform only works if it can live inside ATS, calendar, email, and enterprise workflow realities. Generic “we integrate” language is useless without connector, mapping, and sync-health design.

## Connector model

Each provider should eventually have:
- a base connector contract;
- provider-specific auth and scope handling;
- object and field mappings;
- stage or lifecycle-state mappings where relevant;
- sync jobs and webhook consumers;
- normalized error and retry handling;
- admin-readable health and log surfaces.

## Provider priorities

The scaffold assumes early focus on at least one ATS plus email and calendar providers, with broader CRM/HCM coverage following later. Public API and webhook exposure should share the same event and auth discipline as first-party integrations rather than becoming a separate style of system.

## Integration debugging requirements

An admin should eventually be able to answer:
- whether the connection is healthy;
- which scopes are granted;
- when the last sync ran;
- what failed and why;
- whether a mapping or permissions problem caused the issue;
- what can be retried safely.

That expectation should shape both persistence models and user-facing admin surfaces.

## Phased implementation notes

Build integration abstractions and test doubles before provider sprawl. For each new provider, implement auth, mapping, sync, logs, retries, docs, and checklist coverage together so connector quality does not become invisible technical debt.
