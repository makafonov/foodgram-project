start:
	@poetry run python manage.py runserver

migrate:
	@poetry run python manage.py migrate

setup: migrate
	@poetry run python manage.py createsuperuser
