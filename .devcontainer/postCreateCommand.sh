#! /usr/bin/env bash

# Install Dependencies
uv venv
uv sync --dev
source './.venv/bin/activate'
pre-commit install --install-hooks