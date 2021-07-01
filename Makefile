.env:
	@test ! -f .env && cp .env.example .env

install: .env
	poetry install --no-dev

lint:
	poetry run flake8 apps

start:
	@poetry run python manage.py runserver

migrate:
	@poetry run python manage.py migrate

setup: migrate
	@poetry run python manage.py createsuperuser

requirements:
	@poetry export -f requirements.txt --output requirements.txt --without-hashes
