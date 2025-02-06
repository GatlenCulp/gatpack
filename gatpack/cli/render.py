"""CLI command for rendering a specific LaTeX document."""

from pathlib import Path
from typing import Annotated

from loguru import logger
from rich.console import Console
import typer

from gatpack.core.render_jinja import render_jinja

console = Console()


def render(
    template: Annotated[
        Path,
        typer.Argument(
            help="Template file to load in",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
    output: Annotated[
        Path | None,
        typer.Argument(
            help="File to save the rendered template into",
        ),
    ],
    context: Annotated[
        str,
        typer.Argument(
            help="Variable assignments to load the template with.",
        ),
    ] = "",
    # **kwargs: Annotated[
    #     dict[str, Any],
    #     typer.Argument(
    #         help="Additional arguments to pass to CookieCutter.",
    #     ),
    # ],
) -> None:
    """Render a specified LaTeX document with Jinja placeholders with provided context."""
    try:
        logger.info(f"Rendering template at {template}")
        logger.info(f"And saving to {output}")

        # Define all template variables needed for cover-test.jinja.tex
        render_context = {
            "program_long_name": "Intro Fellowship",
            "time_period": "Spring 2024",
            "chron_info": "WEEK 5",
            "title": "Model internals",
            "subtitle": "READINGS",
        }

        render_jinja(template, output, context=render_context)

        console.print(f"✨ Successfully rendered project in [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed to initialize project: {e}")
        raise typer.Exit(1)
