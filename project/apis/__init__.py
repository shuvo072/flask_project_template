from flask_restx import Api

from project.apis.alive.api import alive_namespace
from project.apis.sample.views import sample_namespace

api = Api(
    version="1.0",
    title="Sample Flask Backend",
    prefix="/api/sample/v1",
    doc="/docs",
)

api.add_namespace(alive_namespace, path="/alive")
api.add_namespace(sample_namespace, path="/sample")
