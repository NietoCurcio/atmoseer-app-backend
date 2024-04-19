from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.services.exceptions import BadRequest

from ._ClimaTempo import _clima_tempo
from ._OpenMeteo import _open_meteo
from ._OpenWeatherMap import _open_weather_map
from ._WeatherAPI import _weather_api
from .interfaces import WeatherService
from .models.Weather import Weather

log = logger.get_logger(__name__)


class Weather:
    def __init__(
        self,
        _open_meteo: WeatherService,
        _clima_tempo: WeatherService,
        _weather_api: WeatherService,
        _open_weather_map: WeatherService,
    ) -> None:
        self.services = {
            service.get_service_name(): service
            for service in [_open_meteo, _clima_tempo, _weather_api, _open_weather_map]
        }
        self.default_service = _open_meteo

    def get_default_service_name(self) -> str:
        return self.default_service.get_service_name()

    def get_service_names(self) -> list[str]:
        return [service.get_service_name() for service in self.services.values()]

    async def get_current_weather(self, lat: float, long: float, service: str) -> Weather:
        try:
            if service not in self.get_service_names():
                raise BadRequest(f"Service {service} not found")

            selected_service = self.services.get(service)

            return await selected_service.get_current_weather(lat, long)
        except Exception as e:
            log.error(f"Error getting current weather from {selected_service.get_service_name()}: {e}")
            raise e


weather_service = Weather(
    _open_meteo=_open_meteo,
    _clima_tempo=_clima_tempo,
    _weather_api=_weather_api,
    _open_weather_map=_open_weather_map,
)
