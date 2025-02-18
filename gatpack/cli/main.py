"""CLI entrypoint."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

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
)

# Define options at module level
FROM_FILE_OPTION = typer.Option(
    None,
    "--from",
    "-f",
    help="Input file path",
)

TO_OUTPUT_OPTION = typer.Option(
    None,
    "--to",
    "-t",
    help="Output file path",
)

COMPOSE_FILE_OPTION = typer.Option(
    None,
    "--compose",
    help="The compose.gatpack.json file to use for templating operations.",
)

OVERWRITE_OPTION = typer.Option(
    False,
    "--overwrite",
    help="Whether to overwrite output files if they already exist",
)


def version_callback(value: bool) -> None:  # noqa: FBT001
    """Print version and exit."""
    if value:
        typer.echo("gatpack version: 0.0.6")
        raise typer.Exit


VERSION_OPTION = typer.Option(
    None,
    "--version",
    "-v",
    callback=version_callback,
    is_eager=True,
    help="Show version and exit",
)


@app.callback(invoke_without_command=True)
def root(
    ctx: typer.Context,
    from_file: Optional[str] = FROM_FILE_OPTION,
    to_output: Optional[str] = TO_OUTPUT_OPTION,
    compose_file: Optional[Path] = COMPOSE_FILE_OPTION,
    overwrite: bool = OVERWRITE_OPTION,
    version: Optional[bool] = VERSION_OPTION,
) -> None:
    """Common parameters for all commands."""
    ctx.ensure_object(dict)
    ctx.obj["file"] = from_file
    ctx.obj["output"] = to_output
    ctx.obj["overwrite"] = overwrite

    # If no subcommand and no flags, show help
    if ctx.invoked_subcommand is None and not (from_file or to_output):
        typer.echo(ctx.get_help())
        raise typer.Exit

    # If no subcommand but both files are provided
    if ctx.invoked_subcommand is None and from_file and to_output:
        ctx.invoke(
            infer,
            file=Path(from_file),
            output=Path(to_output),
            overwrite=overwrite,
            compose_file=compose_file,
        )


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
