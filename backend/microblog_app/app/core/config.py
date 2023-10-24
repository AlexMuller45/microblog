"""Конфигурационный файл приложения"""

from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


ORIGINS = [
    "http://localhost",
    "http://localhost:80",
]

ALL_METHODS = [
    "DELETE",
    "GET",
    # "HEAD",
    # "OPTIONS",
    # "PATCH",
    "POST",
    # "PUT",
]

SAFELISTED_HEADERS = [
    "Accept",
    "Accept-Language",
    "Accept-Encoding",
    "Connection",
    "Content-Language",
    "Content-Type",
    "Set-Cookie",
    "Access-Control-Allow-Headers",
    "Access-Control-Allow-Origin",
    "Authorization",
]


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env", env_file_encoding="utf-8"
    )
    postgres_user: str
    postgres_password: str
    postgres_db: str = "microblog_db"
    pg_container_name: str
    pg_port: int = 5432
    db_url: str
    db_echo: bool = False
    api_v1_prefix: str = "/api"
    pgadmin_default_email: str
    pgadmin_default_password: str
    pgadmin_listen_port: int
    media_path: str = f"{BASE_DIR}/app/media"
    filename: str = "{media_id}__{file_name}"
    origins: list[str] = ORIGINS
    all_methods: list[str] = ALL_METHODS
    safe_listed_headers: list[str] = SAFELISTED_HEADERS


settings = Setting()
