from .interfaces.AtmoseerService import AtmoseerService

from atmoseer_app_backend.helpers.Logger import logger
from atmoseer.src.predict_oc import predict_oc

from .exceptions.Exceptions import InternalServerError

log = logger.get_logger(__name__)

class ForecastService(AtmoseerService):
    def __init__(self) -> None:
        super().__init__()
        self.current_workdir = self.path_helper.get_current_workdir()

    def get_data(self):
        self.path_helper.set_wordkir("atmoseer")
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
            built_workdir = self.path_helper.build_workdir('atmoseer')
            fn_name = predict_oc.__name__
            message = f"Error running {fn_name} function in {built_workdir}"
            log.error(f"{message}: {e}")
            raise InternalServerError(message=message, error=e)
        finally:
            self.path_helper.set_wordkir(str(self.current_workdir))
        
forecast_service = ForecastService()
