"""Loads the GatPack config file for rendering jinja and others."""

from pathlib import Path
from typing import Any


def load_config(
    config: Path,
    **kwargs: dict[str, Any],
) -> dict[str, Any]:
    """Loads the GatPack config file for rendering jinja and others."""
