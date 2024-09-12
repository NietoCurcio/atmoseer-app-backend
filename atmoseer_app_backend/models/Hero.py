from sqlmodel import Field, SQLModel
from typing import Union


class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: Union[int, None] = None


class Hero(HeroBase, table=True):
    id: Union[int, None] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Union[int, None] = None


class HeroCreate(HeroBase):
    pass


class HeroOut(HeroBase):
    id: int
