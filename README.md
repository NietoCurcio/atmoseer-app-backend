# Atmoseer app backend

## Get started

Clone the repository
```sh
git clone https://github.com/NietoCurcio/atmoseer-app-backend.git
cd atmoseer-app-backend
```

Initialize atmoseer project
```sh
git submodule update --init --progress
```

Install [poetry](https://github.com/python-poetry/poetry) dependency manager.
  - Linux and macOS
    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

  - Windows powershell
    ```sh
    (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
    ```

Install project dependencies:
```sh
poetry install

# Creating virtualenv atmoseer-app-backend-...
# Installing dependencies from lock file
# ...
# Installing the current project: atmoseer-app-backend (0.1.0)
```

Start a local instance of PostgreSQL with [Docker](https://hub.docker.com/_/postgres):
```sh
docker compose up
```

Run [alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) database migrations:
```sh
alembic upgrade head

# INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
# INFO  [alembic.runtime.migration] Will assume transactional DDL.
# INFO  [alembic.runtime.migration] Running upgrade  -> 76213b2e56df, create hero table

# to undo all migrations run 'alembic downgrade base'
```

Start the server:
```sh
poetry run start
# INFO:     Uvicorn running on http://127.0.0.1:3333 (Press CTRL+C to quit)
# ...
# INFO:     Application startup complete.
```

Documentation

- Interactive API docs http://localhost:3333/docs
- Alternative API docs http://localhost:3333/redoc

## Project structure

```
atmoseer-app-backend/
├── .env.example
├── .gitmodules
├── alembic.ini
├── docker-compose.yml
├── poetry.lock
├── pyproject.toml
├── README.md
├── atmoseer
└── atmoseer_app_backend
    ├── main.py
    ├── app.py
    ├── config.py
    ├── helpers
    │   ├── Logger.py
    │   └── PathHelper.py
    ├── migrations
    │   └── alembic
    │       ├── env.py
    │       └── versions
    ├── models
    │   └── Hero.py
    ├── repositories
    │   ├── HeroRepository.py
    │   ├── database
    │   │   └── database.py
    │   └── interfaces
    │       └── Repository.py
    ├── services
    │   ├── ForecastService.py
    │   ├── HeroService.py
    │   ├── SomeService.py
    │   ├── exceptions
    │   │   └── exceptions.py
    │   └── interfaces
    │       ├── AtmoseerService.py
    │       └── Service.py
    └── api
        ├── router.py
        └── routes
            ├── forecast.py
            └── heros.py
```

The source code of the backend is in the `atmoseer_app_backend` folder. The `atmoseer` folder is a submodule, it has its own git repostiory at [NietoCurcio/atmoseer Github](https://github.com/NietoCurcio/atmoseer). The `atmoseer` submodule is necessary to use the machine learning algorithms developed by the CEFET-RJ Machine Learning Research Group.

- Endpoints

- Services

## Technologies

### Docker

Removing all containers:
```sh
docker rm -f $(docker ps -a -q)
```

Removing all volumes:
```sh
docker volume rm $(docker volume ls -q)
```