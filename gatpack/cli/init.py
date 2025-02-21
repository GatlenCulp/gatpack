"""CLI command for project initialization."""

from pathlib import Path

from loguru import logger
import typer

from gatpack.cli.options import OutputDirArgument, TemplateOption
from gatpack.config import console
from gatpack.core.initialize_project import initialize_project


def init(
    output_dir: OutputDirArgument = None,
    template: TemplateOption = "default",
) -> None:
    """Initialize a new GatPack project in your specified directory."""
    output_dir = Path.cwd() if output_dir is None else output_dir

    try:
        logger.info(f"Initializing new project in {output_dir}")
        logger.info(f"Using template: {template}")

        initialize_project(output_dir, template)

        console.print(f"✨ Successfully initialized project in [bold green]{output_dir}[/]")

    except Exception as e:
        logger.error(f"Failed to initialize project: {e}")
        raise typer.Exit(1)
