"""CLI command at root, inferring the file formats from the file type and performing the needed operation."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Optional

from loguru import logger
import typer

from gatpack.cli.error_handling import handle_gatpack_error
from gatpack.cli.options import ComposeFileOption, OverwriteOption
from gatpack.config import console
from gatpack.core.exceptions import GatPackError
from gatpack.core.infer_and_run_command import infer_and_run_command


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
        Optional[Path],
        typer.Argument(help="Where to save the resulting files"),
    ],
    compose_file: ComposeFileOption = None,
    overwrite: OverwriteOption = False,
) -> None:
    """[DEFAULT] Infers file formats from the file type and performs the needed operations."""
    try:
        logger.info(f"Inferring needed operation and processing file at {file}")
        logger.info(f"And saving to {output}")

        if output and output.exists() and not overwrite:
            console.print(
                f"[bold red]Error:[/] Output path {output} already exists. Use --overwrite to force."
            )
            raise typer.Exit(1)

        infer_and_run_command(file, output, overwrite=overwrite, compose_file=compose_file)
        console.print(
            f"\n✨ [bold green]Successfully processed[/] [cyan]{file}[/] → [cyan]{output}[/]"
        )
    except GatPackError as e:
        handle_gatpack_error(e)
        raise typer.Exit(1)
    except Exception as e:
        # Handle unexpected errors
        console.print(f"\n[bold red]Unexpected Error:[/] {e!s}\n")
        logger.exception("Unexpected error occurred")
        raise typer.Exit(1)
