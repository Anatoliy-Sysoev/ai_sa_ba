"""
M1-W01 starter — первый вызов LLM.
Заготовка. Допиши помеченные TODO. Провайдер-независимо: работает с любым
OpenAI-совместимым HTTP API (OpenAI, локальный Ollama, и т.п.).

Запуск:
    cp .env.example .env   # впиши свои значения
    pip install -r requirements.txt
    python experiments/first_llm_call.py
"""
import os
import json
import pathlib
import httpx
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.environ.get("LLM_API_KEY", "")
BASE_URL = os.environ.get("LLM_BASE_URL", "https://api.openai.com/v1")
MODEL = os.environ.get("LLM_MODEL", "gpt-4o-mini")

PROMPT_FILE = pathlib.Path("prompts/first_prompt.md")
OUT_FILE = pathlib.Path("outputs/first_response.json")


def load_prompt() -> str:
    # TODO: прочитать промпт из PROMPT_FILE и вернуть текст
    return PROMPT_FILE.read_text(encoding="utf-8")


def call_llm(prompt: str, temperature: float = 0.0) -> dict:
    """Один вызов chat-completions. Возвращает сырой ответ API (dict)."""
    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": temperature,
    }
    # TODO: сделать POST на {BASE_URL}/chat/completions, вернуть resp.json()
    resp = httpx.post(f"{BASE_URL}/chat/completions", headers=headers, json=payload, timeout=60)
    resp.raise_for_status()
    return resp.json()


def main() -> None:
    assert API_KEY, "LLM_API_KEY пуст — заполни .env (см. .env.example)"
    prompt = load_prompt()
    raw = call_llm(prompt, temperature=0.0)

    # TODO: вытащить текст ответа и usage из raw
    answer = raw["choices"][0]["message"]["content"]
    usage = raw.get("usage", {})

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(
        json.dumps(
            {"prompt": prompt, "model": MODEL, "answer": answer, "usage": usage},
            ensure_ascii=False,
            indent=2,
        ),
        encoding="utf-8",
    )
    # НИКОГДА не печатаем API_KEY. Только результат:
    print("answer:", answer[:300])
    print("tokens:", usage)


if __name__ == "__main__":
    main()
