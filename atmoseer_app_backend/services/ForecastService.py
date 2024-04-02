from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.helpers.WorkdirManager import workdir_manager, WorkdirManager
from atmoseer_app_backend.helpers.GeoStations import geo_stations, GeoStations

from atmoseer.src.predict_oc import predict_oc

from .interfaces import AtmoseerService
from .exceptions import InternalServerError

log = logger.get_logger(__name__)

class ForecastService(AtmoseerService):
    def __init__(
        self,
        workdir_manager: WorkdirManager,
        geo_stations: GeoStations
    ) -> None:
        self.workdir_manager = workdir_manager
        self.current_workdir = self.workdir_manager.get_current_workdir()

    def get_data(self):
        self.workdir_manager.set_wordkir("atmoseer")
        try:
            pipeline_id = 'A652_A621_A636_A627'
            prediction_task_sufix = "oc"

            log.info(f"""
                Running predict_oc function:
                pipeline_id: {pipeline_id}
                prediction_task_sufix: {prediction_task_sufix}
            """)

            predict_result = predict_oc(
                pipeline_id=pipeline_id,
                prediction_task_sufix=prediction_task_sufix
            )
            return {
                "message": f"Prediction result: {predict_result}"
            }
        except Exception as e:
            built_workdir = self.workdir_manager.build_workdir('atmoseer')
            fn_name = predict_oc.__name__
            message = f"Error running {fn_name} function in {built_workdir}"
            log.error(f"{message}: {e}")
            raise InternalServerError(message=message, error=e)
        finally:
            self.workdir_manager.set_wordkir(str(self.current_workdir))
        
forecast_service = ForecastService(workdir_manager, geo_stations)
