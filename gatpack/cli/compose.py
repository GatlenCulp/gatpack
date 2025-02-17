"""CLI command for running the pipelines described within a GatPack compose file."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Optional

from loguru import logger
from rich.console import Console
from rich.table import Table
import typer

from gatpack.core.run_pipeline import infer_compose, load_compose, run_pipeline
from gatpack.schema.GatPackCompose import Pipeline


def _print_available_pipelines(pipelines: list[Pipeline]) -> None:
    """Prints all available pipelines in a formatted table."""
    console = Console()
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
    console = Console()

    console.print("\n[bold cyan]Usage:[/bold cyan]")
    console.print("  [green]gatpack compose[/green] [yellow]PIPELINE_ID[/yellow]\n")


def compose(
    pipeline_id: Optional[str] = typer.Argument(
        None,
        help="The pipeline name to run.",
    ),
    compose_file: Optional[Path] = typer.Option(
        None,
        "--compose",
        help="The compose.gatpack.json file to use for templating operations.",
    ),
    overwrite: Annotated[
        bool,
        typer.Option(
            "--overwrite",
            help="Overwrite existing output files if they exist",
        ),
    ] = False,
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
    except Exception as e:
        logger.error(f"Failed to infer and run command: {e}")
        raise typer.Exit(1)
