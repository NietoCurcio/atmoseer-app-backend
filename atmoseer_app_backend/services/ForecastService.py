from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.helpers.WorkdirManager import workdir_manager, WorkdirManager
from atmoseer_app_backend.helpers.GeoStations import geo_stations, GeoStations
from atmoseer_app_backend.helpers.AsyncExecutor import async_executor, AsyncExecutor

from atmoseer.src.predict_oc import predict_oc

from .interfaces import AtmoseerService
from .exceptions import InternalServerError

log = logger.get_logger(__name__)

class ForecastService(AtmoseerService):
    def __init__(
        self,
        workdir_manager: WorkdirManager,
        geo_stations: GeoStations,
        async_executor: AsyncExecutor
    ) -> None:
        self.workdir_manager = workdir_manager
        self.geo_stations = geo_stations
        self.async_executor = async_executor
        self.current_workdir = self.workdir_manager.get_current_workdir()

    async def get_data(self, latitude: float, longitude: float):
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

            self.workdir_manager.set_wordkir("atmoseer")

            predict_result = await async_executor.execute(
                predict_oc,
                pipeline_id=station.station_id,
                prediction_task_sufix=prediction_task_sufix
            )
            return {
                "message": f"Prediction result: {predict_result}"
            }
        except Exception as e:
            workdir = self.workdir_manager.get_current_workdir()
            fn_name = predict_oc.__name__
            message = f"Error running {fn_name} function in {workdir}"
            log.error(f"{message}: {e}")
            raise InternalServerError(message=message, error=e)
        finally:
            self.workdir_manager.set_wordkir(str(self.current_workdir))
        
forecast_service = ForecastService(workdir_manager, geo_stations, async_executor)
