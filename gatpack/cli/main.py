from pathlib import Path
from typing import Annotated, Optional

from loguru import logger
from rich import print
import typer

from gatpack.cli.init import init
from gatpack.cli.render import render
from gatpack.cli.combine import combine
from gatpack.cli.build import build
from gatpack.cli.footer import footer

# Create Typer app instance
app = typer.Typer(
    name="gatpack",
    help="A PDF and website templating tool",
    add_completion=False,
)

app.command()(init)
app.command()(render)
app.command()(combine)
app.command()(build)
app.command()(footer)


if __name__ == "__main__":
    app()
