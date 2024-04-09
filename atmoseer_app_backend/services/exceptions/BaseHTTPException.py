from abc import ABC


class BaseHTTPException(ABC, Exception):
    def __init__(self, status_code: int, message: str, error: Exception = None):
        self.status_code = status_code
        self.message = message
        self.error = error
