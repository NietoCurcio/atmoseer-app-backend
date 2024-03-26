from .interfaces import Repository

class SomeRepository(Repository):
    def __init__(self):
        pass

    def get(self, id):
        pass

    def get_all(self):
        pass

    def create(self, entity):
        pass

    def update(self, entity):
        pass

    def delete(self, entity):
        pass

some_repository = SomeRepository()