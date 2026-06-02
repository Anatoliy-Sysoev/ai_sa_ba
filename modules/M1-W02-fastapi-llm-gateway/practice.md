# Практика — M1-W02

Развиваем `projects/01-llm-gateway-fastapi/`. Заготовка приложения — в `starter/`.

## Задание 1. Структура приложения
```
projects/01-llm-gateway-fastapi/
├── src/
│   ├── main.py        # FastAPI app, эндпоинты
│   ├── models.py      # Pydantic-модели
│   └── llm_client.py  # вызов провайдера (из W01, причёсанный)
├── tests/
│   └── test_api.py
├── requirements.txt   # + fastapi, uvicorn, pytest
└── README.md
```

## Задание 2. Эндпоинты
- `GET /health` -> `{"status": "ok"}`.
- `POST /ask` принимает `AskRequest`, вызывает `llm_client`, возвращает `AskResponse`.

## Задание 3. Тесты (LLM замокан!)
В `tests/test_api.py` минимум 3 теста:
1. `/health` отвечает 200 и `{"status":"ok"}`.
2. `/ask` с замоканным llm_client возвращает корректную схему `AskResponse`.
3. `/ask` с пустым `question` отдаёт 422 (валидация Pydantic).

Подсказка: используй `unittest.mock.patch` на `llm_client.call_llm` или `monkeypatch`, чтобы тест не ходил в сеть.

## Задание 4. Экспорт контракта
Запусти сервис, открой `/openapi.json`, сохрани в `docs/openapi/llm-gateway.yaml` (или .json). Это артефакт-контракт.

## Запуск
```bash
pip install -r requirements.txt
uvicorn src.main:app --reload
# открой http://127.0.0.1:8000/docs
pytest -q
```

## Definition of Done
Все пункты `checklist.md` отмечены, PR открыт.
