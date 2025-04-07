import click
from .commands import suggest_command, explain_command, bash_command, prompt_command

from typing import Optional
from rich.console import Console
from rich.markdown import Markdown

# Create a console instance
console = Console()

def print_md(text: str) -> None:
    """Print Markdown text to console with additional formatting."""
    md = Markdown(text)
    print("\n")
    console.print(md)
    print("\n")

@click.group()
def cli() -> None:
    """A CLI tool to interact with terminal commands such as suggestion, explanation, and bash command generation."""
    pass

@cli.command()
@click.argument('idea')
def suggest(idea: str) -> None:
    """Suggest a terminal command based on a description."""
    try:
        result = suggest_command(idea)
        print_md(result)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

@cli.command()
@click.argument('command')
def explain(command: str) -> None:
    """Explain a given command in simple terms."""
    try:
        result = explain_command(command)
        print_md(result)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

@cli.command()
@click.argument('task')
def bash(task: str) -> None:
    """Generate a bash command to accomplish a task."""
    try:
        result = bash_command(task)
        print_md(result)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")

@cli.command()
@click.argument('prompt')
def prompt(prompt: str) -> None:
    """Generate an answer to your questions."""
    try:
        result = prompt_command(prompt)
        print_md(result)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


if __name__ == '__main__':
    cli()
