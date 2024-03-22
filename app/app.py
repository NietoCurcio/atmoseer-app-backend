from fastapi import FastAPI

from app.api.router import api_router
from app.exceptions import add_custom_exception_handler

app = FastAPI(title="Atmoseer-app API", version="0.1.0")

add_custom_exception_handler(app)

app.include_router(api_router)
