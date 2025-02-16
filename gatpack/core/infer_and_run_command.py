from pathlib import Path
from typing import Literal

from gatpack.core.build_pdf_from_latex import build_pdf_from_latex
from gatpack.core.load_compose import GatPackCompose, load_compose
from gatpack.core.render_jinja import render_jinja


def infer_compose(search_dir: Path) -> GatPackCompose:
    """Infers the compose file to use."""
    found_compose_files = list(search_dir.glob("*.gatpack.json"))
    if len(found_compose_files) == 0:
        err_msg = (
            "The operation you're looking for requires a Gatpack Compose file "
            f"and none were found in the directory {search_dir.resolve()}."
        )
        raise FileNotFoundError(err_msg)
    if len(found_compose_files) == 1:
        inferred_compose = found_compose_files[0]
    else:
        # TODO(Gatlen): Update this to prompt the user for which compose file they would like to use
        inferred_compose = found_compose_files[0]
    return load_compose(inferred_compose)


def infer_file_type(file: Path) -> Literal["tex", "jinja-tex", "pdf"]:
    """Infers the file type from a path. Currently just checks file extension."""
    input_type = file.name.split(".")
    if len(input_type) == 1:
        err_msg = f"Unable to infer the file type of {file}"
        raise Exception(err_msg)
    if input_type[-1] == "pdf":
        return "pdf"
    if input_type[-1] == "tex":
        if len(input_type) >= 3 and input_type[-2] == "jinja":
            return "jinja-tex"
        return "tex"
    err_msg = f"Unable to infer the file type of {file}"
    raise Exception(err_msg)


def infer_and_run_command(file: Path, output: Path) -> None:
    """Infers the command that needs to be run based on arguments."""
    # TODO: Perhaps in the future, search for a command path from the
    # input file to the output file. Encorporate pandoc in this.
    input_type = infer_file_type(file)
    output_type = infer_file_type(output)
    if input_type == "jinja-tex" and output_type == "tex":
        compose = infer_compose(file.parent)
        render_jinja(file, output, context=compose.context)
        return
    if input_type == "tex" and output_type == "pdf":
        build_pdf_from_latex(file, output)
        return

    err_msg = (
        f"Unable to infer command to run with input of {input_type} to output of {output_type}"
    )
    raise Exception(err_msg)
