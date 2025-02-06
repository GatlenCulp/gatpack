from pathlib import Path
from typing import Optional

import typer
from loguru import logger

# Create Typer app instance
app = typer.Typer(
    name="gatpack",
    help="A PDF and website templating tool",
    add_completion=True,
)


@app.command()
def main(
    name: str = typer.Argument(..., help="Name to greet"),
    log_file: Optional[Path] = typer.Option(
        None,
        "--log-file",
        "-l",
        help="Path to log file",
    ),
) -> None:
    """Run the gatpack CLI."""
    if log_file:
        logger.add(log_file)

    logger.info(f"Hello {name}")


if __name__ == "__main__":
    app()
