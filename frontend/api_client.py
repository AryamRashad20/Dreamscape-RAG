import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")

if not API_URL:
    raise RuntimeError(
        "API_URL is not set. Please add API_URL to frontend/.env"
    )


def ask_dreamscape(question: str) -> dict:
    """Send a question to the Dreamscape FastAPI backend."""
    response = requests.post(
        API_URL,
        json={"question": question},
        timeout=180
    )

    response.raise_for_status()

    return response.json()