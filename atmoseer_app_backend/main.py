import uvicorn
import sys
from pathlib import Path

def main():
    uvicorn.run("atmoseer_app_backend.app:app", port=3333, reload=True)

if __name__ == "__main__":
    main()
