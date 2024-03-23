from enum import Enum
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import model_validator

from app.helpers.Logger import logger

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
        if self.ENV in ENVs: return self
        logger.get_logger(__name__).error(f'Invalid ENV: {self.ENV}. Setting to "{ENVs.DEV.value}"')
        self.ENV = ENVs.DEV.value
        return self

settings = Settings()
