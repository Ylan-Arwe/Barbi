"""
Purpose:
- Reserve the HTTP application entrypoint for the platform's API surface and document the deployable responsibilities that should stay at the app layer instead of leaking into domain modules.

Planned public functions, classes, endpoints, workers, or components:
- `create_application()`
- `register_route_groups()`
- `attach_middleware_stack()`
- `attach_observability_and_error_handlers()`
- `bind_background_dispatch_hooks()`

Major collaborators and dependencies:
- `src/ai_recruiting_platform/api/` route modules
- `src/ai_recruiting_platform/config/runtime_and_settings.py`
- `apps/worker/worker_surface_contract.py`
- `docs/03_architecture/system_architecture.md`

Inputs, outputs, and boundaries:
- Inputs: framework-specific runtime configuration, route registries, auth middleware, observability hooks. Outputs: initialized HTTP application. Boundary: no business rules or provider-specific orchestration should live here.

Implementation sequencing notes:
- Implement after settings, auth, route-group contracts, and core service wiring have been chosen. Keep framework bootstrapping isolated here so the internal package stays portable.

Related docs and checklist references:
- `docs/03_architecture/system_architecture.md`
- `docs/03_architecture/api_design_and_webhooks.md`
- `Final-Productization-Checklist.md`
"""
