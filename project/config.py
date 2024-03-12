import os


class BaseConfig:
    DEPLOYMENT_ENVIRONMENT = os.environ.get("DEPLOYMENT_ENVIRONMENT", "staging")
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "my_precious")
    RESTX_ERROR_404_HELP = False
    X_API_KEY = os.environ.get("X_API_KEY", "my_precious_api_key")


class DevelopmentConfig(BaseConfig):
    FLASK_ENV = "development"
    MONGO_URI = os.environ.get(
        "MONGO_DATABASE_URL",
        "mongodb://admin:shuvo72@localhost:27321/sms-firewall?authSource=admin",
    )
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", "postgresql://admin:shuvo72@localhost:5432/shuvo_db"
    )
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    TESTING = True
    MONGO_URI = os.environ.get(
        "MONGO_TEST_DATABASE_URL",
        "mongodb://admin:shuvo72@localhost:27123/sms-firewall-test?authSource=admin",
    )
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_TEST_URL",
        "postgresql://admin:shuvo72@localhost:5432/shuvo_test_db",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    FLASK_ENV = "production"
    RESTX_ERROR_404_HELP = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    MONGO_URI = os.environ.get("MONGO_DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY", "my_precious")
