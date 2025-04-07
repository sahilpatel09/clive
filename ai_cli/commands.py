import requests
from .config import get_api_key

import json
import os
import requests
from dotenv import load_dotenv

# Load the environment variables from the .env file
load_dotenv()

# Get the Gemini API key from the .env file
API_KEY = os.getenv('GEMINI_API_KEY')

def query_gemini(prompt: str) -> str:
    """Query the Google Gemini API and return a response."""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    # Make the POST request
    response = requests.post(url, headers=headers, json=data)

    if response.status_code != 200:
        return f"❌ Error: {response.status_code} - {response.text}"

    #print("Type of response text", type(response.json()), response.json())

    try:
        # Assuming the response is in the format we expect
        return response.json()['candidates'][0]['content']['parts'][0]['text']
    except KeyError:
        raise TypeError('Unexpected response format')
        return f"❌ Unexpected response format: {response.text}"


def suggest_command(idea):
    return query_gemini(f"Suggest a terminal command for: {idea}, keep your response as straight to the answer possible and in few lines.")

def prompt_command(prompt):
    return query_gemini(prompt)

def explain_command(command):
    return query_gemini(f"Explain this command like I'm 5: {command}")

def bash_command(task):
    return query_gemini(f"Write a bash command to: {task}")


