install:
	 poetry install

migrations:
	 docker exec -it app alembic revision --autogenerate

build:
	docker compose build

setup: install build

start-dev:
	docker compose up

start-server:
	poetry run uvicorn src.main:app --reload


test:
	poetry run pytest

lint:
	poetry run flake8 .

