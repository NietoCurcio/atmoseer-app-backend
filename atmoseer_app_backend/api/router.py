from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from atmoseer_app_backend.api.routes import (
    dogs,
    forecast
)

api_router = APIRouter()

@api_router.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/docs")

api_router.include_router(dogs.router, prefix="/dogs", tags=["dogs"])
api_router.include_router(forecast.router, prefix="/forecast", tags=["forecast"])
