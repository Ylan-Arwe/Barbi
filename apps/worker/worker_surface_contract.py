"""Worker shell bootstrap contract using framework-neutral runtime descriptors."""

from __future__ import annotations

from dataclasses import dataclass, field
from os import environ


@dataclass(frozen=True)
class WorkerTaskDescriptor:
    """Declarative background task registration metadata."""

    name: str


def _empty_tasks() -> list[WorkerTaskDescriptor]:
    return []


@dataclass
class WorkerRuntime:
    """Framework-neutral worker runtime payload."""

    broker_url: str
    result_backend_url: str
    tasks: list[WorkerTaskDescriptor] = field(default_factory=_empty_tasks)
    worker_send_task_events: bool = False
    task_default_retry_delay: int = 0


def _broker_url() -> str:
    return environ.get("BROKER_URL", "redis://localhost:6379/0")


def _result_backend_url() -> str:
    return environ.get("RESULT_BACKEND_URL", "redis://localhost:6379/1")


def register_job_handlers(worker_runtime: WorkerRuntime) -> None:
    worker_runtime.tasks.append(WorkerTaskDescriptor(name="platform.worker.health_check"))


def register_retry_and_dead_letter_policies(worker_runtime: WorkerRuntime) -> None:
    worker_runtime.task_default_retry_delay = 5


def attach_worker_observability(worker_runtime: WorkerRuntime) -> None:
    worker_runtime.worker_send_task_events = True


def create_worker_runtime() -> WorkerRuntime:
    worker_runtime = WorkerRuntime(broker_url=_broker_url(), result_backend_url=_result_backend_url())
    register_retry_and_dead_letter_policies(worker_runtime)
    attach_worker_observability(worker_runtime)
    register_job_handlers(worker_runtime)
    return worker_runtime


def run_worker(worker_runtime: WorkerRuntime) -> list[str]:
    """Return startup argv equivalent for worker process bootstrap."""

    del worker_runtime
    return ["worker", "--loglevel=INFO"]
