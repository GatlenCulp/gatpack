import typer
from loguru import logger


def main(name: str) -> None:
    """Runs the gatpack cli."""
    logger.info(f"Hello {name}")


if __name__ == "__main__":
    typer.run(main)
