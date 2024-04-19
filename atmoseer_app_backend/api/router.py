from fastapi import APIRouter
from fastapi.responses import RedirectResponse

from atmoseer_app_backend.api.routes import forecast, heros, weather

api_router = APIRouter()


@api_router.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url="/docs")


api_router.include_router(heros.router, prefix="/heros", tags=["heros"])
api_router.include_router(forecast.router, prefix="/forecast", tags=["forecast"])
api_router.include_router(weather.router, prefix="/weather", tags=["weather"])
