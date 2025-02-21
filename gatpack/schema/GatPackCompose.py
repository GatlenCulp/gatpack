"""Model schema for a compose.gatpack.json file."""

from __future__ import annotations

from typing import Any, Optional, Union

from pydantic import BaseModel, Field


class RenderStep(BaseModel):
    """Step for rendering a single file using a template."""

    name: str = Field(..., description="Name of the rendering step")
    from_: str = Field(
        ...,
        alias="from",
        description="Source template file path",
    )
    to: str = Field(..., description="Output file path")


class CombineStep(BaseModel):
    """Step for combining multiple PDF files."""

    name: str = Field(..., description="Name of the combination step")
    combine: list[str] = Field(..., description="List of PDF files to combine")
    to: str = Field(..., description="Output combined PDF path")


class FooterStep(BaseModel):
    """Step for adding footers and page numbers to PDFs."""

    name: str = Field(..., description="Name of the footer step")
    from_: str = Field(
        ...,
        alias="from",
        description="PDF to add footer to",
    )
    to: str = Field(..., description="Path to save rendered footer")
    text: str = Field(
        "{n} of {N}",
        description="Text to use for the footer, using Python templating "
        "(n is current page number, N is total pages).",
    )


Step = Union[RenderStep, CombineStep, FooterStep]


class Pipeline(BaseModel):
    """Represents a single pipeline of steps to produce files."""

    id: str = Field(..., description="Unique identifier for the pipeline")
    description: Optional[str] = Field(..., description="Description of what the pipeline does")
    steps: list[Step] = Field(..., description="Ordered list of steps to execute")


class GatPackCompose(BaseModel):
    """Class representing the GatPack Compose file."""

    version: str = Field(
        "1.0",
        description="Schema version for compatibility checking",
    )
    name: Optional[str] = Field(
        "",
        description="Optional name for the configuration file.",
        examples=["Intro Fellowship Reading Packet"],
    )
    description: Optional[str] = Field(
        "",
        description="Optional description for the compose file.",
        examples=["Packet for CAIAC's Spring 2025 Intro Fellowship"],
    )
    context: Optional[dict[str, Any]] = Field(
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
    pipelines: list[Pipeline] = Field(
        [],
        description="Step-by-step pipelines to produce files.",
        examples=[
            [
                {
                    "id": "reading-packet",
                    "description": "Create the full reading packet.",
                    "steps": [
                        {
                            "name": "Render cover page",
                            "from": "cover/cover.jinja.tex",
                            "to": "cover/cover.pdf",
                        },
                        {
                            "name": "Render device readings page",
                            "from": "device_readings/device_readings.jinja.tex",
                            "to": "device_readings/device_readings.pdf",
                        },
                        {
                            "name": "Render further readings page",
                            "from": "further_readings/further_readings.jinja.tex",
                            "to": "further_readings/further_readings.pdf",
                        },
                        {
                            "name": "Combine all readings into packet.pdf",
                            "combine": [
                                "cover/cover.pdf",
                                "device_readings/device_readings.pdf",
                                "further_readings/further_readings.pdf",
                            ],
                            "to": "output/packet.pdf",
                        },
                    ],
                },
            ],
        ],
    )
