"""CLI command for combining any number of PDFs into one."""

from pathlib import Path
from typing import Annotated

from loguru import logger
from rich.console import Console
import typer

from gatpack.core.combine_pdfs import combine_pdfs

console = Console()


def combine(
    pdfs: Annotated[
        list[Path],
        typer.Argument(
            help="Any number of PDFs to combine",
            exists=True,
            file_okay=True,
            dir_okay=False,
        ),
    ],
    output: Annotated[
        Path,
        typer.Argument(
            help="File to save the combined PDF into",
        ),
    ],
    # **kwargs: Annotated[
    #     dict[str, Any],
    #     typer.Argument(
    #         help="Additional arguments to pass to CookieCutter.",
    #     ),
    # ],
) -> None:
    """Initialize a new project with the specified template."""
    try:
        logger.info(f"Merging {len(pdfs)} PDFs")
        logger.info(f"And saving to {output}")

        combine_pdfs(pdfs, output)

        console.print(f"✨ Successfully merged PDFs into [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed to merge pdfs: {e}")
        raise typer.Exit(1)
