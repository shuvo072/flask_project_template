HOST ?= 0.0.0.0
PORT ?= 5000
TAG ?= 0.1
FILES = project manage.py
dev:
	FLASK_ENV=development FLASK_DEBUG=1 poetry run python manage.py run -p $(PORT) -h $(HOST)

celery:
	FLASK_ENV=development FLASK_DEBUG=1 poetry run python manage.py celery_worker

prod:
	gunicorn manage:app -w 4 --log-level INFO --bind $(HOST):$(PORT)

image:
	make lint
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker build -f Dockerfile -t docker_username/<server_name>:$(TAG) . || true
	rm requirements.txt

image-prod:
	make lint
	poetry export -f requirements.txt --output requirements.txt --without-hashes
	docker build -f Dockerfile -t docker_username/<server_name>:$(TAG) . || true
	rm requirements.txt

format:
	@for file in $(FILES); do \
		echo "Formatting $$file"; \
		poetry run black $$file; \
		poetry run isort $$file --profile black; \
	done

lint:
	@for file in $(FILES); do \
		echo "Checking $$file for error"; \
		poetry run flake8 $$file; \
		poetry run black $$file --check --quiet; \
		poetry run isort $$file --profile black --check-only; \
	done

vulnerabilities:
	poetry run bandit -r project
	poetry run safety check --short-report

tox:
	poetry run tox
