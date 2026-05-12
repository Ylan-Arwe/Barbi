"""Tests for typed runtime settings loading."""

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path

from _pytest.monkeypatch import MonkeyPatch

MODULE_PATH = (
    Path(__file__).resolve().parents[1] / "src" / "ai_recruiting_platform" / "config" / "runtime_and_settings.py"
)
MODULE_SPEC = importlib.util.spec_from_file_location("runtime_and_settings", MODULE_PATH)
if MODULE_SPEC is None or MODULE_SPEC.loader is None:
    raise RuntimeError("Unable to load runtime settings module for tests.")
RUNTIME_MODULE = importlib.util.module_from_spec(MODULE_SPEC)
sys.modules[MODULE_SPEC.name] = RUNTIME_MODULE
MODULE_SPEC.loader.exec_module(RUNTIME_MODULE)


class RuntimeSettingsTests(unittest.TestCase):
    """Runtime settings behavior tests."""

    def setUp(self) -> None:
        """Start each test with a clean cache."""

        RUNTIME_MODULE.clear_settings_cache()

    def tearDown(self) -> None:
        """Reset cache after each test."""

        RUNTIME_MODULE.clear_settings_cache()

    def test_load_settings_reads_environment_overrides(self) -> None:
        """Settings loader should map environment variables into typed fields."""

        monkeypatch = MonkeyPatch()
        self.addCleanup(monkeypatch.undo)

        monkeypatch.setenv("ENVIRONMENT", "staging")
        monkeypatch.setenv("PORT", "8100")
        monkeypatch.setenv("DATABASE_URL", "postgresql://dbuser:dbpass@localhost:5432/app")
        monkeypatch.setenv("ALLOW_EXTERNAL_DATA_EXPORT", "true")

        settings = RUNTIME_MODULE.load_settings()

        self.assertEqual(settings.platform.environment, "staging")
        self.assertEqual(settings.application.api.port, 8100)
        self.assertEqual(settings.data.database.url, "postgresql://dbuser:dbpass@localhost:5432/app")
        self.assertTrue(settings.compliance.allow_external_data_export)

    def test_load_settings_is_cached_until_cache_clear(self) -> None:
        """Loader should cache settings to avoid repeated parse overhead."""

        monkeypatch = MonkeyPatch()
        self.addCleanup(monkeypatch.undo)

        monkeypatch.setenv("PORT", "8200")
        first = RUNTIME_MODULE.load_settings()

        monkeypatch.setenv("PORT", "8300")
        second = RUNTIME_MODULE.load_settings()

        self.assertIs(first, second)
        self.assertEqual(second.application.api.port, 8200)

        RUNTIME_MODULE.clear_settings_cache()
        third = RUNTIME_MODULE.load_settings()
        self.assertEqual(third.application.api.port, 8300)
