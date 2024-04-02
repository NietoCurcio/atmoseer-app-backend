from pydantic import BaseModel

class Station(BaseModel):
    station_name: str
    latitude: float
    longitude: float