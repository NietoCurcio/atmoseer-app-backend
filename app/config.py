from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator

from app.Logger import logger

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

    @model_validator(mode="after")
    def _validate_env(self):
        try:
            assert self.ENV in [env.value for env in ENVs]
        except AssertionError:
            log = logger.get_logger(__name__)
            log.error(f'Invalid ENV: {self.ENV}. Setting to "{ENVs.DEV.value}"')
            self.ENV = ENVs.DEV.value
        return self

settings = Settings()
