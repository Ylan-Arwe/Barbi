"""Typed runtime settings for API, worker, integrations, AI, and governance controls."""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from os import environ
from typing import Literal, cast


def _read_env(name: str, default: str) -> str:
    """Read a raw environment value with a default fallback."""

    return environ.get(name, default)


def _read_bool(name: str, default: bool) -> bool:
    """Read a boolean environment variable."""

    value = _read_env(name, "true" if default else "false").strip().lower()
    return value in {"1", "true", "yes", "on"}


def _read_int(name: str, default: int, *, minimum: int, maximum: int) -> int:
    """Read and range-validate an integer environment variable."""

    value = int(_read_env(name, str(default)))
    if value < minimum or value > maximum:
        message = f"Environment variable {name} must be between {minimum} and {maximum}; got {value}."
        raise ValueError(message)
    return value


def _read_float(name: str, default: float, *, minimum: float, maximum: float) -> float:
    """Read and range-validate a float environment variable."""

    value = float(_read_env(name, str(default)))
    if value < minimum or value > maximum:
        message = f"Environment variable {name} must be between {minimum} and {maximum}; got {value}."
        raise ValueError(message)
    return value


def _read_csv(name: str, default: tuple[str, ...]) -> tuple[str, ...]:
    """Read a comma-separated environment variable into a tuple."""

    raw_value = _read_env(name, ",".join(default))
    return tuple(entry.strip() for entry in raw_value.split(",") if entry.strip())


@dataclass(frozen=True)
class PlatformSettings:
    """Cross-cutting application metadata and environment controls."""

    environment: Literal["local", "dev", "staging", "prod"]
    service_name: str
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    enable_json_logs: bool
    telemetry_enabled: bool


@dataclass(frozen=True)
class ApiSettings:
    """HTTP API runtime settings."""

    host: str
    port: int
    workers: int
    enable_docs: bool
    cors_allowed_origins: tuple[str, ...]


@dataclass(frozen=True)
class WorkerSettings:
    """Background worker and queue settings."""

    queue_name: str
    prefetch_multiplier: int
    max_retries: int
    task_soft_time_limit_seconds: int


@dataclass(frozen=True)
class DatabaseSettings:
    """Transactional database settings for SQLAlchemy and Alembic."""

    url: str
    echo_sql: bool


@dataclass(frozen=True)
class QueueSettings:
    """Redis-backed queue and result backend settings."""

    broker_url: str
    result_backend_url: str


@dataclass(frozen=True)
class SearchSettings:
    """Lexical and semantic search runtime settings."""

    opensearch_url: str
    candidate_index_name: str
    jobs_index_name: str
    semantic_provider: Literal["pgvector", "none"]


@dataclass(frozen=True)
class IntegrationSettings:
    """Integration provider and webhook settings."""

    ats_provider: Literal["none", "greenhouse", "lever"]
    crm_provider: Literal["none", "salesforce"]
    webhook_signing_secret: str


@dataclass(frozen=True)
class AISettings:
    """AI gateway and model behavior defaults."""

    provider: Literal["openai", "none"]
    model: str
    temperature: float
    max_output_tokens: int


@dataclass(frozen=True)
class AnalyticsSettings:
    """Metrics and event pipeline settings."""

    enable_event_emission: bool
    event_sink: Literal["stdout", "none"]


@dataclass(frozen=True)
class NotificationSettings:
    """Notification and outbound messaging defaults."""

    email_provider: Literal["none", "smtp"]
    from_email: str


@dataclass(frozen=True)
class ComplianceSettings:
    """Governance-sensitive defaults and kill switches."""

    require_human_review_for_scoring_overrides: bool
    outreach_requires_suppression_check: bool
    allow_external_data_export: bool


@dataclass(frozen=True)
class ApplicationRuntimeSettings:
    """API and worker runtime settings group."""

    api: ApiSettings
    worker: WorkerSettings


@dataclass(frozen=True)
class DataRuntimeSettings:
    """Database, queue, and search runtime settings group."""

    database: DatabaseSettings
    queue: QueueSettings
    search: SearchSettings


@dataclass(frozen=True)
class ServiceRuntimeSettings:
    """Integrations, AI, analytics, and notifications group."""

    integrations: IntegrationSettings
    ai: AISettings
    analytics: AnalyticsSettings
    notifications: NotificationSettings


@dataclass(frozen=True)
class RuntimeSettings:
    """Top-level container for all typed runtime settings groups."""

    platform: PlatformSettings
    application: ApplicationRuntimeSettings
    data: DataRuntimeSettings
    services: ServiceRuntimeSettings
    compliance: ComplianceSettings


