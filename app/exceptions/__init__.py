from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from abc import ABC

class BaseHTTPException(ABC, Exception):
    def __init__(self, status_code: int, message: str, error: Exception = None):
        self.status_code = status_code
        self.message = message
        self.error = error

def add_custom_exception_handler(app: FastAPI):
    @app.exception_handler(BaseHTTPException)
    async def inner(request: Request, exc: BaseHTTPException):
        content = {
            "message": exc.message,
            "status_code": exc.status_code,
        }
        if exc.error is not None: content["error"] = str(exc.error)
        return JSONResponse(status_code=exc.status_code, content=content)
    return inner