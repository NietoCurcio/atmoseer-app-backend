from fastapi import Depends

from atmoseer_app_backend.models.Hero import Hero, HeroCreate
from atmoseer_app_backend.repositories import HeroRepository, Repository

from .exceptions import BadRequest
from .interfaces import Service


class HeroService(Service):
    def __init__(self, repository: Repository = Depends(HeroRepository)) -> None:
        self.repository = repository

    def get_data(self):
        return self.my_data.get_my_data()

    def create(self, hero: HeroCreate) -> Hero:
        return self.repository.create(hero)

    def read_all(self) -> list[Hero]:
        raise BadRequest("Not implemented")
        return self.repository.read_all()
