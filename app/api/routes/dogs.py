
from fastapi import APIRouter

from app.Logger import logger
from app.services import dogs_service

log = logger.get_logger(__name__)

router = APIRouter()

@router.get("/")
async def read_dogs():
    log.info("Getting dogs data")
    return dogs_service.get_data()
