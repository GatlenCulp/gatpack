from gatpack.schema.GatPackCompose import GatPackCompose
import orjson

# TODO: Come back to this


def generate_json_schema():
    schema_json = orjson.dumps(GatPackCompose.model_json_schema())
