"""CLI entrypoint."""

import typer

from gatpack.cli.build import build
from gatpack.cli.combine import combine
from gatpack.cli.footer import footer
from gatpack.cli.init import init
from gatpack.cli.render import render

# Create Typer app instance
app = typer.Typer(
    name="gatpack",
    help="A PDF and website templating tool",
    add_completion=True,
    no_args_is_help=True,
)

app.command()(init)
app.command()(render)
app.command()(combine)
app.command()(build)
app.command(
    # hidden=True,  # NotImplemented.
)(footer)


if __name__ == "__main__":
    app()
