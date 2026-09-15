import os
from pathlib import Path

import requests
from dotenv import load_dotenv


# Load .env from the same folder as this file
ENV_PATH = Path(__file__).parent / ".env"

load_dotenv(ENV_PATH)


API_URL = os.getenv("API_URL")


if not API_URL:
    raise RuntimeError(
        f"API_URL is not set. Make sure this file exists:\n{ENV_PATH}\n\n"
        "and contains:\n"
        "API_URL=http://127.0.0.1:8000/api/query"
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