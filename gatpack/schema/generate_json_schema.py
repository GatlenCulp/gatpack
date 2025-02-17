"""Export GatPackCompose into a JSON Schema for validation and intellisense."""

from pathlib import Path

import orjson

from gatpack.schema.GatPackCompose import GatPackCompose

# TODO(Gatlen): Come back to this


def generate_json_schema(
    output_file: Path = Path("./gatpack/schema/json/GatPackCompose.schema.json"),
) -> None:
    """Export GatPackCompose into a JSON schema for validation and intellisense.

    Args:
        output_file: Path to write the JSON schema file to.
    """
    json_schema = GatPackCompose.model_json_schema()
    # Create parent directories if they don't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    # Write the schema to file
    output_file.write_bytes(orjson.dumps(json_schema, option=orjson.OPT_INDENT_2))
    print(f"Successfully wrote JSON schema to: {output_file}")


if __name__ == "__main__":
    generate_json_schema()
