"""Add a footer to a PDF."""

import io
from pathlib import Path
from typing import Literal

from pypdf import PdfReader, PdfWriter
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def add_footer_to_pdf(
    file: Path,
    output: Path,
    text: str,
    overwrite: bool = False,
) -> None:
    """Adds a footer to a PDF."""
    if not file.exists():
        err_msg = f"The following PDF does not exist: {file}"
        raise FileNotFoundError(err_msg)
    if output.exists() and not overwrite:
        err_msg = f"There already exists a file at {output}"
        raise FileExistsError(err_msg)

    _add_page_numbers(file, output, text)


def _add_page_numbers(
    input_pdf_path: Path,
    output_pdf_path: Path,
    text: str,
    font_size: float = 10,
    y_pos: float = 30,
    horizontal_align: Literal["left", "center", "right"] = "right",
) -> None:
    # if horizontal_align in ["center", "right"]:
    #     err_msg = "Center and right alignments are not yet implemented."
    #     raise NotImplementedError(err_msg)
    x_pos = None
    if horizontal_align == "left":
        x_pos = 60
    elif horizontal_align == "center":
        x_pos = 297.5
    elif horizontal_align == "right":
        x_pos = 500

    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        footer_text = text.format(
            n=page_num + 1,
            N=len(reader.pages),
        )
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont("Helvetica", font_size)
        can.drawString(x_pos, y_pos, footer_text)
        can.save()
        packet.seek(0)
        page_num_pdf = PdfReader(packet)

        numbered_page = page_num_pdf.pages[0]
        page.merge_page(numbered_page)
        writer.add_page(page)

    with output_pdf_path.open("wb") as output_pdf:
        writer.write(output_pdf)
