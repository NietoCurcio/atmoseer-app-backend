from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator, PostgresDsn
from pydantic_core import MultiHostUrl

from atmoseer_app_backend.helpers.Logger import logger

class ENVs(Enum):
    DEV = "dev"
    PROD = "prod"

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="allow",
        env_ignore_empty=True
    )
    
    ENV: str = ENVs.DEV.value
    TOKEN_INMET: str | None = None

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "changeme"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str = "atmoseer"
    PGADMIN_DEFAULT_EMAIL: str = "pgadmin4@pgadmin.org"
    PGADMIN_DEFAULT_PASSWORD: str = "admin"

    POSTGRES_URL: PostgresDsn = MultiHostUrl.build(
        scheme="postgresql+psycopg2",
        username=POSTGRES_USER,
        password=POSTGRES_PASSWORD,
        host=POSTGRES_SERVER,
        port=POSTGRES_PORT,
        path=POSTGRES_DB
    )

    @model_validator(mode="after")
    def _validate_env(self):
        if self.ENV in ENVs: return self
        logger.get_logger(__name__).warning(f'Invalid ENV: {self.ENV}. Setting to "{ENVs.DEV.value}"')
        self.ENV = ENVs.DEV.value
        return self

settings = Settings()
