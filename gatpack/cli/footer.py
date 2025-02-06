"""CLI command for adding a footer to a PDF."""

from pathlib import Path
from typing import Annotated

from loguru import logger
from rich.console import Console
import typer

from gatpack.core.add_footer_to_pdf import add_footer_to_pdf

console = Console()


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
    text: Annotated[
        str,
        typer.Argument(
            help="Footer text to add to each page of the PDF file. Supports templating.",
        ),
    ],
    output: Annotated[
        Path,
        typer.Argument(
            help="Location to save the new PDF with footer to.",
        ),
    ],
    # **kwargs: Annotated[
    #     dict[str, Any],
    #     typer.Argument(
    #         help="Additional arguments to pass to CookieCutter.",
    #     ),
    # ],
) -> None:
    """Add a footer to every page of a PDF (Currently Not-Implemented)."""
    try:
        logger.info(f"Adding a footer to the PDF document at {file}")
        logger.info(f"And saving to {output}")

        add_footer_to_pdf(file, output, text)

        console.print(f"✨ PDF w/ footer successfully saved to [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed add footer to PDF: {e}")
        raise typer.Exit(1)
