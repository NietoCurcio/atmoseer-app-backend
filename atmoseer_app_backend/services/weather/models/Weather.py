from enum import StrEnum

from pydantic import BaseModel, Field


class WmoCondition(StrEnum):
    CLEAR_SKY = "Clear sky"


class Weather(BaseModel):
    wmo_code: int | None = Field(description="Weather WMO code", example=0)
    condition: str | None = Field(description="Weather WMO condition", example="Clear sky")
    temperature: float = Field(description="Temperature in Celsius", example=27.3)
    cloud_cover: float | None = Field(description="Cloud cover in percentage", example=0.0)
    precipitation: float | None = Field(description="Precipitation in mm", example=0.0)
    humidity: float = Field(description="Relative humidity in percentage", example=79)
    wind_direction: float = Field(description="Wind direction in degrees", example=211)
    wind_speed: float = Field(description="Wind speed in km/h", example=2.1)
    timestamp: str = Field(
        description="Timestamp of the weather data in ISO 8601 format in UTC",
        example="2024-04-18T19:30:00+00:00",
    )
