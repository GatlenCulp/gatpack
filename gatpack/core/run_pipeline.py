"""Infers and runs the operations needed to convert one file type to another."""

from __future__ import annotations

from pathlib import Path
from typing import Optional

from gatpack.core.infer_and_run_command import infer_compose, load_compose


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
    breakpoint()
