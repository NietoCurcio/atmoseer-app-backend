from datetime import datetime
from datetime import timezone as UTC

from httpx import AsyncClient

from atmoseer_app_backend.config import settings
from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.services.exceptions import Unauthorized

from .interfaces import WeatherService
from .models import Weather

log = logger.get_logger(__name__)


class _ClimaTempo(WeatherService):
    def __init__(self) -> None:
        self.base_url = "http://apiadvisor.climatempo.com.br/api/v1"
        self.token = settings.CLIMA_TEMPO_TOKEN

    def get_service_name(self) -> str:
        return "climatempo"

    def _to_iso(self, timestamp: str) -> str:
        timestamp_iso_utc = datetime.fromisoformat(timestamp).astimezone(UTC)
        return timestamp_iso_utc.isoformat()

    def _8_point_compass_to_degrees(self, wind_direction: str) -> float:
        compass_points = [
            "N",
            "NE",
            "E",
            "SE",
            "S",
            "SW",
            "W",
            "NW",
        ]
        return compass_points.index(wind_direction) * 360 / len(compass_points)

    async def get_current_weather(self, lat: float, long: float) -> Weather:
        """
        Idk, this api lacks some info, the docs also does not match with real response
        """
        if self.token is None:
            log.error("ClimaTempo token not found")
            raise Unauthorized("ClimaTempo token not found")

        params = {"token": self.token}

        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}/weather/locale/5959/current", params=params)

        response.raise_for_status()
        data = response.json()

        log.info(f"ClimaTempo response: {data}")

        timestamp = self._to_iso(data["data"]["date"])

        weather = Weather(
            wmo_code=None,
            condition=data["data"]["condition"],
            temperature=data["data"]["temperature"],
            cloud_cover=None,
            precipitation=None,
            humidity=data["data"]["humidity"],
            wind_speed=data["data"]["wind_velocity"],
            wind_direction=self._8_point_compass_to_degrees(data["data"]["wind_direction"]),
            timestamp=timestamp,
            latitude=lat,
            longitude=long,
        )

        return weather


_clima_tempo = _ClimaTempo()
