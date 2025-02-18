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
    file: FileOption = None,
    output: OutputOption = None,
    compose_file: ComposeFileOption = None,
    overwrite: OverwriteOption = False,
    version: VersionOption = False,
) -> None:
    """Establish infer as the root command."""
    # If no subcommand but both files are provided
    if ctx.invoked_subcommand is None and file and output:
        ctx.invoke(infer)


app.command(
    name="init",
    help="Use CookieCutter to initialize a new GatPack project in your specified directory.",
    short_help="Initialize a new GatPack project in your specified directory.",
)(init)

app.command(
    name="combine",
    help="Combine PDFs (files or globs) and save them to the specified output file.",
    short_help="Combine PDFs into a single file.",
)(combine)

app.command(
    name="compose",
    help="Run the specified pipleine ID as defined in the GatPack compose file.",
    short_help="Run the specified pipleine ID from the compose file.",
)(compose)

app.command(
    name="infer",
    help="Infers and run needed operations to transform one file format to another.",
    short_help="Automatically transform one file format to another.",
)(infer)

app.command(
    name="show-examples",
    help="Show examples GatPack's common uses.",
    short_help="Show examples GatPack's common uses.",
)(examples)

app.command(hidden=True)(render)
app.command(hidden=True)(build)
app.command(hidden=True)(footer)  # NotImplemented.


if __name__ == "__main__":
    app()
