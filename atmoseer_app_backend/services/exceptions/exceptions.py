from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED,
    HTTP_500_INTERNAL_SERVER_ERROR,
)

from .BaseHTTPException import BaseHTTPException


class BadRequest(BaseHTTPException):
    def __init__(self, message: str, error: Exception = None):
        super().__init__(status_code=HTTP_400_BAD_REQUEST, message=message, error=error)


class InternalServerError(BaseHTTPException):
    def __init__(self, message: str, error: Exception = None):
        super().__init__(status_code=HTTP_500_INTERNAL_SERVER_ERROR, message=message, error=error)


class Unauthorized(BaseHTTPException):
    def __init__(self, message: str, error: Exception = None):
        super().__init__(status_code=HTTP_401_UNAUTHORIZED, message=message, error=error)
