import logging


class Logger:
    def __init__(self):
        self.logger = logging.getLogger("log")
        self.logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                datefmt="%Y-%m-%d %H:%M:%S",
            )
        )
        self.logger.addHandler(handler)

    def get_logger(self, name: str) -> logging.Logger:
        return self.logger.getChild(name)


logger = Logger()
