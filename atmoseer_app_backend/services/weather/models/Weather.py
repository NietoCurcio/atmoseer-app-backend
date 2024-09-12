from enum import StrEnum
from typing import Union

from pydantic import BaseModel, Field


class WmoCondition(StrEnum):
    CLEAR_SKY = "Clear sky"


class Weather(BaseModel):
    wmo_code: Union[int, None] = Field(description="Weather WMO code", example=0)
    condition: Union[str, None] = Field(description="Weather WMO condition", example="Clear sky")
    temperature: float = Field(description="Temperature in Celsius", example=27.3)
    cloud_cover: Union[float, None] = Field(description="Cloud cover in percentage", example=0.0)
    precipitation: Union[float, None] = Field(description="Precipitation in mm", example=0.0)
    humidity: float = Field(description="Relative humidity in percentage", example=79)
    wind_direction: float = Field(description="Wind direction in degrees", example=211)
    wind_speed: float = Field(description="Wind speed in km/h", example=2.1)
    timestamp: str = Field(
        description="Timestamp of the weather data in ISO 8601 format in UTC",
        example="2024-04-18T19:30:00+00:00",
    )
    latitude: float = Field(description="Latitude of the weather data", example=-22)
    longitude: float = Field(description="Longitude of the weather data", example=-43)
