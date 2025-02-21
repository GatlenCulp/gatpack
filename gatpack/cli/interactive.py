"""Interactive CLI mode for GatPack."""

import os
from pathlib import Path

from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import typer

PROJECT_PANEL = "📦 Project Operations"
OPERATIONS_PANEL = "🛠️ Basic Operations"
FILESYSTEM_PANEL = "📁 File System Operations"


def format_path(path: Path) -> str:
    """Format path for display in prompt.

    Args:
        path: Path to format

    Returns:
        Formatted path string with home directory as ~ and components separated
    """
    try:
        # Convert to relative to home directory if possible
        home = Path.home()
        try:
            relative_to_home = path.relative_to(home)
            path_str = f"~/{relative_to_home}"
        except ValueError:
            path_str = str(path)

        # Split into components and style
        components = path_str.split(os.sep)
        styled_components = []
        for i, comp in enumerate(components):
            if i == len(components) - 1:  # Last component
                styled_components.append(f"[bold cyan]{comp}[/]")
            else:
                styled_components.append(f"[blue]{comp}[/]")

        return f"[blue]{os.sep}[/]".join(styled_components)
    except Exception:
        # Fallback to simple path if any error occurs
        return str(path)


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


def ls_command() -> None:
    """List contents of current directory."""
    console = Console()
    try:
        for item in sorted(Path.cwd().iterdir()):
            prefix = "📁" if item.is_dir() else "📄"
            console.print(f"{prefix} {item.name}")
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e!s}")


def cd_command(path: str = "..") -> None:
    """Change current working directory.

    Args:
        path: Target directory path. Defaults to parent directory.
    """
    console = Console()
    try:
        os.chdir(path)
        console.print(f"[green]Changed directory to:[/] {Path.cwd()}")
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e!s}")


def pwd_command() -> None:
    """Print current working directory."""
    console = Console()
    try:
        console.print(f"[green]Current directory:[/] {Path.cwd()}")
    except Exception as e:
        console.print(f"[bold red]Error:[/] {e!s}")


def interactive_mode(app: typer.Typer) -> None:
    """Run GatPack in interactive mode."""
    console = Console()

    console.print("\n[bold blue]🎮 Welcome to GatPack Interactive Mode![/]")
    console.print("[dim]Type 'help' to see available commands[/]\n")

    # Add filesystem commands
    filesystem_commands = {
        "ls": ("List contents of current directory", ls_command, FILESYSTEM_PANEL),
        "cd": ("Change current working directory", cd_command, FILESYSTEM_PANEL),
        "pwd": ("Print current working directory", pwd_command, FILESYSTEM_PANEL),
    }

    # Map commands to their info and callbacks
    commands = {
        cmd.name: (cmd.help, cmd.callback, cmd.rich_help_panel)
        for cmd in app.registered_commands
        if not cmd.hidden
        and not cmd.deprecated
        and cmd.rich_help_panel in [PROJECT_PANEL, OPERATIONS_PANEL]
    }

    # Add filesystem commands to the command dictionary
    commands.update(filesystem_commands)

    # Group commands by panel
    panels = {}
    for name, (help_text, _, panel) in commands.items():
        if panel not in panels:
            panels[panel] = []
        panels[panel].append((name, help_text))

    while True:
        # Show current directory in prompt with nice formatting
        cwd = Path.cwd()
        formatted_path = format_path(cwd)
        action = Prompt.ask(
            f"\n📍 {formatted_path}\n[bold green]What would you like to do?[/]",
            choices=[*commands.keys(), "help", "exit"],
            default="help",
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
                if action == "cd":
                    path = Prompt.ask("Enter directory path", default="..")
                    commands[action][1](path)  # Call cd with path argument
                else:
                    commands[action][1]()  # Call the callback
        except Exception as e:
            console.print(f"[bold red]Error:[/] {e!s}")
