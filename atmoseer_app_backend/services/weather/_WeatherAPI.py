from datetime import UTC, datetime

from httpx import AsyncClient

from atmoseer_app_backend.config import settings
from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.services.exceptions import Unauthorized

from .interfaces import WeatherService
from .models import Weather

log = logger.get_logger(__name__)


class _WeatherAPI(WeatherService):
    def __init__(self) -> None:
        self.base_url = "https://api.weatherapi.com/v1"
        self.token = settings.WEATHER_API_TOKEN

    def get_service_name(self) -> str:
        return "weatherapi"

    def _to_iso(self, timestamp: str) -> str:
        timestamp_iso_utc = datetime.fromisoformat(timestamp).astimezone(UTC)
        return timestamp_iso_utc.isoformat()

    def _16_point_compass_to_degrees(self, wind_direction: str) -> float:
        compass_points = [
            "N",
            "NNE",
            "NE",
            "ENE",
            "E",
            "ESE",
            "SE",
            "SSE",
            "S",
            "SSW",
            "SW",
            "WSW",
            "W",
            "WNW",
            "NW",
            "NNW",
        ]

        return compass_points.index(wind_direction) * 360 / len(compass_points)

    def _map_condition_text_to_wmo_condition(self, condition: str) -> str:
        """
        TODO improve this mapping, create a enum for the WMO conditions strings,
        see WmoCondition in models.py
        """
        contition_text_to_wmo_condition = {
            "Sunny": "Clear sky",
            "Partly Cloudy": "Partly cloudy",
            "Cloudy": "Overcast",
            "Overcast": "Overcast",
            "Mist": "Fog",
            "Patchy rain nearby": "Drizzle: Light intensity",
            "Patchy snow nearby": "Snow grains",
            "Patchy sleet nearby": "Snow grains",
            "Patchy freezing drizzle nearby": "Freezing Drizzle: Light intensity",
            "Thundery outbreaks in nearby": "Thunderstorm: Slight intensity",
            "Blowing snow": "Snow fall: Slight intensity",
            "Blizzard": "Snow fall: Heavy intensity",
            "Fog": "Fog",
            "Freezing fog": "Depositing rime fog",
            "Patchy light drizzle": "Drizzle: Light intensity",
            "Light drizzle": "Drizzle: Light intensity",
            "Freezing drizzle": "Freezing Drizzle: Light intensity",
            "Heavy freezing drizzle": "Freezing Drizzle: Dense intensity",
            "Patchy light rain": "Rain: Slight intensity",
            "Light rain": "Rain: Slight intensity",
            "Moderate rain at times": "Rain: Moderate intensity",
            "Moderate rain": "Rain: Moderate intensity",
            "Heavy rain at times": "Rain: Heavy intensity",
            "Heavy rain": "Rain: Heavy intensity",
            "Light freezing rain": "Freezing Rain: Light intensity",
            "Moderate or heavy freezing rain": "Freezing Rain: Heavy intensity",
            "Light sleet": "Snow grains",
            "Moderate or heavy sleet": "Snow grains",
            "Patchy light snow": "Snow fall: Slight intensity",
            "Light snow": "Snow fall: Slight intensity",
            "Patchy moderate snow": "Snow fall: Moderate intensity",
            "Moderate snow": "Snow fall: Moderate intensity",
            "Patchy heavy snow": "Snow fall: Heavy intensity",
            "Heavy snow": "Snow fall: Heavy intensity",
            "Ice pellets": "Snow grains",
            "Light rain shower": "Rain showers: Slight intensity",
            "Moderate or heavy rain shower": "Rain showers: Moderate intensity",
            "Torrential rain shower": "Rain showers: Violent intensity",
            "Light sleet showers": "Snow showers: Slight intensity",
            "Moderate or heavy sleet showers": "Snow showers: Heavy intensity",
            "Light snow showers": "Snow showers: Slight intensity",
            "Moderate or heavy snow showers": "Snow showers: Heavy intensity",
            "Light showers of ice pellets": "Snow showers: Slight intensity",
            "Moderate or heavy showers of ice pellets": "Snow showers: Heavy intensity",
            "Patchy light rain in area with thunder": "Thunderstorm: Slight intensity",
            "Moderate or heavy rain in area with thunder": "Thunderstorm with heavy hail",
            "Patchy light snow in area with thunder": "Thunderstorm: Slight intensity",
            "Moderate or heavy snow in area with thunder": "Thunderstorm with heavy hail",
        }
        return contition_text_to_wmo_condition.get(condition, "Unknown")

    async def get_current_weather(self, lat: float, long: float) -> Weather:
        if self.token is None:
            log.error("WeatherAPI token not found")
            raise Unauthorized("WeatherAPI token not found")

        async with AsyncClient() as client:
            response = await client.get(f"{self.base_url}/current.json?key={self.token}&q={lat},{long}")

        response.raise_for_status()
        data = response.json()

        log.info(f"WeatherAPI response: {data}")

        wmo_condition = self._map_condition_text_to_wmo_condition(data["current"]["condition"]["text"])
        wmo_code = self._wmo_condition_to_wmo_weather_code(wmo_condition)

        wind_direction = self._16_point_compass_to_degrees(data["current"]["wind_dir"])

        weather = Weather(
            wmo_code=wmo_code,
            condition=wmo_condition,
            temperature=data["current"]["temp_c"],
            cloud_cover=data["current"]["cloud"],
            precipitation=data["current"]["precip_mm"],
            humidity=data["current"]["humidity"],
            wind_speed=data["current"]["wind_kph"],
            wind_direction=wind_direction,
            timestamp=self._to_iso(data["current"]["last_updated"]),
            latitude=data["location"]["lat"],
            longitude=data["location"]["lon"],
        )

        return weather


_weather_api = _WeatherAPI()
