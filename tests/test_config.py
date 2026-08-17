import pytest
from pydantic import ValidationError

from safecart_api.config import Settings, get_settings


def test_settings_have_safe_local_defaults() -> None:
    settings = Settings()

    assert settings.env == "development"
    assert settings.ai_base_url == "http://localhost:8001"
    assert settings.ai_timeout_seconds == 2.0


def test_ai_timeout_must_be_positive() -> None:
    with pytest.raises(ValidationError):
        Settings(ai_timeout_seconds=0)


def test_get_settings_is_cached() -> None:
    get_settings.cache_clear()
    assert get_settings() is get_settings()
