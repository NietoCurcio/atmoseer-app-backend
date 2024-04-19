from fastapi import APIRouter, Depends

from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.models.Hero import HeroCreate, HeroOut
from atmoseer_app_backend.services.HeroService import HeroService

log = logger.get_logger(__name__)

router = APIRouter()


@router.get("/")
async def read_heros(hero_service: HeroService = Depends(HeroService)):
    log.info("Getting heros data")
    return hero_service.read_all()


@router.post("/")
async def create_hero(hero: HeroCreate, hero_service: HeroService = Depends(HeroService)) -> HeroOut:
    # TODO use Service interface instead of HeroService as type, improve services and repos interfaces
    log.info("Creating hero")
    return hero_service.create(hero)
