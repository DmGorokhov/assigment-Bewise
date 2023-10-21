run-celery:
	 celery -A R4C worker --loglevel=info & celery -A R4C flower

migrations:
	 docker exec -it app alembic revision --autogenerate

build:
	docker compose build

start-dev:
	docker compose up

start-server:
	poetry run uvicorn src.main:app --reload

lint:
		poetry run flake8 .

