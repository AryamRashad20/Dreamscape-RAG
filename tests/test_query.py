from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_query_happy_path(monkeypatch):
    """Test that a valid question returns an answer and sources."""

    monkeypatch.setattr(
        "backend.app.api.routes.query.retrieve_chunks",
        lambda question: [
            {
                "score": 0.9,
                "source": "locations.txt",
                "chunk_id": 1,
                "text": "The Crystal Caverns are located beneath the eastern mountains."
            }
        ]
    )

    monkeypatch.setattr(
        "backend.app.api.routes.query.generate_answer",
        lambda question, chunks:
            "The Crystal Caverns are located beneath the eastern mountains."
    )

    response = client.post(
        "/api/query",
        json={"question": "Where are the Crystal Caverns located?"}
    )

    assert response.status_code == 200

    data = response.json()

    assert "answer" in data
    assert "sources" in data
    assert "locations.txt" in data["sources"]


def test_query_empty_question():
    """Test that an empty question is rejected."""

    response = client.post(
        "/api/query",
        json={"question": ""}
    )

    assert response.status_code == 422