from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings with validation."""
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    anthropic_api_key: str
    openai_api_key: str | None = None
    default_model: str = "anthropic.claude-sonnet-4-0"
    log_level: str = "INFO"
    server_host: str = "0.0.0.0"
    server_port: int = 8080


settings = Settings()