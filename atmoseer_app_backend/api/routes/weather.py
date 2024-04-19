from typing import Annotated

from fastapi import APIRouter, Query

from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.services import weather_service
from atmoseer_app_backend.services.weather.models import Weather

log = logger.get_logger(__name__)

router = APIRouter()


@router.get("/")
async def get_current_weather(
    latitude: Annotated[float, Query(description="Latitude", ge=-90, le=90)],
    longitude: Annotated[float, Query(description="Longitude", ge=-180, le=180)],
    service: Annotated[
        str, Query(description="Service to use for fetch current weather")
    ] = weather_service.get_default_service_name(),
) -> Weather:
    log.info(f"Getting weather for latitude {latitude} and longitude {longitude} using service {service}")
    weather = await weather_service.get_current_weather(latitude, longitude, service)
    return weather


@router.get("/services")
async def get_services() -> list[str]:
    return weather_service.get_service_names()
