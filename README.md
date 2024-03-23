# Atmoseer app backend

## Get started

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

Documentation

- Interactive API docs http://localhost:3333/docs
- Alternative API docs http://localhost:3333/redoc

## Project structure

```
atmoseer-app-backend/
├── .env.example
├── .gitmodules
├── README.md
└── app/
    ├── app.py
    ├── config.py
    ├── main.py
    ├── api/
    │   ├── router.py
    │   └── routes/
    │       ├── dogs.py
    │       └── forecast.py
    ├── exceptions/
    │   └── Exceptions.py
    ├── helpers/
    │   ├── Logger.py
    │   └── PathHelper.py
    └── services/
        ├── DogsService.py
        ├── ForecastService.py
        └── interfaces/
            ├── AtmoseerService.py
            └── Service.py
```

The source code of the backend is in the `app` folder. The `atmoseer` folder is a submodule, it has its own git repostiory at [NietoCurcio/atmoseer Github](https://github.com/NietoCurcio/atmoseer). The `atmoseer` submodule is necessary to use the machine learning algorithms developed by the CEFET-RJ Machine Learning Research Group.

- Endpoints

- Services
