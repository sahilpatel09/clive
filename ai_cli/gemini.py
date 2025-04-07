import requests
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class GeminiClient:
    """A client to interact with the Gemini API."""
    api_key: str

    def _make_request(self, prompt: str) -> Dict[str, Any]:
        """Make the POST request to the Gemini API and return the raw response."""
        url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={self.api_key}"
        
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "contents": [{
                "parts": [{"text": prompt}]
            }]
        }

        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code != 200:
            raise ConnectionError(f"Error: {response.status_code} - {response.text}")
        
        return response.json()

    def _parse_response(self, response_data: Dict[str, Any]) -> str:
        """Parse the response data and extract the relevant information."""
        try:
            return response_data['candidates'][0]['content']['parts'][0]['text']
        except KeyError:
            raise TypeError('Unexpected response format')

    def query_gemini(self, prompt: str) -> str:
        """Query the Gemini API and return a parsed response."""
        response_data = self._make_request(prompt)  # Get raw response
        return self._parse_response(response_data)  # Parse the response
