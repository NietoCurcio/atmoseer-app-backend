from fastapi import APIRouter

from app.api.routes import dogs

api_router = APIRouter()
api_router.include_router(dogs.router, prefix="/dogs", tags=["dogs"])