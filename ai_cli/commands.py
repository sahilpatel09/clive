import os
from typing import Optional
from dotenv import load_dotenv
from .config import get_gemini_api_key
from .gemini import GeminiClient


GEMINI_API_KEY: Optional[str] = get_gemini_api_key()


def query_gemini(prompt: str) -> str:
    """
    Queries the Gemini API with the provided prompt and returns the response text.
    
    :param prompt: The prompt to send to the Gemini API.
    :return: The response text from the Gemini API.
    """
    if GEMINI_API_KEY is None:
        raise ValueError("GEMINI_API_KEY is not set. Make sure the environment variable 'GEMINI_API_KEY' is properly configured.")
    
    gemini_client = GeminiClient(api_key=GEMINI_API_KEY)
    response = gemini_client.query_gemini(prompt)
    return response


def suggest_command(idea: str) -> str:
    """
    Suggests a terminal command based on the given idea.

    :param idea: The idea for which a terminal command needs to be suggested.
    :return: The suggested terminal command as a string.
    """
    return query_gemini(f"Suggest a terminal command for: {idea}, keep your response as straight to the answer possible and in few lines.")


def prompt_command(prompt: str) -> str:
    """
    Queries the Gemini API directly with a custom prompt.

    :param prompt: The prompt to send to Gemini API.
    :return: The response text from the Gemini API.
    """
    return query_gemini(prompt)


def explain_command(command: str) -> str:
    """
    Asks Gemini to explain a terminal command in a simple way.

    :param command: The terminal command to be explained.
    :return: The explanation of the command in simple terms.
    """
    return query_gemini(f"Explain this command like I'm 5: {command}")


def bash_command(task: str) -> str:
    """
    Requests Gemini to write a bash command for the given task.

    :param task: The task description to generate a bash command for.
    :return: The bash command that Gemini generates for the task.
    """
    return query_gemini(f"Write a bash command to: {task}")
