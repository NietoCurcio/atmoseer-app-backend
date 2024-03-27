from .interfaces import Service

from atmoseer_app_backend.repositories import (
    some_repository, Repository
)

class SomeService(Service):
    def __init__(self, repository: Repository) -> None:
        # super().__init__(some_repository)
        self.repository = repository

    def get_data(self):
        return [{
            "name": "Buddy",
            "breed": "Golden Retriever",
            "age": 5
        }, {
            "name": "Milo",
            "breed": "Pug",
            "age": 3
        }]
    
some_service = SomeService(repository=some_repository)
