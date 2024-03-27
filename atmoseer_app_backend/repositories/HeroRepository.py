from fastapi import Depends
from sqlmodel import Session

from atmoseer_app_backend.models.Hero import HeroCreate, HeroOut, Hero
from .interfaces import Repository
from .database import get_session

class HeroRepository(Repository):
    def __init__(self, session: Session = Depends(get_session)) -> None:
        self.session = session

    def create(self, hero: HeroCreate) -> HeroOut:
        db_hero = Hero.model_validate(hero)
        self.session.add(db_hero)
        self.session.commit()
        self.session.refresh(db_hero)
        return db_hero
