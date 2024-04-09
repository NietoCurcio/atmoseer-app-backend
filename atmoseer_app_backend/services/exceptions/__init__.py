from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from atmoseer_app_backend.services.exceptions.BaseHTTPException import BaseHTTPException

from .exceptions import BadRequest, InternalServerError, Unauthorized


def add_custom_exception_handler(app: FastAPI):
    @app.exception_handler(BaseHTTPException)
    async def inner(request: Request, exc: BaseHTTPException):
        content = {"message": exc.message}
        if exc.error is not None:
            content["error"] = str(exc.error)
        return JSONResponse(status_code=exc.status_code, content=content)

    return inner
