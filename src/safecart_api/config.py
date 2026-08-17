from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="SAFECART_API_",
        extra="ignore",
    )

    env: str = "development"
    ai_base_url: str = "http://localhost:8001"
    ai_timeout_seconds: float = Field(default=2.0, gt=0, le=30)
    log_level: str = "INFO"


@lru_cache
def get_settings() -> Settings:
    return Settings()
