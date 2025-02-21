"""CLI command for running the pipelines described within a GatPack compose file."""

from __future__ import annotations

from typing import Annotated, Optional

from loguru import logger
from rich.table import Table
import typer

from gatpack.cli.error_handling import handle_gatpack_error
from gatpack.cli.options import ComposeFileOption, OverwriteOption
from gatpack.config import console
from gatpack.core.exceptions import GatPackError
from gatpack.core.run_pipeline import infer_compose, load_compose, run_pipeline
from gatpack.schema.GatPackCompose import Pipeline


def _print_available_pipelines(pipelines: list[Pipeline]) -> None:
    """Prints all available pipelines in a formatted table."""
    table = Table(title=f"Available Pipelines ({len(pipelines)})")

    table.add_column("ID", style="cyan", no_wrap=True)
    table.add_column("Description", style="green")
    table.add_column("# of Steps", style="magenta", justify="right")

    for pipeline in pipelines:
        table.add_row(
            pipeline.id,
            pipeline.description,
            str(len(pipeline.steps)),
        )

    console.print(table)


def _print_usage() -> None:
    """Prints usage information for the gatpack compose command."""
    console.print("\n[bold cyan]Usage:[/bold cyan]")
    console.print("  [green]gatpack compose[/green] [yellow]PIPELINE_ID[/yellow]\n")


PipelineIdArgument = Annotated[
    Optional[str],
    typer.Argument(
        help="The pipeline name to run.",
    ),
]


def compose(
    pipeline_id: PipelineIdArgument = None,
    compose_file: ComposeFileOption = None,
    overwrite: OverwriteOption = False,
) -> None:
    """Runs the specified pipleine id from the compose file."""
    try:
        if not pipeline_id:
            _print_usage()
            compose = load_compose(compose_file) if compose_file else infer_compose()
            _print_available_pipelines(compose.pipelines)
            return
        logger.info(f"Running pipeline {pipeline_id}")
        run_pipeline(pipeline_id, compose_file=compose_file, overwrite=overwrite)
    except GatPackError as e:
        handle_gatpack_error(e)
        raise typer.Exit(1)
    except Exception as e:
        # Handle unexpected errors
        console.print(f"\n[bold red]Unexpected Error:[/] {str(e)}\n")
        logger.exception("Unexpected error occurred")
        raise typer.Exit(1)
