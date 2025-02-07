from pydantic import BaseModel, Field
from typing import Any


## Inspiration from GitHub Actions?
# name: "Setup Python Environment"
# description: "Set up Python environment for the given Python version"

# inputs:
#   python-version:
#     description: "Python version to use"
#     required: true
#     default: "3.12"
#   uv-version:
#     description: "uv version to use"
#     required: true
#     default: "0.4.6"

# runs:
#   using: "composite"
#   steps:
#     - uses: actions/setup-python@v5
#       with:
#         python-version: ${{inputs.python-version}}

#     - name: Install uv
#       uses: astral-sh/setup-uv@v2
#       with:
#         version: ${{inputs.uv-version}}
#         enable-cache: "true"
#         cache-suffix: ${{matrix.python-version}}

#     - name: Install Python dependencies
#       run: uv sync --frozen
#       shell: bash


## Inspirations from Docker Compose?
# include:
#    - infra.yaml
# services:
#   web:
#     build: .
#     ports:
#       - "8000:5000"
#     develop:
#       watch:
#         - action: sync
#           path: .
#           target: /code


class GatPackCompose(BaseModel):
    """Class representing the GatPack Compose file."""

    # Is this even necessary?
    name: str = Field(
        "",
        description="Optional name for the configuration file",
        examples=[
            "Intro Fellowship Reading Packet",
        ],
    )
    context: dict[str, Any] = Field(
        {},
        description="Context assigning values to variable names",
        examples=[
            {
                "program_long_name": "Intro Fellowship",
                "time_period": "Spring 2024",
                "chron_info": "WEEK 5",
                "title": "Model internals",
                "subtitle": "READINGS",
            },
        ],
    )
