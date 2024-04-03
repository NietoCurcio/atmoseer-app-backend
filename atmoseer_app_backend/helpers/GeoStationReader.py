import csv
from pathlib import Path
from collections.abc import Generator

from .models.Station import Station

class GeoStationReader:
    def __init__(self, geo_stations_path: str) -> None:
        self.geo_stations_path = self._initialize_geo_stations_path(geo_stations_path)

    def _initialize_geo_stations_path(self, geo_stations_path: str) -> str:
        path = Path(geo_stations_path)
        if not path.is_file(): raise FileNotFoundError(f"File '{path}' not found.")
        return path

    def csv_row_generator(
        self,
        file_path: str | None = None,
        skip_header: bool = True
    ) -> Generator[Station, None, None]:
        file_path = file_path or self.geo_stations_path
        with open(file_path, 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)

            if skip_header: next(csv_reader)
            
            for row in csv_reader:
                station_name, latitude, longitude = row
                yield Station(
                    station_name=station_name,
                    latitude=float(latitude),
                    longitude=float(longitude)
                )

geo_station_reader = GeoStationReader("./atmoseer_app_backend/helpers/stations.csv")
