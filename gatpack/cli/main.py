"""CLI entrypoint."""

from __future__ import annotations

from pathlib import Path
from typing import Annotated, Optional

import typer

from gatpack.cli.build import build
from gatpack.cli.combine import combine
from gatpack.cli.compose import compose
from gatpack.cli.examples import examples
from gatpack.cli.footer import footer
from gatpack.cli.infer import infer
from gatpack.cli.init import init
from gatpack.cli.render import render

# Create Typer app instance
app = typer.Typer(
    name="gatpack",
    help="A LaTeX Template to PDF rendering tool.",
    no_args_is_help=True,
)

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


def version_callback(value: bool) -> None:  # noqa: FBT001
    """Print version and exit."""
    if value:
        typer.echo("gatpack version: 0.0.6")
        raise typer.Exit()


VERSION_OPTION = Annotated[
    bool,
    typer.Option(
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
]


@app.callback(invoke_without_command=True)
def root(
    ctx: typer.Context,
    file: FileOption,
    output: OutputOption,
    overwrite: OverwriteOption,
    compose_file: ComposeFileOption,
    version: VERSION_OPTION,
) -> None:
    """Common parameters for all commands."""
    ctx.ensure_object(dict)

    # Store options directly
    ctx.obj["file"] = file
    ctx.obj["output"] = output
    ctx.obj["overwrite"] = overwrite
    ctx.obj["compose_file"] = compose_file

    # If no subcommand and no flags, show help
    if ctx.invoked_subcommand is None and not (file or output):
        typer.echo(ctx.get_help())
        raise typer.Exit

    # If no subcommand but both files are provided
    if ctx.invoked_subcommand is None and file and output:
        ctx.invoke(infer)


app.command()(init)
app.command()(combine)
app.command()(compose)
app.command(hidden=True)(render)
app.command(hidden=True)(build)
app.command()(infer)
app.command(
    hidden=True,  # NotImplemented.
)(footer)
app.command()(examples)

if __name__ == "__main__":
    app()
