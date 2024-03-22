import uvicorn

from app.config import settings

def main():
    uvicorn.run("app.app:app", port=3333, reload=settings.ENV == "dev")

if __name__ == "__main__":
    main()
