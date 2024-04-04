import logging
import inspect
from types import FrameType

class Logger:
    def __init__(self):
        self.logger = logging.getLogger('logger')
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S'
        ))
        self.logger.addHandler(handler)

    def _get_module_name(self, frame: FrameType) -> str | None:
        module = inspect.getmodule(frame)
        return module.__name__ if module is not None else None

    def _get_caller_frame(self, frame: FrameType) -> FrameType | None:
        if frame is None: return None

        module_name = self._get_module_name(frame)
        if module_name is None: return None

        if module_name == __name__: return self._get_caller_frame(frame.f_back)
        
        return frame
    
    def _get_caller_name(self) -> str | None:
        frame = self._get_caller_frame(inspect.currentframe())
        if frame is None: return None
        module_name = self._get_module_name(frame)
        return module_name if module_name is not None else None
    
    def _log(self, level: int, message: str):
        level_name = logging.getLevelName(level).lower()

        caller_name = self._get_caller_name()
        logger = self.logger.getChild(caller_name) if caller_name else self.logger
        log_method = getattr(logger, level_name)
        log_method(message)

    def debug(self, message: str):
        self._log(logging.DEBUG, message)

    def info(self, message: str):
        self._log(logging.INFO, message)

    def warning(self, message: str):
        self._log(logging.WARNING, message)

    def error(self, message: str):
        self._log(logging.ERROR, message)

    def critical(self, message: str):
        self._log(logging.CRITICAL, message)

logger = Logger()
