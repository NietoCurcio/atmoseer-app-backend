from collections.abc import Collection, Iterator

from .GeoStationReader import GeoStationReader, geo_station_reader
from .GreatCircleDistance import GreatCircleDistance, great_circle_distance
from .models.Station import Station


class GeoStations(Collection):
    def __init__(
        self,
        great_circle_distance: GreatCircleDistance,
        geo_station_reader: GeoStationReader,
    ) -> None:
        self.great_circle_distance = great_circle_distance
        self.geo_station_reader = geo_station_reader

    def __contains__(self, station_id_or_name: str) -> bool:
        for station in self.geo_station_reader.csv_row_generator():
            if station.station_id == station_id_or_name or station.name == station_id_or_name:
                return True
        return False

    def __iter__(self) -> Iterator[Station]:
        return self.geo_station_reader.csv_row_generator()

    def __len__(self) -> int:
        return sum(1 for _ in self.geo_station_reader.csv_row_generator())

    def get_nearest_station(self, latitude: float, longitude: float) -> Station:
        min_distance = float("inf")
        nearest_station = None
        for station in self:
            distance = self.great_circle_distance.get_distance(
                latitude, longitude, station.latitude, station.longitude
            )
            if distance < min_distance:
                min_distance = distance
                nearest_station = station
        return nearest_station


geo_stations = GeoStations(great_circle_distance, geo_station_reader)
