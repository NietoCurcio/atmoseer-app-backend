from typing import Annotated

from fastapi import APIRouter, Query

from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.services import forecast_service

log = logger.get_logger(__name__)

router = APIRouter()


@router.get("/")
async def forecast_latitude_longitude(
    latitude: Annotated[float, Query(description="Latitude to forecast", ge=-90, le=90)],
    longitude: Annotated[float, Query(description="Longitude to forecast", ge=-180, le=180)],
):
    log.info(f"Forecasting latitude {latitude} and longitude {longitude}")
    return await forecast_service.get_data(latitude, longitude)
