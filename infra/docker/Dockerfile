FROM python:3.8.11-slim-buster

ENV POETRY_VIRTUALENVS_CREATE=false \
  # do not ask any interactive question
  POETRY_NO_INTERACTION=1 \
  # prevents python creating .pyc files
  PYTHONDONTWRITEBYTECODE=1 \
  PATH="$PATH:/root/.poetry/bin"

RUN apt-get update && apt-get upgrade -y \
  && apt-get install --no-install-recommends -y \
    curl \
  && curl -sSL 'https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py' | python \
  && poetry --version \
  # Cleaning cache:
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && apt-get clean -y && rm -rf /var/lib/apt/lists/*

WORKDIR /code

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip
RUN poetry install --no-dev

COPY ./infra/docker/entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

COPY . .
ENTRYPOINT ["/docker-entrypoint.sh"]
