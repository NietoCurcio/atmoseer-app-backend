from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator

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
    POSTGRES_PASSWORD: str = "password"
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: str = "5432"
    POSTGRES_DB: str = "atmoseer"
    PGADMIN_DEFAULT_EMAIL: str = "pgadmin4@pgadmin.org"
    PGADMIN_DEFAULT_PASSWORD: str = "admin"

    @model_validator(mode="after")
    def _validate_env(self):
        if self.ENV in ENVs: return self
        logger.get_logger(__name__).warning(f'Invalid ENV: {self.ENV}. Setting to "{ENVs.DEV.value}"')
        self.ENV = ENVs.DEV.value
        return self

settings = Settings()
