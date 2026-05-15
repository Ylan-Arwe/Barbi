"""Web application shell contract for Next.js-facing route and health metadata."""

from __future__ import annotations

from dataclasses import dataclass
from os import environ


@dataclass(frozen=True)
class RouteGroup:
    name: str
    base_path: str
    allowed_roles: tuple[str, ...]


@dataclass(frozen=True)
class WebShellContract:
    app_name: str
    environment: str
    route_groups: tuple[RouteGroup, ...]


def define_route_groups() -> tuple[RouteGroup, ...]:
    return (
        RouteGroup(name="recruiter", base_path="/recruiter", allowed_roles=("recruiter", "admin")),
        RouteGroup(name="hiring_manager", base_path="/hiring-manager", allowed_roles=("hiring_manager", "admin")),
        RouteGroup(name="admin", base_path="/admin", allowed_roles=("admin",)),
        RouteGroup(name="compliance", base_path="/compliance", allowed_roles=("compliance", "admin")),
    )


def attach_layout_shells(contract: WebShellContract) -> WebShellContract:
    return contract


def register_role_gated_navigation(contract: WebShellContract) -> WebShellContract:
    return contract


def bind_data_loading_contracts(contract: WebShellContract) -> WebShellContract:
    return contract


def attach_error_and_empty_state_patterns(contract: WebShellContract) -> WebShellContract:
    return contract


def create_web_shell_contract() -> WebShellContract:
    contract = WebShellContract(
        app_name=f"{environ.get('SERVICE_NAME', 'ai-recruiting-platform')} Web",
        environment=environ.get("ENVIRONMENT", "local"),
        route_groups=define_route_groups(),
    )
    contract = attach_layout_shells(contract)
    contract = register_role_gated_navigation(contract)
    contract = bind_data_loading_contracts(contract)
    return attach_error_and_empty_state_patterns(contract)
