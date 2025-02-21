"""Interactive CLI mode for GatPack."""

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.table import Table
import typer

PROJECT_PANEL = "📦 Project Operations"
OPERATIONS_PANEL = "🛠️ Basic Operations"


def display_help(console: Console, commands: dict) -> None:
    """Display detailed help information about available commands.

    Args:
        console: Rich console instance for output.
        commands: Dictionary of command information.
    """
    table = Table(title="📚 Available Commands", show_header=True, header_style="bold magenta")
    table.add_column("Command", style="cyan")
    table.add_column("Category", style="green")
    table.add_column("Description", style="yellow")

    for name, (help_text, _, panel) in sorted(commands.items()):
        table.add_row(name, panel, help_text or "No description available")

    console.print("\n")
    console.print(table)
    console.print("\nType 'exit' to quit the interactive mode\n")


def interactive_mode(app: typer.Typer) -> None:
    """Run GatPack in interactive mode."""
    console = Console()

    console.print("\n[bold blue]🎮 Welcome to GatPack Interactive Mode![/]\n")

    # Map commands to their info and callbacks
    commands = {
        cmd.name: (cmd.help, cmd.callback, cmd.rich_help_panel)
        for cmd in app.registered_commands
        if not cmd.hidden
        and not cmd.deprecated
        and cmd.rich_help_panel in [PROJECT_PANEL, OPERATIONS_PANEL]
    }

    # Group commands by panel
    panels = {}
    for name, (help_text, _, panel) in commands.items():
        if panel not in panels:
            panels[panel] = []
        panels[panel].append((name, help_text))

    # Display commands in panels
    for panel_name, cmds in panels.items():
        content = "\n".join(f"{name} {help_text}" for name, help_text in sorted(cmds))
        console.print(Panel(content, title=panel_name, expand=True))

    while True:
        action = Prompt.ask(
            "\n[bold green]What would you like to do?[/]",
            choices=[*commands.keys(), "help", "exit"],
            default="exit",
        )

        if action == "exit":
            console.print("\n[bold blue]👋 Goodbye![/]\n")
            break

        if action == "help":
            display_help(console, commands)
            continue

        # Call the appropriate command
        try:
            if action in commands:
                commands[action][1]()  # Call the callback
        except Exception as e:
            console.print(f"[bold red]Error:[/] {e!s}")
