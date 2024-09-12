FROM python:3.12

# Instalação do Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app
COPY . .
RUN poetry install

CMD ["poetry", "run", "start"]