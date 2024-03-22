from fastapi import APIRouter

from app.api.routes import (
    dogs,
    forecast
)

api_router = APIRouter()
api_router.include_router(dogs.router, prefix="/dogs", tags=["dogs"])
api_router.include_router(forecast.router, prefix="/forecast", tags=["forecast"])
