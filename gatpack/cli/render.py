"""CLI command for rendering a specific LaTeX document."""

from pathlib import Path
from typing import Annotated

from loguru import logger
import typer

from gatpack.cli.options import ComposeFileOption, OverwriteOption
from gatpack.config import console
from gatpack.core.load_compose import load_compose
from gatpack.core.render_jinja import render_jinja


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
    compose: ComposeFileOption,
    use_standard_jinja: Annotated[
        bool,
        typer.Option(
            help="Whether to use the standard Jinja tags ({{ var }} "
            "{% for item in items %}, etc.)"
            r"instead of custom LaTeX Jinja Tags (\VAR{ var } \BLOCK{}, etc.)",
        ),
    ] = False,
    overwrite: OverwriteOption = False,
) -> None:
    """Render a LaTeX document with Jinja placeholders using provided context. (Replaced w/ `infer`)"""
    try:
        logger.info(f"Rendering template at {template}")
        logger.info(f"And saving to {output}")

        # Define all template variables needed for cover-test.jinja.tex
        gp_compose = load_compose(compose)

        render_jinja(
            template,
            output,
            context=gp_compose.context,
            use_standard_jinja=use_standard_jinja,
            overwrite=overwrite,
        )

        console.print(f"✨ Successfully rendered project in [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed to initialize project: {e}")
        raise typer.Exit(1)
