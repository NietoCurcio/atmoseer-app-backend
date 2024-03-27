from sqlmodel import SQLModel, Field

class HeroBase(SQLModel):
    name: str
    secret_name: str
    age: int | None = None

class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: int | None = None

class HeroCreate(HeroBase):
    pass

class HeroOut(HeroBase):
    id: int
