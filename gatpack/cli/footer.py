"""CLI command for adding a footer to a PDF."""

from pathlib import Path
from typing import Annotated

from loguru import logger
import typer

from gatpack.config import console
from gatpack.core.add_footer_to_pdf import add_footer_to_pdf


def footer(
    file: Annotated[
        Path,
        typer.Argument(
            help="PDF file to attach a footer to",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
    output: Annotated[
        Path,
        typer.Argument(
            help="Location to save the new PDF with footer to.",
        ),
    ],
    text: Annotated[
        str,
        typer.Option(
            help=(
                "Footer text to add to each page of the PDF file."
                "Supports Python-string templating."
                "n is current page. N is total number of pages."
            ),
        ),
    ] = "{n} of {N}",
    overwrite: Annotated[bool, typer.Option(help="Whether to overwrite existing file")] = False,
) -> None:
    """Add a footer to every page of a PDF (Currently Not-Implemented)."""
    try:
        logger.info(f"Adding a footer to the PDF document at {file}")
        logger.info(f"And saving to {output}")

        add_footer_to_pdf(file, output, text, overwrite)

        console.print(f"✨ PDF w/ footer successfully saved to [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed add footer to PDF: {e}")
        raise typer.Exit(1)
