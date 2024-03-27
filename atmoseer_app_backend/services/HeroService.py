from fastapi import Depends

from atmoseer_app_backend.models.Hero import HeroCreate, HeroOut
from atmoseer_app_backend.repositories import HeroRepository, Repository
from .interfaces.Service import Service

class HeroService(Service):
    def __init__(self, repository: Repository = Depends(HeroRepository)) -> None:
        self.repository = repository

    def get_data(self):
        return self.my_data.get_my_data()
    
    def create(self, hero: HeroCreate) -> HeroOut:
        return self.repository.create(hero)
