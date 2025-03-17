"""Combines PDFs from any list of files."""

from pathlib import Path
from typing import Literal

from loguru import logger
from pypdf import PdfWriter

TemplateType = Literal["default"]  # Add more template types as needed
TEMPLATE_URLS = {
    "default": "https://github.com/GatlenCulp/cookiecutter-gatpack.git",
}


def resolve_globs(pdfs: list[str]) -> list[Path]:
    """Transforms a list of strings containing globs into a list of paths."""
    resolved_pdfs = []
    # Deal with globbing
    for pdf in pdfs:
        glob = list(
            Path.glob(
                Path.cwd(),
                pdf,
            ),
        )
        if not glob:
            err_msg = "Glob picked up no files: {pdf}"
            raise FileNotFoundError(err_msg)
        invalid_selected_files = [pdf for pdf in glob if not pdf.is_file()]
        if invalid_selected_files:
            err_msg = "Glob picked up the following invalid files:\n" + "\n".join(
                invalid_selected_files,
            )
            raise Exception(err_msg)
        # Sort files alphabetically before adding them
        glob.sort()
        resolved_pdfs.extend(glob)
    return resolved_pdfs


def combine_pdfs(
    pdfs: list[Path],
    output: Path,
    overwrite: bool,
) -> None:
    """Combines any number of provided pdfs into a single one."""
    non_existent_pdfs = [pdf for pdf in pdfs if not pdf.exists()]
    if non_existent_pdfs:
        err_msg = "The following pdfs do not exist:\n" + "\n".join(non_existent_pdfs)
        raise FileNotFoundError(err_msg)
    if output.exists() and not overwrite:
        err_msg = f"There already exists a file at {output}"
        raise FileExistsError(err_msg)

    pdf_writer = PdfWriter()
    for pdf in pdfs:
        pdf_writer.append(pdf)
    pdf_writer.write(output)
    pdf_writer.close()
    logger.info(f"{len(pdfs)} pdfs have been combined into {output}")
