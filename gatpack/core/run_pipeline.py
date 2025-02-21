"""Infers and runs the operations needed to convert one file type to another."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from rich.console import Console
from rich.panel import Panel
from rich.progress import track

from gatpack.core.add_footer_to_pdf import add_footer_to_pdf
from gatpack.core.combine_pdfs import combine_pdfs, resolve_globs
from gatpack.core.infer_and_run_command import infer_and_run_command, infer_compose, load_compose
from gatpack.schema.GatPackCompose import CombineStep, FooterStep, RenderStep, Step

console = Console()


def _run_step(step: Step, overwrite: bool = False) -> None:
    """Runs a given step."""
    if isinstance(step, RenderStep):
        infer_and_run_command(Path(step.from_), Path(step.to), overwrite=overwrite)
        return
    if isinstance(step, CombineStep):
        pdfs = resolve_globs(step.combine)
        combine_pdfs(pdfs, Path(step.to), overwrite=overwrite)
        return
    if isinstance(step, FooterStep):
        add_footer_to_pdf(Path(step.from_), Path(step.to), step.text, overwrite=overwrite)
        return
    err_msg = f"Unknown step type {type(step)} for step:\n{step}"
    raise Exception(err_msg)


def run_pipeline(
    pipeline_id: str,
    compose_file: Optional[Path] = None,
    overwrite: bool = False,
) -> None:
    """Run the specified pipeline."""
    compose = load_compose(compose_file) if compose_file else infer_compose()
    try:
        pipeline = next(
            filter(
                lambda pipeline: pipeline.id == pipeline_id,
                compose.pipelines,
            ),
        )
    except Exception:
        err_msg = f"pipeline id {pipeline_id} not detected in compose file."
        raise Exception(err_msg)

    console.print(
        f"\n[bold blue]Running Pipeline:[/]\n"
        f"[cyan]{pipeline_id}[/] "
        f"[green]{pipeline.description}[/]",
    )

    for step in track(
        pipeline.steps,
        description="Processing steps",
        console=console,
    ):
        console.print(
            Panel(
                f"[bold]{step.name}[/]",
                border_style="cyan",
                padding=(0, 2),
            ),
        )
        _run_step(step, overwrite=overwrite)

    console.print("\n[bold green]✨ Pipeline ran successfully![/]")
