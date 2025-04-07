import click
from .commands import suggest_command, explain_command, bash_command, prompt_command

from rich.console import Console
from rich.markdown import Markdown

console = Console()

def print_md(text):
    md = Markdown(text)
    print("\n")
    console.print(md)
    print("\n \n")

@click.group()
def cli():
    pass

@cli.command()
@click.argument('idea')
def suggest(idea):
    """Suggest a terminal command based on a description."""
    print_md(suggest_command(idea))

@cli.command()
@click.argument('command')
def explain(command):
    """Explain a given command in simple terms."""
    print_md(explain_command(command))

@cli.command()
@click.argument('task')
def bash(task):
    """Generate a bash command to accomplish a task."""
    print_md(bash_command(task))

@cli.command()
@click.argument('prompt')
def prompt(prompt):
    """Generate an answer to your questions."""
    print_md(prompt_command(prompt))


if __name__ == '__main__':
    cli()

