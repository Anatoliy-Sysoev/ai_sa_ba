"""Вызов провайдера. В тестах эта функция мокается."""
import os
import httpx

BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")
MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")
API_KEY = os.environ.get("LLM_API_KEY", "")


def call_llm(question: str, temperature: float = 0.0) -> dict:
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {"model": MODEL, "messages": [{"role": "user", "content": question}], "temperature": temperature}
    resp = httpx.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    data = resp.json()
    return {
        "answer": data["choices"][0]["message"]["content"],
        "model": MODEL,
        "tokens": data.get("usage", {}).get("total_tokens", 0),
    }
