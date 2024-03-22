from .interfaces.Service import Service

class ForecastService(Service):
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
    
forecast_service = ForecastService()