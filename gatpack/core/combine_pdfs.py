"""Combines PDFs from any list of files."""

from pathlib import Path
from typing import Any, Literal

from pypdf import PdfWriter
from loguru import logger

TemplateType = Literal["default"]  # Add more template types as needed
TEMPLATE_URLS = {
    "default": "https://github.com/GatlenCulp/cookiecutter-gatpack.git",
}


def combine_pdfs(
    pdfs: list[Path],
    output: Path,
    **kwargs: dict[str, Any],
) -> None:
    """Combines any number of provided pdfs into a single one."""
    non_existent_pdfs = [pdf for pdf in pdfs if not pdf.exists()]
    if non_existent_pdfs:
        err_msg = "The following pdfs do not exist:\n" + "\n".join(non_existent_pdfs)
        raise FileNotFoundError(err_msg)
    if output.exists():
        err_msg = f"There already exists a file at {output}"
        raise FileExistsError(err_msg)

    pdf_writer = PdfWriter()
    for pdf in pdfs:
        pdf_writer.append(pdf)
    pdf_writer.write(output)
    pdf_writer.close()
    print(f"{len(pdfs)} pdfs have been combined into {output}")
