from flask_restx import Model, fields

sample_model = Model(
    "Sample",
    {
        "sample": fields.String(
            required=True, description="sample", example="sample"
        ),
    },
)
