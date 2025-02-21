"""CLI entrypoint."""

from __future__ import annotations

# from trogon.typer import init_tui
import typer

from gatpack.cli.build import build
from gatpack.cli.combine import combine
from gatpack.cli.compose import compose
from gatpack.cli.examples import examples
from gatpack.cli.footer import footer
from gatpack.cli.infer import infer
from gatpack.cli.init import init
from gatpack.cli.interactive import interactive_mode
from gatpack.cli.options import version
from gatpack.cli.render import render

# Create Typer app instance
app = typer.Typer(
    name="gatpack",
    help="A LaTeX Template to PDF rendering tool.",
    no_args_is_help=True,
    add_completion=False,
)

# init_tui(app)

PROJECT_PANEL = "📦 Project Operations"
OPERATIONS_PANEL = "🛠️ Basic Operations"
HELP_PANEL = "👋 Help"

app.command(
    name="init",
    help="Use CookieCutter to initialize a new GatPack project in your specified directory.",
    short_help="Initialize a new GatPack project in your specified directory.",
    rich_help_panel=PROJECT_PANEL,
)(init)

app.command(
    name="compose",
    help="Run the specified pipleine ID as defined in the GatPack compose file.",
    short_help="Run the specified pipleine ID from the compose file.",
    rich_help_panel=PROJECT_PANEL,
)(compose)

app.command(
    name="combine",
    help="Combine PDFs (files or globs) and save them to the specified output file.",
    short_help="Combine PDFs into a single file.",
    rich_help_panel=OPERATIONS_PANEL,
)(combine)

app.command(
    name="infer",
    help=(
        "Infer and run needed operations to transform one file format to another. "
        "Automatically renders Jinja and builds PDFs."
    ),
    short_help="Automatically transform one file format to another.",
    rich_help_panel=OPERATIONS_PANEL,
)(infer)

app.command(
    name="show-examples",
    help="Show examples GatPack's common uses.",
    short_help="Show examples GatPack's common uses.",
    rich_help_panel=HELP_PANEL,
)(examples)

app.command(
    name="version",
    help="Get the current version of GatPack",
    short_help="Get the current version of GatPack",
    rich_help_panel=HELP_PANEL,
)(version)

app.command(
    name="footer",
    help="Add a footer to a pdf",
    short_help="Add a footer to a pdf",
    rich_help_panel=OPERATIONS_PANEL,
)(footer)

# Outdated Commands
app.command(deprecated=True, hidden=True, rich_help_panel=OPERATIONS_PANEL)(render)
app.command(deprecated=True, hidden=True, rich_help_panel=OPERATIONS_PANEL)(build)


# Add the interactive command
app.command(
    name="interactive",
    help="Start an interactive session with GatPack",
    short_help="Start an interactive session",
    rich_help_panel=HELP_PANEL,
)(lambda: interactive_mode(app))

if __name__ == "__main__":
    app()
