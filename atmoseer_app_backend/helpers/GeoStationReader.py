import csv
from collections.abc import Generator
from datetime import datetime
from pathlib import Path
from typing import Union

from .Logger import logger
from .models.Station import Station

log = logger.get_logger(__name__)


class GeoStationReader:
    def __init__(self, geo_stations_path: str) -> None:
        self.geo_stations_path = self._initialize_geo_stations_path(geo_stations_path)

    def _initialize_geo_stations_path(self, geo_stations_path: str) -> str:
        path = Path(geo_stations_path)
        if not path.is_file():
            raise FileNotFoundError(f"File '{path}' not found.")
        return path

    def _create_station(self, row: list[str], ignore_first_column: bool) -> Station:
        if ignore_first_column:
            row = row[1:]

        # Pydantic maintains field order - https://docs.pydantic.dev/1.10/usage/models/#field-ordering
        columns = Station.model_fields.keys()

        assert len(columns) == len(row), "Number of columns and row do not match"

        try:
            row = map(str.strip, row)
            station = dict(zip(columns, row))

            station["latitude"] = float(station["latitude"])
            station["longitude"] = float(station["longitude"])

            station["altitude"] = (
                float(station["altitude"].replace(",", ".")) if station["altitude"] else None
            )

            station["start_date"] = (
                datetime.strptime(station["start_date"], "%d/%m/%Y") if station["start_date"] else None
            )

            return Station(**station)
        except Exception as e:
            log.error(f"Error creating Station: {e}")
            raise e

    def csv_row_generator(
        self,
        file_path: Union[str, None] = None,
        skip_header: bool = True,
        ignore_first_column: bool = True,
    ) -> Generator[Station, None, None]:
        file_path = file_path or self.geo_stations_path
        try:
            csvfile = open(file_path, newline="")
            csv_reader = csv.reader(csvfile)

            header = next(csv_reader)

            if not skip_header:
                yield self._create_station(header, ignore_first_column)

            for row in csv_reader:
                yield self._create_station(row, ignore_first_column)
        except Exception as e:
            log.error(f"Error reading CSV file '{file_path}': {e}")
            raise e
        finally:
            csvfile.close()


geo_station_reader = GeoStationReader("./atmoseer_app_backend/helpers/WeatherStations.csv")
