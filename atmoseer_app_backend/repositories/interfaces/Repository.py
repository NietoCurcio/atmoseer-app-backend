from abc import ABC, abstractmethod


class Repository(ABC):
    # @abstractmethod
    # def get(self, id):
    #     pass

    # @abstractmethod
    # def get_all(self):
    #     pass

    @abstractmethod
    def create(self, entity):
        pass

    # @abstractmethod
    # def update(self, entity):
    #     pass

    # @abstractmethod
    # def delete(self, entity):
    #     pass
