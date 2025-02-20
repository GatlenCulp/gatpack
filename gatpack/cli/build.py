"""CLI command for rendering a specific LaTeX document."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated

from loguru import logger
import typer

from gatpack.config import console
from gatpack.core.build_pdf_from_latex import build_pdf_from_latex


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
) -> None:
    """Build a LaTeX document into a PDF. (Replaced w/ `infer`)"""
    try:
        logger.info(f"Building LaTeX document at {file}")
        logger.info(f"And saving to {output}")

        build_pdf_from_latex(file, output)

        console.print(f"✨ Successfully rendered LaTeX into [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed to build LaTeX to PDF: {e}")
        raise typer.Exit(1)
