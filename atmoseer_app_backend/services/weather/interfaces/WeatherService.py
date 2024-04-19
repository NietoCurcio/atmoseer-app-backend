from abc import ABC, abstractmethod

from ..models import Weather


class WeatherService(ABC):
    @abstractmethod
    def get_service_name(self) -> str:
        pass

    @abstractmethod
    async def get_current_weather(self, lat: float, long: float) -> Weather:
        pass

    def _wmo_weather_code_to_wmo_condition(self, code: int) -> str:
        """
        https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM
        https://open-meteo.com/en/docs
        """
        wmo_code_to_weather_conditions = {
            0: "Clear sky",
            1: "Mainly clear",
            2: "Partly cloudy",
            3: "Overcast",
            45: "Fog",
            48: "Depositing rime fog",
            51: "Drizzle: Light intensity",
            53: "Drizzle: Moderate intensity",
            55: "Drizzle: Dense intensity",
            56: "Freezing Drizzle: Light intensity",
            57: "Freezing Drizzle: Dense intensity",
            61: "Rain: Slight intensity",
            63: "Rain: Moderate intensity",
            65: "Rain: Heavy intensity",
            66: "Freezing Rain: Light intensity",
            67: "Freezing Rain: Heavy intensity",
            71: "Snow fall: Slight intensity",
            73: "Snow fall: Moderate intensity",
            75: "Snow fall: Heavy intensity",
            77: "Snow grains",
            80: "Rain showers: Slight intensity",
            81: "Rain showers: Moderate intensity",
            82: "Rain showers: Violent intensity",
            85: "Snow showers: Slight intensity",
            86: "Snow showers: Heavy intensity",
            95: "Thunderstorm: Slight intensity",
            96: "Thunderstorm with slight hail",
            99: "Thunderstorm with heavy hail",
        }
        return wmo_code_to_weather_conditions.get(code, "Unknown")

    def _wmo_condition_to_wmo_weather_code(self, condition: str) -> int:
        """
        https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM
        https://open-meteo.com/en/docs
        """
        wmo_weather_conditions_to_code = {
            "Clear sky": 0,
            "Mainly clear": 1,
            "Partly cloudy": 2,
            "Overcast": 3,
            "Fog": 45,
            "Depositing rime fog": 48,
            "Drizzle: Light intensity": 51,
            "Drizzle: Moderate intensity": 53,
            "Drizzle: Dense intensity": 55,
            "Freezing Drizzle: Light intensity": 56,
            "Freezing Drizzle: Dense intensity": 57,
            "Rain: Slight intensity": 61,
            "Rain: Moderate intensity": 63,
            "Rain: Heavy intensity": 65,
            "Freezing Rain: Light intensity": 66,
            "Freezing Rain: Heavy intensity": 67,
            "Snow fall: Slight intensity": 71,
            "Snow fall: Moderate intensity": 73,
            "Snow fall: Heavy intensity": 75,
            "Snow grains": 77,
            "Rain showers: Slight intensity": 80,
            "Rain showers: Moderate intensity": 81,
            "Rain showers: Violent intensity": 82,
            "Snow showers: Slight intensity": 85,
            "Snow showers: Heavy intensity": 86,
            "Thunderstorm: Slight intensity": 95,
            "Thunderstorm with slight hail": 96,
            "Thunderstorm with heavy hail": 99,
        }
        return wmo_weather_conditions_to_code.get(condition, -1)
