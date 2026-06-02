"""M1-W02 — пример тестов. LLM замокан, в сеть не ходим."""
from unittest.mock import patch
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_ask_ok():
    fake = {"answer": "RAG ищет в данных, fine-tune меняет веса.", "model": "test", "tokens": 42}
    with patch("src.llm_client.call_llm", return_value=fake):
        r = client.post("/ask", json={"question": "RAG vs fine-tune?"})
    assert r.status_code == 200
    body = r.json()
    assert set(body) == {"answer", "model", "tokens"}
    assert body["tokens"] == 42


def test_ask_empty_question_422():
    r = client.post("/ask", json={"question": ""})
    assert r.status_code == 422
