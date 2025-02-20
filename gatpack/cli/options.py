"""Typer CLI options to import and reuse across project."""

from pathlib import Path
from typing import Annotated, Optional

import typer

from gatpack.config import VERSION


def version() -> None:
    """Print version and exit."""
    typer.echo(f"gatpack version: {VERSION}")


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
    Optional[Path],
    typer.Option(
        "--compose",
        help="The gatpack compose file to use for templating operations.",
        show_default="./*gatpack.json",
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=True,
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
        file_okay=True,
        dir_okay=False,
        writable=True,
    ),
]

OutputArgument = Annotated[
    Path,
    typer.Argument(
        help="Output file path",
        file_okay=True,
        dir_okay=False,
        writable=True,
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

InputGlobsArgument = Annotated[
    list[str],
    typer.Argument(
        help="Any squence of files or globs",
    ),
]

OutputDirArgument = Annotated[
    Optional[Path],
    typer.Argument(
        help="Directory to initialize the project in",
        exists=False,
        file_okay=False,
        dir_okay=True,
        writable=True,
    ),
]

TemplateOption = Annotated[
    str,
    typer.Option(
        "--template",
        "-t",
        help="Template to use for initialization",
    ),
]
