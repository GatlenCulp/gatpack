"""CLI command for project initialization."""

from pathlib import Path
from typing import Annotated

from loguru import logger
from rich.console import Console
import typer

from gatpack.core.initialize_project import initialize_project

console = Console()


def init(
    output_dir: Annotated[
        Path | None,
        typer.Argument(
            help="Directory to initialize the project in",
            exists=False,
            file_okay=False,
            dir_okay=True,
            writable=True,
        ),
    ] = None,
    template: Annotated[
        str,
        typer.Option(
            "--template",
            "-t",
            help="Template to use for initialization",
        ),
    ] = "default",
    # **kwargs: Annotated[
    #     dict[str, Any],
    #     typer.Argument(
    #         help="Additional arguments to pass to CookieCutter.",
    #     ),
    # ],
) -> None:
    """Initialize a new project with the specified template."""
    output_dir = Path.cwd() if output_dir is None else output_dir

    try:
        logger.info(f"Initializing new project in {output_dir}")
        logger.info(f"Using template: {template}")

        initialize_project(output_dir, template)  # **kwargs)

        console.print(f"✨ Successfully initialized project in [bold green]{output_dir}[/]")

    except Exception as e:
        logger.error(f"Failed to initialize project: {e}")
        raise typer.Exit(1)
