from pathlib import Path
from typing import Any

from jinja2 import Environment, FileSystemLoader
from loguru import logger

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
    overwrite: bool = False,
) -> None:
    """Renders Jinja from the provided input file into the output file.

    Args:
        template: Path to the template file
        output: Path where the rendered file should be written
        context: Dictionary of variables to be rendered in the template
        use_standard_jinja: Whether to use standard Jinja delimiters instead of LaTeX-safe ones
        overwrite: Whether to overwrite the output file if it already exists
    """
    if not template.exists():
        err_msg = f"File at {template} does not exist."
        raise FileNotFoundError(err_msg)
    if output.exists() and not overwrite:
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
    logger.info(f"Template successfully rendered, see result at {output}")
