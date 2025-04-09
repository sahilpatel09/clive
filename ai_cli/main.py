import os
import click
from .commands import suggest_command, explain_command, bash_command, prompt_command

from typing import Optional
from rich.console import Console
from rich.markdown import Markdown
from rich.progress import Progress
from rich.spinner import Spinner

console = Console()

def show_loading():
    console.print("[bold yellow]Loading...[/bold yellow]", end="\r")

def print_md(text: str) -> None:
    """Print Markdown text to console with additional formatting."""
    md = Markdown(text)
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
@click.option('--short', is_flag=True, help="Keep the response short and straightforward.")
def prompt(prompt: str) -> None:
    """Generate an answer to your questions."""
    try:
        if short:
            prompt = f"Please keep your response short and to the point: {prompt}"
        result = prompt_command(prompt)
        print_md(result)
    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


@cli.command()
@click.argument('prompt')
@click.option('--short', is_flag=True, help="Keep the response short and straightforward.")
def prompt(prompt: str, short: bool) -> None:
    """Generate an answer to your questions."""
    show_loading()
    if short:
        prompt = f"Please keep your response short and to the point: {prompt}"
    print_md(prompt_command(prompt))

from dataclasses import dataclass
from datetime import datetime
@dataclass
class Message:
    user: str
    message: str
    timestamp: int = datetime.now()

@dataclass
class Chat:
    """Chat Room"""
    messages = []

    def broadcast(self, sender, content):
        msg = Message(sender, content)
        msg.user = sender
        msg.message = content
        self.messages.append(msg)   

import google.generativeai as genai


genai.configure(api_key='AIzaSyALLXnxtajBKpxgt4W_ZAcpm7lRDDYYhgo')
model = genai.GenerativeModel('gemini-1.5-flash')
conversation_history = []

os.makedirs('chats', exist_ok=True)

import random 

def chat_with_model(user_input, filename):
    global conversation_history
    conversation_history.append({"role": "user", "parts": [{"text": user_input}]})
    response = model.generate_content(conversation_history)
    model_reply = response.text
    conversation_history.append({"role": "model", "parts": [{"text": model_reply}]})
    
    name = "_".join(filename.split(" "))

    with open(f'chats/{name}.txt', 'a') as f:
        f.write(f"User: {user_input} \nAI: {model_reply} \n")
    return model_reply

@cli.command()
def chat() -> None:
    """Generate an answer to your questions."""
    try:
        filename = input("Please name this chat: ")
        while True: 
            input_str = str(input("User: "))
            response = chat_with_model(input_str, filename)
            print_md(f"AI: {response}")

    except Exception as e:
        console.print(f"Error: {e}", style="bold red")


if __name__ == '__main__':
    cli()
