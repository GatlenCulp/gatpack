"""Show usage examples with rich-click's standard formatting."""

from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from gatpack.config import console

# These are the proper style constants from rich-click
STYLE_USAGE = "yellow"
STYLE_OPTION = "bold cyan"
STYLE_METAVAR = "bold yellow"
STYLE_HELPTEXT = "dim"


def examples() -> None:
    """Show usage examples with rich-click's standard formatting."""

    table = Table(
        show_header=False,
        box=None,
        padding=(0, 2),
        collapse_padding=True,
        show_lines=False,
        leading=1,  # Add vertical spacing between rows
    )
    table.add_column("Examples", style="white")

    # Define examples using rich-click's standard styles
    examples = [
        (f"# Initialize a new template\n[{STYLE_USAGE}]gatpack[/] [{STYLE_OPTION}]init[/] \n"),
        (
            "# Render a template to PDF\n"
            f"[{STYLE_USAGE}]gatpack[/] "
            f"[{STYLE_OPTION}]-f[/] [{STYLE_METAVAR}]template.tex[/] "
            f"[{STYLE_OPTION}]-t[/] [{STYLE_METAVAR}]output.pdf[/]\n"
        ),
        (
            "# Combine multiple PDFs\n"
            f"[{STYLE_USAGE}]gatpack[/] "
            f"[{STYLE_OPTION}]combine[/] "
            f"[{STYLE_METAVAR}]input1.pdf input2.pdf[/] "
            f"[{STYLE_METAVAR}]combined.pdf[/]\n"
        ),
    ]

    # Add examples to table
    for example in examples:
        table.add_row(example)

    # Create header
    header = Text("🚀 GatPack Usage Examples", style="bold cyan")

    # Display in a panel
    console.print(
        Panel(
            table,
            title=header,
            border_style="cyan",
            padding=(1, 2),
        ),
    )

    # Add legend using Typer's styles
    legend = Table.grid(padding=1)
    legend.add_row(
        Text("Legend:", style="bold white"),
        Text("Command", style=STYLE_USAGE),
        Text("Action", style=STYLE_OPTION),
        Text("Flag", style=STYLE_OPTION),
        Text("Value", style=STYLE_METAVAR),
    )
