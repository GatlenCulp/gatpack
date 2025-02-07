"""CLI command for rendering a specific LaTeX document."""

from pathlib import Path
from typing import Annotated

from loguru import logger
from rich.console import Console
import typer

from gatpack.core.build_pdf_from_latex import build_pdf_from_latex

console = Console()


def build(
    file: Annotated[
        Path,
        typer.Argument(
            help="LaTeX file to render to a PDF",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
    output: Annotated[
        Path | None,
        typer.Argument(
            help="File to save the built PDF to",
        ),
    ],
    # **kwargs: Annotated[
    #     dict[str, Any],
    #     typer.Argument(
    #         help="Additional arguments to pass to CookieCutter.",
    #     ),
    # ],
) -> None:
    """Build a LaTeX document into a PDF."""
    try:
        logger.info(f"Building LaTeX document at {file}")
        logger.info(f"And saving to {output}")

        build_pdf_from_latex(file, output)

        console.print(f"✨ Successfully rendered LaTeX into [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed to build LaTeX to PDF: {e}")
        raise typer.Exit(1)
