from datetime import UTC, datetime

from httpx import AsyncClient

from atmoseer_app_backend.helpers.Logger import logger

from .interfaces import WeatherService
from .models import Weather

log = logger.get_logger(__name__)


class _OpenMeteo(WeatherService):
    def __init__(self) -> None:
        self.base_url = "https://api.open-meteo.com/v1"

    def get_service_name(self) -> str:
        return "open-meteo"

    def _to_iso(self, timestamp: str) -> str:
        timestamp_iso_utc = datetime.fromisoformat(timestamp).replace(tzinfo=UTC)
        return timestamp_iso_utc.isoformat()

    async def get_current_weather(self, lat: float, long: float) -> Weather:
        params = {
            "latitude": lat,
            "longitude": long,
            "current": [
                "temperature_2m",
                "relative_humidity_2m",
                "precipitation",
                "wind_speed_10m",
                "wind_direction_10m",
                "weather_code",
                "cloud_cover",
            ],
            "timezone": "GMT",
        }

        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}/forecast", params=params)

        response.raise_for_status()
        data = response.json()

        log.info(f"OpenMeteo response: {data}")

        weather = Weather(
            wmo_code=data["current"]["weather_code"],
            condition=self._wmo_weather_code_to_wmo_condition(data["current"]["weather_code"]),
            temperature=data["current"]["temperature_2m"],
            cloud_cover=data["current"]["cloud_cover"],
            precipitation=data["current"]["precipitation"],
            humidity=data["current"]["relative_humidity_2m"],
            wind_speed=data["current"]["wind_speed_10m"],
            wind_direction=data["current"]["wind_direction_10m"],
            timestamp=self._to_iso(data["current"]["time"]),
            latitude=data["latitude"],
            longitude=data["longitude"],
        )

        return weather


_open_meteo = _OpenMeteo()
