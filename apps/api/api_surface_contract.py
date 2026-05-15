"""API shell bootstrap contract using framework-neutral runtime descriptors."""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from os import environ


@dataclass(frozen=True)
class HealthPayload:
    """Typed health-check payload for API status endpoints."""

    service: str
    environment: str
    status: str


@dataclass(frozen=True)
class RouteDescriptor:
    """Declarative route registration metadata."""

    method: str
    path: str
    handler_name: str


def _empty_route_descriptors() -> list[RouteDescriptor]:
    return []


def _empty_startup_hooks() -> list[str]:
    return []


@dataclass
class ApiApplication:
    """Framework-neutral API shell runtime payload."""

    name: str
    docs_enabled: bool
    routes: list[RouteDescriptor] = field(default_factory=_empty_route_descriptors)
    startup_hooks: list[str] = field(default_factory=_empty_startup_hooks)


def _service_name() -> str:
    return environ.get("SERVICE_NAME", "ai-recruiting-platform")


def _environment() -> str:
    return environ.get("ENVIRONMENT", "local")


def _enable_docs() -> bool:
    return environ.get("ENABLE_DOCS", "true").lower() in {"1", "true", "yes", "on"}


def healthz() -> HealthPayload:
    """Return process health payload for liveness checks."""

    return HealthPayload(service=_service_name(), environment=_environment(), status="ok")


def register_route_groups(application: ApiApplication) -> None:
    """Register starter route groups for the API shell."""

    application.routes.append(RouteDescriptor(method="GET", path="/v1/healthz", handler_name="healthz"))


def attach_middleware_stack(application: ApiApplication) -> None:
    del application


def attach_observability_and_error_handlers(application: ApiApplication) -> None:
    del application


def bind_background_dispatch_hooks(
    application: ApiApplication, dispatch_hook: Callable[[str], None] | None = None
) -> None:
    if dispatch_hook is None:
        return
    dispatch_hook("startup")
    application.startup_hooks.append("dispatch_hook")


def create_application() -> ApiApplication:
    """Create and configure the API application shell."""

    application = ApiApplication(name=f"{_service_name()} API", docs_enabled=_enable_docs())
    attach_middleware_stack(application)
    register_route_groups(application)
    attach_observability_and_error_handlers(application)
    bind_background_dispatch_hooks(application)
    return application
