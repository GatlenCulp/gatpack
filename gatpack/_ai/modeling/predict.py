"""Model inference pipeline for gatpack.

Provides CLI interface to generate predictions using trained models.
"""

from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from gatpack.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    features_path: Path = PROCESSED_DATA_DIR / "test_features.csv", # noqa: ARG001 template arg
    model_path: Path = MODELS_DIR / "model.pkl", # noqa: ARG001 template arg
    predictions_path: Path = PROCESSED_DATA_DIR / "test_predictions.csv", # noqa: ARG001 template arg
    # -----------------------------------------
) -> None:
    """Generate predictions using a trained model.

    Args:
        features_path: Path to the test features CSV file
        model_path: Path to the trained model file
        predictions_path: Path where predictions will be saved

    Returns:
        None
    """
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Performing inference for model...")
    for i in tqdm(range(10), total=10):
        if i == 5:  # noqa: PLR2004 example code
            logger.info("Something happened for iteration 5.")
    logger.success("Inference complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
