from pathlib import Path
from typing import Any
from rich import print
from jinja2 import Environment, FileSystemLoader

# Borrowed from Marc Brinkmann's latex repository (mbr/latex on github)
J2_ARGS = {
    "block_start_string": r"\BLOCK{",
    "block_end_string": "}",
    "variable_start_string": r"\VAR{",
    "variable_end_string": "}",
    "comment_start_string": r"\COMMENT{",
    "comment_end_string": "}",
    "line_statement_prefix": "%-",
    "line_comment_prefix": "%#",
    "trim_blocks": True,
}


def render_jinja(
    template: Path,
    output: Path,
    context: dict[str, Any],
    use_standard_jinja: bool = False,
) -> None:
    """Renders Jinja from the provided input file into the output file."""
    if not template.exists():
        err_msg = f"File at {template} does not exist."
        raise FileNotFoundError(err_msg)
    if output.exists():
        err_msg = f"There already exists a file at {output}"
        raise FileExistsError(err_msg)

    # Create environment with LaTeX or standard settings
    j2_env_args = {} if use_standard_jinja else J2_ARGS
    j2_env = Environment(
        loader=FileSystemLoader(template.parent),
        autoescape=True,
        **j2_env_args,
    )
    j2_template = j2_env.get_template(template.name)
    render = j2_template.render(context)
    output.write_text(render)
    print(f"✨ Template successfully rendered, see your result at {output}")
