from pathlib import Path
from typing import Any
from rich import print
from jinja2 import Environment, Template

# TODO: look at this https://stackoverflow.com/questions/46652984/python-jinja2-latex-table

# ENV_ARGS = {
#     'block_start_string': '\BLOCK{',
#     'block_end_string': '}',
#     'variable_start_string': '\VAR{',
#     'variable_end_string': '}',
#     'comment_start_string': '\#{',
#     'comment_end_string': '}',
#     'line_statement_prefix': '%-',
#     'line_comment_prefix': '%#',
#     'trim_blocks': True,
#     'autoescape': False,
# }


def render_jinja(
    template: Path,
    output: Path,
    context: dict[str, Any],
) -> None:
    """Renders Jinja from the provided input file into the output file."""
    if not template.exists():
        err_msg = f"File at {template} does not exist."
        raise FileNotFoundError(err_msg)
    if output.exists():
        err_msg = f"There already exists a file at {output}"
        raise FileExistsError(err_msg)
    jinja_template = Template(template.read_text())
    render = jinja_template.render(context)
    output.write_text(render)
    print(f"Template successfully rendered, see your result at {output}")
