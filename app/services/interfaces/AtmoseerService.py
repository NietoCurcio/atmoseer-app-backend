from .Service import Service as Service
from app.helpers.PathHelper import path_helper

class AtmoseerService(Service):
    def __init__(self) -> None:
        self.path_helper = path_helper
