import os
from typing import ClassVar

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Pokeberries API"
    app_version: str = "1.0.0"

    debug: bool = False
    reload: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    api_prefix: ClassVar[str] = ""

    app_poke_api: str = os.environ.get("APP_POKE_API", "")

    url_origins: list[str] = ["*"]

    model_config = SettingsConfigDict(
        env_file=".env",
        env_prefix="APP_",
        env_file_encoding="utf-8",
        extra="allow",
    )


settings = Settings()
