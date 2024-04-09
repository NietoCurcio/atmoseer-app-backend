from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from atmoseer_app_backend.api.router import api_router
from atmoseer_app_backend.config import settings
from atmoseer_app_backend.services.exceptions import add_custom_exception_handler

app = FastAPI(
    title="Atmoseer-app API",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_custom_exception_handler(app)

app.include_router(api_router)
