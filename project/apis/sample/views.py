from http import HTTPStatus

from flask import request
from flask_restx import Namespace, Resource

from project.apis.sample.models import sample_model
from project.utils.autentication import token_required

sample_namespace = Namespace(
    "Sample", description="Sample CRUD"
)

sample_namespace.add_model("Sample", sample_model)


class SampleClass(Resource):
    @token_required
    @sample_namespace.doc(
        params={
            "Authorization": {
                "in": "header",
                "description": "Authorization token",
                "type": "string",
                "required": True,
            }
        }
    )
    @sample_namespace.expect(sample_model, validate=True)
    @sample_namespace.response(
        code=HTTPStatus.CREATED, description="Sample Data Inserted"
    )
    def post(self):
        try:
            payload = request.get_json()
            response_object = {"status": "success"}
            return response_object, HTTPStatus.CREATED
        except Exception as e:
            sample_namespace.abort(
                HTTPStatus.BAD_REQUEST, message=str(e), status="error"
            )



sample_namespace.add_resource(SampleClass, "")
