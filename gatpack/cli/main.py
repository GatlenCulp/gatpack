"""CLI entrypoint."""

from __future__ import annotations

from typing import Optional

import typer

from gatpack.cli.build import build
from gatpack.cli.combine import combine
from gatpack.cli.footer import footer
from gatpack.cli.init import init
from gatpack.cli.render import render
from gatpack.cli.infer import infer

# Create Typer app instance
app = typer.Typer(
    name="gatpack",
    help="A PDF and website templating tool",
    add_completion=True,
    no_args_is_help=True,
)


def version_callback(value: bool) -> None:  # noqa: FBT001
    """Print version and exit."""
    if value:
        typer.echo("gatpack version: 0.0.6")
        raise typer.Exit


@app.callback(invoke_without_command=True)
def root(
    ctx: typer.Context,
    from_file: Optional[str] = typer.Option(
        None,
        "--from",
        "-f",
        help="Input file path",
    ),
    to_output: Optional[str] = typer.Option(
        None,
        "--output",
        "-o",
        help="Output file path",
    ),
    version: Optional[bool] = typer.Option(  # noqa: ARG001
        None,
        "--version",
        "-v",
        callback=version_callback,
        is_eager=True,
        help="Show version and exit",
    ),
) -> None:
    """Common parameters for all commands."""
    ctx.ensure_object(dict)
    ctx.obj["from_file"] = from_file
    ctx.obj["to_output"] = to_output

    # If no subcommand and no flags, show help
    if ctx.invoked_subcommand is None and not (from_file or to_output):
        typer.echo(ctx.get_help())
        raise typer.Exit

    # If no subcommand but both files are provided
    if ctx.invoked_subcommand is None and from_file and to_output:
        ctx.invoke(infer)


app.command()(init)
app.command()(render)
app.command()(combine)
app.command()(build)
app.command()(infer)
app.command(
    hidden=True,  # NotImplemented.
)(footer)

if __name__ == "__main__":
    app()
