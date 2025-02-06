from pathlib import Path
from typing import Annotated, Optional

from loguru import logger
from rich import print
import typer

from gatpack.cli.init import init
from gatpack.cli.render import render

# Create Typer app instance
app = typer.Typer(
    name="gatpack",
    help="A PDF and website templating tool",
    add_completion=False,
)

app.command()(init)
app.command()(render)


@app.command()
def main(
    name: str = typer.Argument(..., help="Name to greet"),
    log_file: Optional[Path] = Annotated[
        None,
        typer.Option(
            "--log-file",
            "-l",
            help="Path to log file",
        ),
    ],
) -> None:
    """Run the gatpack CLI."""
    if log_file:
        logger.add(log_file)

    logger.info(f"Hello {name}")


if __name__ == "__main__":
    app()
