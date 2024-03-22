from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from abc import ABC

class BaseHTTPException(ABC, Exception):
    def __init__(self, status_code: int, message: str = None):
        self.status_code = status_code
        self.message = message

def add_custom_exception_handler(app: FastAPI):
    @app.exception_handler(BaseHTTPException)
    async def inner(request: Request, exc: BaseHTTPException):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "message": exc.message,
                "status_code": exc.status_code,
            },
        )
    return inner