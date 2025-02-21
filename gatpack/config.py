"""Project configuration and path management.

Defines project-wide constants, directory structures, and logging setup.
Automatically loads environment variables from .env if present.
"""

from __future__ import annotations

from pathlib import Path
import sys
from typing import Union

from dotenv import load_dotenv
from loguru import logger
from rich.console import Console
from rich.theme import Theme

# Load environment variables from .env file if it exists
load_dotenv()

# Version
VERSION = "0.1.2"

# Paths
PROJ_ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = PROJ_ROOT / "logs" / "gatpack.log"

# Custom theme for Rich
custom_theme = Theme(
    {
        "info": "cyan",
        "warning": "yellow",
        "error": "red bold",
        "success": "green bold",
        "path": "blue underline",
    },
)

# Create console instance with custom settings
console = Console(
    theme=custom_theme,
    highlight=True,
    log_path=LOG_PATH,
    log_time=True,
    log_time_format="[%X]",
)


# Configure logging
def setup_logger(
    log_path: Union[str, Path] = LOG_PATH,
    log_level: str = "INFO",
) -> None:
    """Configure loguru logger with console and file outputs.

    Args:
        log_path: Path to log file
        log_level: Minimum log level to display
    """
    # Remove default logger
    logger.remove()

    # Add console logger with colors
    logger.add(
        sys.stderr,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level>",
        level=log_level,
        colorize=True,
    )

    # Add file logger
    logger.add(
        str(log_path),
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function}:{line} - {message}",
        rotation="10 MB",
        compression="zip",
    )

    logger.info(f"Logging configured. Log file: {log_path}")


# Initialize logger
setup_logger(log_level="ERROR")

# Configure tqdm integration if available
try:
    from tqdm import tqdm

    logger.add(lambda msg: tqdm.write(msg, end=""), colorize=True)
except ModuleNotFoundError:
    pass

# Log project root path
logger.info(f"PROJ_ROOT path is: {PROJ_ROOT}")
