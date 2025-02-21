"""Interactive CLI mode for GatPack."""

from rich.console import Console
from rich.prompt import Prompt
import typer

PROJECT_PANEL = "📦 Project Operations"
OPERATIONS_PANEL = "🛠️ Basic Operations"


def interactive_mode(app: typer.Typer) -> None:
    """Run GatPack in interactive mode."""
    console = Console()

    console.print("\n[bold blue]🎮 Welcome to GatPack Interactive Mode![/]\n")

    # Map commands to their functions
    commands = {
        cmd.name: cmd.callback
        for cmd in app.registered_commands
        if not cmd.hidden
        and not cmd.deprecated
        and cmd.rich_help_panel in [PROJECT_PANEL, OPERATIONS_PANEL]
    }

    while True:
        action = Prompt.ask(
            "\n[bold green]What would you like to do?[/]",
            choices=[*commands.keys(), "exit"],
            default="exit",
        )

        if action == "exit":
            console.print("\n[bold blue]👋 Thanks for using GatPack![/]\n")
            break

        # Call the appropriate command
        try:
            if action in commands:
                commands[action]()
        except Exception as e:
            console.print(f"[bold red]Error:[/] {e!s}")
