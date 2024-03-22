from . import BaseHTTPException
from starlette.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_401_UNAUTHORIZED
)

class BadRequest(BaseHTTPException):
    def __init__(self, message: str = None):
        super(BadRequest, self).__init__(status_code=HTTP_400_BAD_REQUEST, message=message)

class Unauthorized(BaseHTTPException):
    def __init__(self, message: str = None):
        super(Unauthorized, self).__init__(status_code=HTTP_401_UNAUTHORIZED, message=message)