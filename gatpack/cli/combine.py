"""CLI command for combining any number of PDFs into one."""

from pathlib import Path
from typing import Annotated

from loguru import logger
from rich.console import Console
import typer

from gatpack.core.combine_pdfs import combine_pdfs, resolve_globs

console = Console()


def combine(
    pdfs: Annotated[
        list[str],  # Handle strings manually as globs
        typer.Argument(
            help="Any number of PDFs to combine. Globs accepted",
            # exists=True,
            # file_okay=True,
            # dir_okay=False,
        ),
    ],
    output: Annotated[
        Path,
        typer.Argument(
            help="File to save the combined PDF into",
        ),
    ],
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite",
            help="Overwrite existing output files if they exist",
        ),
    ] = False,
    # **kwargs: Annotated[
    #     dict[str, Any],
    #     typer.Argument(
    #         help="Additional arguments to pass to CookieCutter.",
    #     ),
    # ],
) -> None:
    """Combine any number of PDFs into a single PDF."""
    try:
        resolved_pdfs = resolve_globs(pdfs)
        logger.info(f"Merging {len(resolved_pdfs)} PDFs")
        logger.info(f"And saving to {output}")

        combine_pdfs(resolved_pdfs, output, overwrite=overwrite)

        console.print(f"✨ Successfully merged PDFs into [bold green]{output}[/]")

    except Exception as e:
        logger.error(f"Failed to merge pdfs: {e}")
        raise typer.Exit(1)
