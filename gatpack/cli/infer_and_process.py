"""CLI command at root, inferring the file formats from the file type and performing the needed operation."""

from pathlib import Path
from typing import Annotated

from loguru import logger
from rich.console import Console
import typer

from gatpack.core.build_pdf_from_latex import build_pdf_from_latex

console = Console()


def infer(
    # Note: This should probably be a list of strings like the other was for globbing.
    file: Annotated[
        Path,
        typer.Argument(
            help="Incoming file to be processed.",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
    output: Annotated[
        Path | None,
        typer.Argument(help="Where to save the resulting files"),
    ],
) -> None:
    """CLI command at root, inferring the file formats from the file type and performing the needed operation."""
    try:
        logger.info(f"Inferring needed operation and processing file at {file}")
        logger.info(f"And saving to {output}")

        breakpoint()
        build_pdf_from_latex(file, output)

        console.print(f"✨ Successfully rendered LaTeX into [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed to build LaTeX to PDF: {e}")
        raise typer.Exit(1)
