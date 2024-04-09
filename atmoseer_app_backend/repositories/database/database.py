from collections.abc import Generator

from sqlmodel import Session, create_engine

from atmoseer_app_backend.config import settings

engine = create_engine(str(settings.POSTGRES_URL))


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
