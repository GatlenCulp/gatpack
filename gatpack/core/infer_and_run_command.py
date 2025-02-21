"""Infers and runs the operations needed to convert one file type to another."""

from __future__ import annotations

from pathlib import Path
from typing import Literal, Optional

from gatpack.core.build_pdf_from_latex import build_pdf_from_latex
from gatpack.core.exceptions import (
    ComposeFileNotFoundError,
    FileTypeInferenceError,
    MultipleComposeFilesError,
    UnsupportedConversionError,
)
from gatpack.core.load_compose import GatPackCompose, load_compose
from gatpack.core.render_jinja import render_jinja


def _search_for_compose(search_dir: Path) -> GatPackCompose | None:
    """Finds a compose file within the search_dir."""
    found_compose_files = list(search_dir.glob("*.gatpack.json"))
    if len(found_compose_files) == 0:
        return None
    if len(found_compose_files) == 1:
        inferred_compose = found_compose_files[0]
    else:
        # TODO(Gatlen): Update this to prompt the user for which compose file they would like to use
        raise MultipleComposeFilesError(
            f"Multiple compose files found in {search_dir}. Please specify which one to use.",
        )
    return load_compose(inferred_compose)


def infer_compose(search_dir: Optional[Path] = None) -> GatPackCompose:
    """Infers the compose file to use. Order: cwd, then input file dir."""
    search_order = [Path.cwd(), search_dir] if search_dir else [Path.cwd()]
    for target_dir in search_order:
        compose = _search_for_compose(target_dir)
        if compose:
            return compose
    raise ComposeFileNotFoundError(f"Could not infer compose from {search_order}.")


def _infer_file_type(file: Path) -> Literal["tex", "jinja-tex", "pdf"]:
    """Infers the file type from a path. Currently just checks file extension."""
    input_type = file.name.split(".")
    if len(input_type) == 1:
        raise FileTypeInferenceError(f"Unable to infer the file type of {file}")
    if input_type[-1] == "pdf":
        return "pdf"
    if input_type[-1] == "tex":
        if len(input_type) >= 3 and input_type[-2] == "jinja":
            return "jinja-tex"
        return "tex"
    raise FileTypeInferenceError(f"Unable to infer the file type of {file}")


def infer_and_run_command(
    file: Path,
    output: Path,
    overwrite: bool = False,
    compose_file: Optional[Path] = None,
) -> None:
    """Infers the command that needs to be run based on arguments."""
    # TODO: Perhaps in the future, search for a command path from the
    # input file to the output file. Encorporate pandoc in this.
    input_type = _infer_file_type(file)
    output_type = _infer_file_type(output)
    if input_type == "jinja-tex" and output_type == "tex":
        compose = load_compose(compose_file) if compose_file else infer_compose(file.parent)
        render_jinja(file, output, context=compose.context)
        return
    if input_type == "tex" and output_type == "pdf":
        build_pdf_from_latex(file, output)
        return
    if input_type == "jinja-tex" and output_type == "pdf":
        compose = load_compose(compose_file) if compose_file else infer_compose(file.parent)
        intermediate_path = file.with_name(file.name.split(".")[0] + ".tex")
        render_jinja(file, intermediate_path, context=compose.context, overwrite=overwrite)
        build_pdf_from_latex(intermediate_path, output, overwrite=overwrite)
        return
    raise UnsupportedConversionError(
        f"Unable to infer command to run with input of {input_type} to output of {output_type}",
    )
