from fastapi import FastAPI

from atmoseer_app_backend.api.router import api_router
from atmoseer_app_backend.services.exceptions import add_custom_exception_handler

app = FastAPI(title="Atmoseer-app API", version="0.1.0")

add_custom_exception_handler(app)

app.include_router(api_router)
