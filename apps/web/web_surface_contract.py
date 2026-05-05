"""
Purpose:
- Reserve the primary web application shell for recruiter, hiring-manager, admin, compliance, developer, and candidate-facing experiences.

Planned public functions, classes, endpoints, workers, or components:
- `define_route_groups()`
- `attach_layout_shells()`
- `register_role_gated_navigation()`
- `bind_data_loading_contracts()`
- `attach_error_and_empty_state_patterns()`

Major collaborators and dependencies:
- `docs/02_experience/ux_specification.md`
- `docs/02_experience/information_architecture_and_navigation.md`
- `src/ai_recruiting_platform/api/` route groups
- `src/ai_recruiting_platform/schemas/`

Inputs, outputs, and boundaries:
- Inputs: route-group definitions, auth/session state, API clients, role-aware navigation state. Outputs: the user-facing web shell. Boundary: business logic and persistence remain in the internal package and API layers.

Implementation sequencing notes:
- Implement after navigation groups, route contracts, and at least one vertical workflow slice are defined. Keep role-based visibility and accessibility concerns explicit at this layer.

Related docs and checklist references:
- `docs/02_experience/ux_specification.md`
- `docs/02_experience/information_architecture_and_navigation.md`
- `docs/02_experience/screen_inventory.md`
- `Final-Productization-Checklist.md`
"""
