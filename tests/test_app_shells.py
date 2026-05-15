"""Tests for API, worker, and web shell bootstraps."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path
from types import ModuleType


def _load_module(module_name: str, relative_path: str) -> ModuleType:
    module_path = Path(__file__).resolve().parents[1] / relative_path
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to load module {module_name}.")
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module


API_MODULE = _load_module("api_surface_contract", "apps/api/api_surface_contract.py")
WORKER_MODULE = _load_module("worker_surface_contract", "apps/worker/worker_surface_contract.py")
WEB_MODULE = _load_module("web_surface_contract", "apps/web/web_surface_contract.py")


def test_create_application_registers_health_route() -> None:
    application = API_MODULE.create_application()
    paths = {route.path for route in application.routes}
    if "/v1/healthz" not in paths:
        raise AssertionError("Expected /v1/healthz route to be registered.")


def test_create_worker_runtime_configures_runtime() -> None:
    runtime = WORKER_MODULE.create_worker_runtime()
    if not runtime.broker_url:
        raise AssertionError("Expected broker URL to be configured.")
    task_names = {task.name for task in runtime.tasks}
    if "platform.worker.health_check" not in task_names:
        raise AssertionError("Expected worker health check task to be registered.")


def test_create_web_shell_contract_exposes_route_groups() -> None:
    contract = WEB_MODULE.create_web_shell_contract()
    if len(contract.route_groups) < 4:
        raise AssertionError("Expected at least four role-aware route groups in web shell contract.")
