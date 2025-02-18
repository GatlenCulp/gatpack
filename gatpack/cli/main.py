"""CLI entrypoint."""

from __future__ import annotations

import typer

from gatpack.cli.build import build
from gatpack.cli.combine import combine
from gatpack.cli.compose import compose
from gatpack.cli.examples import examples
from gatpack.cli.footer import footer
from gatpack.cli.infer import infer
from gatpack.cli.init import init
from gatpack.cli.options import (
    ComposeFileOption,
    FileOption,
    OutputOption,
    OverwriteOption,
    VersionOption,
)
from gatpack.cli.render import render

# Create Typer app instance
app = typer.Typer(
    name="gatpack",
    help="A LaTeX Template to PDF rendering tool.",
    no_args_is_help=True,
)


@app.callback(invoke_without_command=True)
def root(
    ctx: typer.Context,
    file: FileOption,
    output: OutputOption,
    overwrite: OverwriteOption,
    compose_file: ComposeFileOption,
    version: VersionOption = False,
) -> None:
    """Common parameters for all commands."""
    ctx.ensure_object(dict)

    # Store options directly
    ctx.obj["file"] = file
    ctx.obj["output"] = output
    ctx.obj["overwrite"] = overwrite
    ctx.obj["compose_file"] = compose_file

    # If no subcommand but both files are provided
    if ctx.invoked_subcommand is None and file and output:
        ctx.invoke(infer)


app.command()(init)
app.command()(combine)
app.command()(compose)
app.command(
    name="infer",
    help="Infers and run needed operations to transform one file format to another.",
    short_help="Automatically transform one file format to another.",
)(infer)
app.command(hidden=True)(render)
app.command(hidden=True)(build)
app.command(
    hidden=True,  # NotImplemented.
)(footer)
app.command()(examples)

if __name__ == "__main__":
    app()
