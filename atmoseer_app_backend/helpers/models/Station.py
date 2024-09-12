from datetime import datetime
from typing import Union

from pydantic import BaseModel


class Station(BaseModel):
    name: str
    state: str
    situation: str
    latitude: float
    longitude: float
    altitude: Union[float, None] = None
    start_date: Union[datetime, None] = None
    station_id: str
