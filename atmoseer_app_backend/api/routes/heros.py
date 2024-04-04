from fastapi import APIRouter, Depends

from atmoseer_app_backend.helpers.Logger import logger
from atmoseer_app_backend.services.interfaces import Service
from atmoseer_app_backend.services.HeroService import HeroService
from atmoseer_app_backend.models.Hero import HeroCreate, HeroOut

router = APIRouter()

@router.get("/")
async def read_heros(hero_service: HeroService = Depends(HeroService)):
    logger.info("Getting heros data")
    return hero_service.read_all()

@router.post("/") 
async def create_hero(hero: HeroCreate, hero_service: HeroService = Depends(HeroService)) -> HeroOut:
    # TODO use Service interface instead of HeroService as type, improve services and repos interfaces
    logger.info("Creating hero")
    return hero_service.create(hero)

