from .interfaces.Service import Service

class DogsService(Service):
    def __init__(self) -> None:
        pass

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
    
dogs_service = DogsService()