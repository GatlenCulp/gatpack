"""Builds a PDF from a LaTeX source document."""

from pathlib import Path
import subprocess
from typing import Any

from loguru import logger

# TODO: Perhaps in the future, switch to PyLaTeX


def _check_latex_installed() -> bool:
    """Check if pdflatex is available on the system."""
    try:
        subprocess.run(
            ["pdflatex", "--version"],
            capture_output=True,
            check=True,
        )
        return True
    except (subprocess.SubprocessError, FileNotFoundError):
        return False


def build_pdf_from_latex(
    file: Path,
    output: Path,
    overwrite: bool = False,
    **kwargs: dict[str, Any],
) -> None:
    """Build a PDF from a LaTeX source document using pdflatex.

    Args:
        file: Path to the LaTeX source file
        output: Desired output path for the PDF
        overwrite: Whether to overwrite the output file if it already exists
        **kwargs: Additional arguments to pass to pdflatex

    Raises:
        FileNotFoundError: If the input file doesn't exist
        FileExistsError: If the output file already exists and overwrite=False
        RuntimeError: If the PDF compilation fails
    """
    if not _check_latex_installed():
        err_msg = "pdflatex not found on the path, please install and run again."
        raise Exception(err_msg)
    if not file.exists():
        err_msg = f"The following LaTeX document does not exist: {file}"
        raise FileNotFoundError(err_msg)
    if output.exists() and not overwrite:
        err_msg = f"There already exists a file at {output}"
        raise FileExistsError(err_msg)

    logger.info(f"Rendering LaTeX at {file}")
    logger.info(f"And saving to {output}")

    # Run pdflatex in the same directory as the input file
    working_dir = file.parent
    result = subprocess.run(
        [
            "pdflatex",
            "-interaction=nonstopmode",  # Don't stop for errors
            "-halt-on-error",  # But do exit if there are errors
            file.name,  # Just the filename since we're in the working dir
        ],
        cwd=file.parent,
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        logger.error(f"LaTeX compilation failed:\n{result.stderr}")
        raise RuntimeError("PDF compilation failed. Check the LaTeX logs for details.")

    # TODO: Fix name collisions
    # pdflatex creates the PDF in the same directory as the source
    # with the same name but .pdf extension
    temp_pdf = working_dir / file.with_suffix(".pdf").name

    # Move to desired output location
    # if output.exists() and overwrite:
    # output.unlink()  # Remove existing file if overwriting
    temp_pdf.rename(output)
    logger.success(f"Successfully created PDF at {output}")
