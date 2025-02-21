"""Helper functions for CLI error handling and user guidance."""

from __future__ import annotations

from rich.panel import Panel
from rich.text import Text

from gatpack.config import console
from gatpack.core.exceptions import (
    ComposeFileNotFoundError,
    FileTypeInferenceError,
    GatPackError,
    MultipleComposeFilesError,
    UnsupportedConversionError,
)


def handle_compose_file_error(error: ComposeFileNotFoundError) -> None:
    """Handle compose file not found error with helpful guidance."""
    message = Text()
    message.append("\n🔍 No compose file found!\n\n", style="bold red")
    message.append(
        "Make sure you are in the correct directory. A compose file should:\n",
        style="yellow",
    )
    message.append("  • Have a '.gatpack.json' extension\n", style="dim")
    message.append("  • Be in your current directory or the input file's directory\n", style="dim")
    message.append("\nTry running: ", style="green")
    message.append("ls *.gatpack.json", style="bold cyan")

    console.print(Panel(message, title="[red]Compose File Error", expand=False))


def handle_file_type_error(error: FileTypeInferenceError) -> None:
    """Handle file type inference error with supported formats."""
    message = Text()
    message.append("\n❌ Unable to determine file type!\n\n", style="bold red")
    message.append("Supported file types are:\n", style="yellow")
    message.append("  • .tex - LaTeX files\n", style="dim")
    message.append("  • .jinja.tex - Jinja-templated LaTeX files\n", style="dim")
    message.append("  • .pdf - PDF files\n", style="dim")
    message.append("\nMake sure your file has the correct extension.", style="green")

    console.print(Panel(message, title="[red]File Type Error", expand=False))


def handle_multiple_compose_error(error: MultipleComposeFilesError) -> None:
    """Handle multiple compose files error with guidance."""
    message = Text()
    message.append("\n⚠️  Multiple compose files found!\n\n", style="bold yellow")
    message.append("Please specify which compose file to use with:\n", style="yellow")
    message.append(
        "  gatpack compose --compose-file PATH_TO_COMPOSE.gatpack.json\n",
        style="bold cyan",
    )

    console.print(Panel(message, title="[yellow]Multiple Compose Files", expand=False))


def handle_unsupported_conversion(error: UnsupportedConversionError) -> None:
    """Handle unsupported file conversion error with supported paths."""
    message = Text()
    message.append("\n❌ Unsupported file conversion!\n\n", style="bold red")
    message.append("Supported conversion paths are:\n", style="yellow")
    message.append("  • .jinja.tex → .tex (Render template)\n", style="dim")
    message.append("  • .tex → .pdf (Build LaTeX)\n", style="dim")
    message.append("  • .jinja.tex → .pdf (Render template & build LaTeX)\n", style="dim")

    console.print(Panel(message, title="[red]Conversion Error", expand=False))


def handle_gatpack_error(error: GatPackError) -> None:
    """Main error handler for all GatPack errors."""
    if isinstance(error, ComposeFileNotFoundError):
        handle_compose_file_error(error)
    elif isinstance(error, FileTypeInferenceError):
        handle_file_type_error(error)
    elif isinstance(error, MultipleComposeFilesError):
        handle_multiple_compose_error(error)
    elif isinstance(error, UnsupportedConversionError):
        handle_unsupported_conversion(error)
    else:
        # Fallback for unknown GatPack errors
        console.print(f"\n[bold red]Error:[/] {error!s}\n")
