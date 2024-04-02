from collections.abc import Collection, Iterator

from .GreatCircleDistance import great_circle_distance, GreatCircleDistance
from .GeoStationReader import geo_station_reader, GeoStationReader
from .models.Station import Station

class GeoStations(Collection):
    def __init__(
        self,
        great_circle_distance: GreatCircleDistance,
        geo_station_reader: GeoStationReader,
    ) -> None:
        self.great_circle_distance = great_circle_distance
        self.geo_station_reader = geo_station_reader

    def __contains__(self, name: str) -> bool:
        for row in self.geo_station_reader.csv_row_generator():
            if row.station_name == name: return True
        return False
    
    def __iter__(self) -> Iterator[Station]:
        return self.geo_station_reader.csv_row_generator()
    
    def __len__(self) -> int:
        return sum(1 for _ in self.geo_station_reader.csv_row_generator())

    def get_nearest_station(self, latitude: float, longitude: float) -> str:
        min_distance = float('inf')
        nearest_station_name = None
        for station in self:
            distance = self.great_circle_distance.get_distance(
                latitude, longitude, station.latitude, station.longitude
            )
            if distance < min_distance:
                min_distance = distance
                nearest_station_name = station.station_name
        return nearest_station_name

geo_stations = GeoStations(great_circle_distance, geo_station_reader)
