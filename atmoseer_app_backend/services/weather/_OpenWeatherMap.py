from datetime import UTC, datetime

from httpx import AsyncClient

from atmoseer_app_backend.config import settings
from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.services.exceptions import Unauthorized

from .interfaces import WeatherService
from .models import Weather

log = logger.get_logger(__name__)


class _OpenWeatherMap(WeatherService):
    def __init__(self) -> None:
        self.base_url = "https://api.openweathermap.org/data/2.5"
        self.token = settings.OPEN_WEATHER_MAP_TOKEN

    def get_service_name(self) -> str:
        return "openweathermap"

    def _meter_per_second_to_km_per_hour(self, speed: float) -> float:
        return speed * 3.6

    def _map_weather_main_to_wmo_condition(self, weather_main: str) -> str:
        """
        TODO, improve this code, add more conditions and use enums
        """
        weather_main_to_wmo_condition = {
            "Thunderstorm": "Thunderstorm: Slight intensity",
            "Drizzle": "Drizzle: Light intensity",
            "Rain": "Rain: Slight intensity",
            "Snow": "Snow grains",
            "Atmosphere": "Fog",
            "Clear": "Clear sky",
            "Clouds": "Overcast",
        }
        return weather_main_to_wmo_condition.get(weather_main, "Unknown")

    def _timestamp_to_iso(self, timestamp: int) -> str:
        timestamp_iso_utc = datetime.fromtimestamp(timestamp, UTC)
        return timestamp_iso_utc.isoformat()

    async def get_current_weather(self, lat: float, long: float) -> Weather:
        if self.token is None:
            log.error("OpenWeatherMap token not found")
            raise Unauthorized("OpenWeatherMap token not found")

        params = {"lat": lat, "lon": long, "appid": self.token, "units": "metric"}
        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}/weather", params=params)

        response.raise_for_status()
        data = response.json()

        log.info(f"OpenWeatherMap response: {data}")

        wmo_condition = self._map_weather_main_to_wmo_condition(data["weather"][0]["main"])
        wmo_code = self._wmo_condition_to_wmo_weather_code(wmo_condition)

        weather = Weather(
            wmo_code=wmo_code,
            condition=wmo_condition,
            temperature=data["main"]["temp"],
            cloud_cover=data["clouds"]["all"],
            precipitation=data.get("rain", {}).get("1h"),
            humidity=data["main"]["humidity"],
            wind_speed=self._meter_per_second_to_km_per_hour(data["wind"]["speed"]),
            wind_direction=data["wind"]["deg"],
            timestamp=self._timestamp_to_iso(data["dt"]),
            latitude=data["coord"]["lat"],
            longitude=data["coord"]["lon"],
        )

        return weather


_open_weather_map = _OpenWeatherMap()
