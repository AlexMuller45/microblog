from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent.parent.parent


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env", env_file_encoding="utf-8"
    )
    pg_user: str
    pg_password: str
    pg_db: str = "microblog_db"
    pg_port: int = 5432
    db_url: str
    db_url_app: str
    db_echo: bool = False
    api_v1_prefix: str = "/api"


settings = Setting()
