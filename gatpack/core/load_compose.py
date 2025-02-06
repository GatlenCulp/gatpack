"""Loads the GatPack config file for rendering jinja and others."""

from pathlib import Path
from typing import Any
from gatpack.models.GatPackCompose import GatPackCompose


def load_config(
    compose: Path,
    **kwargs: dict[str, Any],
) -> dict[str, Any]:
    """Loads the GatPack config file for rendering jinja and others."""
    gp_compose = GatPackCompose.model_validate_json(compose.read_text())
    return gp_compose
