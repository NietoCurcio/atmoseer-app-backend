import uvicorn

from atmoseer_app_backend.config import settings


def main():
    uvicorn.run("atmoseer_app_backend.app:app", port=3333, reload=settings.ENV == "dev")


if __name__ == "__main__":
    main()
