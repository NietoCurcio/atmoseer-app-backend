import contextlib

from atmoseer.src.predict_oc import predict_oc

from atmoseer_app_backend.helpers.AsyncExecutor import AsyncExecutor, async_executor
from atmoseer_app_backend.helpers.GeoStations import GeoStations, geo_stations
from atmoseer_app_backend.helpers.Logger import logger

from .exceptions import InternalServerError
from .interfaces import AtmoseerService

log = logger.get_logger(__name__)


class ForecastService(AtmoseerService):
    def __init__(
        self,
        geo_stations: GeoStations,
        async_executor: AsyncExecutor,
    ) -> None:
        self.geo_stations = geo_stations
        self.async_executor = async_executor
        self.rain_mapping = {
            0: "no rain",
            1: "rain",
            2: "heavy rain",
            3: "very heavy rain",
            4: "extreme rain",
        }

    def _get_data(self, latitude: float, longitude: float):
        try:
            prediction_task_sufix = "oc"

            station = self.geo_stations.get_nearest_station(latitude, longitude)

            log.info(f"""
                Nearest station to lat {latitude} long {longitude}:
                name: {station.name}
                situation: {station.situation}
                latitude: {station.latitude}
                longitude: {station.longitude}
                id: {station.station_id}
            """)

            log.info(f"""
                Running predict_oc function:
                pipeline_id: {station.station_id}
                prediction_task_sufix: {prediction_task_sufix}
            """)

            with contextlib.chdir("atmoseer"):
                predict_result = predict_oc(
                    pipeline_id=station.station_id, prediction_task_sufix=prediction_task_sufix
                )

            predict_result = int(predict_result)
            return {
                "atmoseer_result": {
                    "prediction_result": predict_result,
                    "prediction_mapped": self.rain_mapping[predict_result],
                    "station": {
                        "name": station.name,
                        "situation": station.situation,
                        "latitude": station.latitude,
                        "longitude": station.longitude,
                        "id": station.station_id,
                    },
                },
            }
        except Exception as e:
            message = f"Error running {predict_oc.__name__} function"
            log.error(f"{message}: {e}")
            raise InternalServerError(message=message, error=e)

    async def get_data(self, latitude: float, longitude: float):
        return await self.async_executor.execute(
            fn=self._get_data,
            latitude=latitude,
            longitude=longitude,
            executor=self.async_executor.PROCESS,
        )


forecast_service = ForecastService(geo_stations, async_executor)
