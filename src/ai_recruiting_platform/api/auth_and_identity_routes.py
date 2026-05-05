"""
Purpose:
- Reserve route-group ownership for authentication, session, identity, SSO, MFA, and provisioning or deprovisioning flows.

Planned public functions, classes, endpoints, workers, or components:
- `register_auth_routes()`
- `get_session()`
- `start_sso()`
- `complete_sso()`
- `provision_user()`

Major collaborators and dependencies:
- `domain/tenancy_and_access.py`
- `config/runtime_and_settings.py`

Inputs, outputs, and boundaries:
- Inputs: auth requests, identity-provider callbacks, admin user management actions. Outputs: session state and identity mutations. Boundary: provider-specific SDK logic stays outside the route layer.

Implementation sequencing notes:
- Implement before role-gated app surfaces.

Related docs and checklist references:
- `docs/03_architecture/api_design_and_webhooks.md`
- `Final-Productization-Checklist.md`
"""
