FROM python:3.14.0-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-root --no-interaction --no-ansi

COPY ./app /app/app
COPY ./alembic.ini /app/
COPY ./scripts /app/scripts
COPY ./tests /app/tests

ENV PYTHONPATH=/app

CMD ["poetry", "run", "fastapi", "run", "--workers", "4", "app/main.py"]
