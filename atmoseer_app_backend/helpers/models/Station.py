from pydantic import BaseModel
from datetime import datetime

class Station(BaseModel):
    name: str
    state: str
    situation: str
    latitude: float
    longitude: float
    altitude: float | None = None
    start_date: datetime | None = None
    station_id: str
