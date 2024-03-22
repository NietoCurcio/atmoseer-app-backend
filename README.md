# Atmoseer app backend

## Usage

Clone the repository
```sh
git clone https://github.com/NietoCurcio/atmoseer-app-backend.git
cd atmoseer-app-backend
```

Install [pipenv](https://github.com/pypa/pipenv)
```sh
pip install pipenv
```

Install project dependencies and start the server:
```sh
pipenv install
pipenv run start

# INFO:     Uvicorn running on http://127.0.0.1:3333 (Press CTRL+C to quit)
# ...
# INFO:     Application startup complete.
```

## Project structure

```
atmoseer-app-backend/
├── README.md
├── atmoseer # MLRG-CEFET-RJ/atmoseer submodule
└── app/
    ├── app.py
    ├── config.py
    ├── Logger.py
    └── main.py
    ├── api/
    │   ├── router.py
    │   └── routes/
    │       ├── dogs.py
    │       └── forecast.py
    ├── exceptions/
    │   └── Exceptions.py
    └── services/
        ├── DogsService.py
        ├── ForecastService.py
        └── interfaces/
            └── Service.py
```

The source code of the backend is in the `app` folder. The `atmoseer` folder is a submodule, it has its own git repostiory at [NietoCurcio/atmoseer Github](https://github.com/NietoCurcio/atmoseer). The `atmoseer` submodule is necessary to use the machine learning algorithms developed CEFET-RJ 
Machine Learning Research Group.

- Endpoints

- Services
