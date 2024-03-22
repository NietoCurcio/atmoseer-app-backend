import subprocess
import os

from .interfaces.Service import Service
from app.exceptions.Exceptions import InternalServerError
from app.Logger import logger

log = logger.get_logger(__name__)

class ForecastService(Service):
    def __init__(self) -> None:
        pass

    def _set_atmoseer_working_dir(self, working_dir: str) -> str:
        current_workdir = os.getcwd()
        os.chdir(working_dir)
        return current_workdir

    def get_data(self):
        script_path = "src/predict_oc.py"
        try:
            current_workdir = self._set_atmoseer_working_dir('atmoseer')
            process = subprocess.run(
                ["python", script_path],
                check=True,
                stdout=subprocess.PIPE, text=True
            )
            log.info(f"Output of {script_path}:\n{process.stdout}")
            self._set_atmoseer_working_dir(current_workdir)
        except subprocess.CalledProcessError as e:
            message = f"Error running the {script_path} script"
            log.error(f"{message}: {e}")
            raise InternalServerError(message=message, error=e)

forecast_service = ForecastService()
