from abc import ABC, abstractmethod


class Service(ABC):
    @abstractmethod
    def get_data(self):
        pass
