"""Add a footer to a PDF."""

from pathlib import Path
from typing import Any, Literal

from pypdf import PdfWriter, PdfReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io


def add_footer_to_pdf(
    file: Path,
    output: Path,
    text: str,
    **kwargs: dict[str, Any],
) -> None:
    """Combines any number of provided pdfs into a single one."""
    if not file.exists():
        err_msg = f"The following PDF does not exist: {file}"
        raise FileNotFoundError(err_msg)
    if output.exists():
        err_msg = f"There already exists a file at {output}"
        raise FileExistsError(err_msg)

    add_page_numbers(file, output)

    # pdf = io.BytesIO()
    # c = canvas.Canvas(packet, pagesize=letter)
    # c.setFont(font_name, font_size)

    # pdf_writer = PdfWriter()
    # for i in range(num_pages):
    #     if i not in list(map(lambda j: j - 1, skip_pages)):
    #         footer = footer_text.format(i=i + 1, n=num_pages)
    #         footer_width = c.stringWidth(footer, font_name, font_size)
    #         footer_object = c.beginText((letter[0] - footer_width) / 2, 20)
    #         footer_object.setFont(font_name, font_size)
    #         footer_object.textOut(footer)
    #         c.drawText(footer_object)
    #     c.showPage()
    # c.save()
    # packet.seek(0)
    # return PdfReader(packet)


def add_page_numbers(input_pdf_path, output_pdf_path):
    reader = PdfReader(input_pdf_path)
    writer = PdfWriter()

    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        packet = io.BytesIO()
        can = canvas.Canvas(packet, pagesize=letter)
        can.setFont('Helvetica', 10)
        can.drawString(297.5, 15, f"{page_num + 1} / {len(reader.pages)}")
        can.save()
        packet.seek(0)
        page_num_pdf = PdfReader(packet)

        numbered_page = page_num_pdf.pages[0]
        page.merge_page(numbered_page)
        writer.add_page(page)

    with open(output_pdf_path, "wb") as output_pdf:
        writer.write(output_pdf)
