"""Add a footer to a PDF."""

from pathlib import Path
from typing import Any, Literal

from pypdf import PdfWriter
from reportlab.lib.pagesizes import letter


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

    raise NotImplementedError("add_footer_to_pdf has yet to be implemented.")

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
