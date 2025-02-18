from pathlib import Path
from typing import Annotated

import typer

from gatpack.config import VERSION


def version_callback(value: bool) -> None:  # noqa: FBT001
    """Print version and exit."""
    if value:
        typer.echo(f"gatpack version: {VERSION}")
        raise typer.Exit


# Define type aliases for common options
OverwriteOption = Annotated[
    bool,
    typer.Option(
        "--overwrite",
        help="Whether to overwrite output files if they already exist",
    ),
]

ComposeFileOption = Annotated[
    Path,
    typer.Option(
        "--compose",
        help="The compose.gatpack.json file to use for templating operations.",
    ),
]

# Input/Output specific options
FileOption = Annotated[
    Path,
    typer.Option(
        "--from",
        "-f",
        help="Input file path",
    ),
]

OutputOption = Annotated[
    Path,
    typer.Option(
        "--to",
        "-t",
        help="Output file path",
    ),
]

VersionOption = Annotated[
    bool,
    typer.Option(
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
]

InputGlobsOption = Annotated[
    list[str],
    typer.Argument(
        help="Any number of files. Globs accepted",
    ),
]
