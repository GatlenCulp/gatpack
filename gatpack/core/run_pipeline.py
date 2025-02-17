"""Infers and runs the operations needed to convert one file type to another."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from loguru import logger

from gatpack.core.combine_pdfs import combine_pdfs, resolve_globs
from gatpack.core.infer_and_run_command import infer_and_run_command, infer_compose, load_compose
from gatpack.schema.GatPackCompose import CombineStep, RenderStep, Step

import ipdb


def _run_step(step: Step, overwrite: bool = False) -> None:
    """Runs a given step."""
    if isinstance(step, RenderStep):
        # ipdb.set_trace()
        infer_and_run_command(Path(step.from_), Path(step.to), overwrite=overwrite)
        return
    if isinstance(step, CombineStep):
        pdfs = resolve_globs(step.combine)
        combine_pdfs(pdfs, Path(step.to), overwrite=overwrite)
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
    # Find first pipeline matching this id
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
    # ipdb.set_trace()
    logger.info(f"Found and now running {pipeline_id}")
    for step in pipeline.steps:
        print(step.name)
        _run_step(step, overwrite=overwrite)
    logger.info("Pipeline ran successfully.")
