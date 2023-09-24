from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


class Setting(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=f"{BASE_DIR}/.env", env_file_encoding="utf-8"
    )
    postgres_user: str
    postgres_password: str
    postgres_db: str = "microblog_db"
    pg_container_name: str
    pg_port: int = 5432
    db_url_docker: str
    db_url: str
    db_echo: bool = False
    api_v1_prefix: str = "/api"
    pgadmin_default_email: str
    pgadmin_default_password: str
    pgadmin_listen_port: int
    media_path: str = f"{BASE_DIR}/media"
    error_response: dict[str:bool, str:str, str:str] = {
        "result": False,
        "error_type": "",
        "error_message": "",
    }


settings = Setting()
