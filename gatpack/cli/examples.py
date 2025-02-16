from rich.console import Console
from rich.panel import Panel
from rich.syntax import Syntax
from rich.text import Text


# Add examples panel
def examples() -> None:
    """Show usage examples.

    This command displays common usage patterns for GatPack with rich formatting.
    """
    console = Console()

    # Create example commands with syntax highlighting
    examples_text = """
# Initialize a new template
gatpack init my-template

# Render a template to PDF
gatpack render -f template.tex -t output.pdf

# Combine multiple PDFs
gatpack combine -f input1.pdf input2.pdf -t combined.pdf

# Build a project
gatpack build -f project/ -t output/
"""

    # Create syntax highlighted block
    syntax = Syntax(
        examples_text.strip(),
        "bash",
        theme="monokai",
        word_wrap=True,
    )

    # Create header
    header = Text("🚀 GatPack Usage Examples", style="bold cyan")

    # Display in a nice panel
    console.print(
        Panel(
            syntax,
            title=header,
            border_style="cyan",
            padding=(1, 2),
        )
    )
