"""Loads the GatPack config file for rendering jinja and others."""

from pathlib import Path
from typing import Any

from gatpack.schema.GatPackCompose import GatPackCompose


def load_compose(
    compose: Path,
    **kwargs: dict[str, Any],
) -> GatPackCompose:
    """Loads the GatPack config file for rendering jinja and others."""
    gp_compose = GatPackCompose.model_validate_json(compose.read_text())
    return gp_compose


if __name__ == "__main__":
    print(load_compose(Path("/Users/gat/work/gatpack/tests/compose/compose.gatpack.json")))