@lru_cache(maxsize=1)
def load_settings() -> RuntimeSettings:
    """Load and cache immutable runtime settings from environment variables."""

    platform_environment = cast(Literal["local", "dev", "staging", "prod"], _read_env("ENVIRONMENT", "local"))
    log_level = cast(Literal["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], _read_env("LOG_LEVEL", "INFO"))

    return RuntimeSettings(
        platform=PlatformSettings(
            environment=platform_environment,
            service_name=_read_env("SERVICE_NAME", "ai-recruiting-platform"),
            log_level=log_level,
            enable_json_logs=_read_bool("ENABLE_JSON_LOGS", True),
            telemetry_enabled=_read_bool("TELEMETRY_ENABLED", True),
        ),
        application=ApplicationRuntimeSettings(
            api=ApiSettings(
                host=_read_env("HOST", "0.0.0.0"),
                port=_read_int("PORT", 8000, minimum=1, maximum=65535),
                workers=_read_int("WORKERS", 1, minimum=1, maximum=32),
                enable_docs=_read_bool("ENABLE_DOCS", True),
                cors_allowed_origins=_read_csv("CORS_ALLOWED_ORIGINS", ("http://localhost:3000",)),
            ),
            worker=WorkerSettings(
                queue_name=_read_env("QUEUE_NAME", "default"),
                prefetch_multiplier=_read_int("PREFETCH_MULTIPLIER", 1, minimum=1, maximum=64),
                max_retries=_read_int("MAX_RETRIES", 3, minimum=0, maximum=100),
                task_soft_time_limit_seconds=_read_int("TASK_SOFT_TIME_LIMIT_SECONDS", 120, minimum=5, maximum=3600),
            ),
        ),
        data=DataRuntimeSettings(
            database=DatabaseSettings(
                url=_read_env(
                    "DATABASE_URL",
                    _read_env("POSTGRES_URL", "postgresql://postgres:postgres@localhost:5432/ai_recruiting"),
                ),
                echo_sql=_read_bool("ECHO_SQL", False),
            ),
            queue=QueueSettings(
                broker_url=_read_env("BROKER_URL", "redis://localhost:6379/0"),
                result_backend_url=_read_env("RESULT_BACKEND_URL", "redis://localhost:6379/1"),
            ),
            search=SearchSettings(
                opensearch_url=_read_env("OPENSEARCH_URL", "http://localhost:9200"),
                candidate_index_name=_read_env("CANDIDATE_INDEX_NAME", "candidates-v1"),
                jobs_index_name=_read_env("JOBS_INDEX_NAME", "jobs-v1"),
                semantic_provider=cast(Literal["pgvector", "none"], _read_env("SEMANTIC_PROVIDER", "pgvector")),
            ),
        ),
        services=ServiceRuntimeSettings(
            integrations=IntegrationSettings(
                ats_provider=cast(Literal["none", "greenhouse", "lever"], _read_env("ATS_PROVIDER", "none")),
                crm_provider=cast(Literal["none", "salesforce"], _read_env("CRM_PROVIDER", "none")),
                webhook_signing_secret=_read_env("WEBHOOK_SIGNING_SECRET", "replace-me"),
            ),
            ai=AISettings(
                provider=cast(Literal["openai", "none"], _read_env("PROVIDER", "openai")),
                model=_read_env("MODEL", "gpt-5-mini"),
                temperature=_read_float("TEMPERATURE", 0.1, minimum=0.0, maximum=1.0),
                max_output_tokens=_read_int("MAX_OUTPUT_TOKENS", 1200, minimum=128, maximum=32000),
            ),
            analytics=AnalyticsSettings(
                enable_event_emission=_read_bool("ENABLE_EVENT_EMISSION", True),
                event_sink=cast(Literal["stdout", "none"], _read_env("EVENT_SINK", "stdout")),
            ),
            notifications=NotificationSettings(
                email_provider=cast(Literal["none", "smtp"], _read_env("EMAIL_PROVIDER", "none")),
                from_email=_read_env("FROM_EMAIL", "noreply@example.com"),
            ),
        ),
        compliance=ComplianceSettings(
            require_human_review_for_scoring_overrides=_read_bool("REQUIRE_HUMAN_REVIEW_FOR_SCORING_OVERRIDES", True),
            outreach_requires_suppression_check=_read_bool("OUTREACH_REQUIRES_SUPPRESSION_CHECK", True),
            allow_external_data_export=_read_bool("ALLOW_EXTERNAL_DATA_EXPORT", False),
        ),
    )


def clear_settings_cache() -> None:
    """Clear cached settings for tests or process-level reload scenarios."""

    load_settings.cache_clear()
