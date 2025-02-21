"""Core functionality for project initialization."""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, Literal, Optional

from cookiecutter.main import cookiecutter

TemplateType = Literal["default"]  # Add more template types as needed
TEMPLATE_URLS = {
    "default": "https://github.com/GatlenCulp/cookiecutter-gatpack.git",
}


def initialize_project(
    output_dir: Path,
    template: TemplateType = "default",
    checkout: Optional[str] = None,
    **kwargs: Dict[str, Any],
) -> None:
    """Initialize a new project using cookiecutter.

    Args:
        output_dir: Directory where the project should be initialized
        template: Template type to use for initialization
        force: Whether to force initialization in non-empty directory
    """
    if template not in TEMPLATE_URLS:
        err_msg = f"Unknown template: {template}"
        raise ValueError(err_msg)

    if checkout:
        cookiecutter(TEMPLATE_URLS[template], output_dir=output_dir, checkout=checkout, **kwargs)
        return
    cookiecutter(TEMPLATE_URLS[template], output_dir=output_dir, **kwargs)
