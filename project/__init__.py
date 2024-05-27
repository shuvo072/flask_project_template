import os

from flask import Flask
from flask_celeryext import FlaskCeleryExt
from flask_cors import CORS
from flask_migrate import Migrate
from flask_pymongo import PyMongo
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy

from project.utils.celery_utils import make_celery

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
pymongo_client = PyMongo()
ext_celery = FlaskCeleryExt(create_celery_app=make_celery)
redis_client = FlaskRedis()


def create_app():
    app = Flask(__name__)
    with app.app_context():
        app_settings = os.environ.get(
            "APP_SETTINGS", "project.config.DevelopmentConfig"
        )
        app.config.from_object(app_settings)
        cors.init_app(app)
        db.init_app(app)
        migrate.init_app(app, db)
        pymongo_client.init_app(app)
        ext_celery.init_app(app)
        redis_client.init_app(app)

        from project.apis import api

        api.init_app(app)

        @app.shell_context_processor
        def ctx():  # pragma: no cover
            return {"app": app, "db": db}

    return app
