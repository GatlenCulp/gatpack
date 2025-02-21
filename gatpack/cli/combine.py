"""CLI command for combining any number of PDFs into one."""

from loguru import logger
import typer

from gatpack.cli.options import InputGlobsArgument, OutputArgument, OverwriteOption
from gatpack.config import console
from gatpack.core.combine_pdfs import combine_pdfs, resolve_globs


def combine(
    pdfs: InputGlobsArgument,
    output: OutputArgument,
    overwrite: OverwriteOption = False,
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
