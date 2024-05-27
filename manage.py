import logging

import yaml
from flask.cli import FlaskGroup

from project import create_app, ext_celery

app = create_app()
cli = FlaskGroup(create_app=create_app)
celery = ext_celery.celery

app.logger.setLevel(logging.INFO)


@cli.command("celery_worker")
def celery_worker():
    import subprocess

    subprocess.call(["python", "run_celery_worker.py"])


@cli.command(
    "generate-schema",
)
def generate_schema():
    """Generates Openapi Schema for Restx Application"""
    import requests

    client = app.test_client()
    schema = client.get("/swagger.json")
    data = schema.json
    data["schemes"] = ["https"]
    data["host"] = "{base_url}"
    resp = requests.post("https://converter.swagger.io/api/convert", json=data)
    print(yaml.safe_dump(resp.json())[:-1])


if __name__ == "__main__":
    cli()

# python manage.py generate-schema > docs/api/openapi.yaml
# poetry add openapi-spec-validator
# openapi-spec-validator docs/api/openapi.yaml
