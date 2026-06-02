# Практика — M1-W01

Работаем в `projects/01-llm-gateway-fastapi/`. На этой неделе — только эксперименты, FastAPI будет на W02.

## Задание 1. Окружение
Создай структуру:
```
projects/01-llm-gateway-fastapi/
├── experiments/
├── prompts/
├── outputs/
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```
Требования:
- `.env.example` содержит `LLM_API_KEY=` и `LLM_BASE_URL=` (без реальных значений);
- реальный `.env` добавлен в `.gitignore`;
- `requirements.txt`: `httpx`, `python-dotenv`.

## Задание 2. Первый вызов LLM
Допиши `experiments/first_llm_call.py` (заготовка в `starter/first_llm_call.py`).
Критерии:
- API key читается из `.env` (никогда не хардкодим);
- prompt лежит отдельно в `prompts/first_prompt.md`;
- ответ сохраняется в `outputs/first_response.json` со структурой:
  `{ "prompt": "...", "model": "...", "answer": "...", "usage": {...} }`;
- в stdout/логах нет ключа.

## Задание 3. Temperature-эксперимент
Сделай 3 вызова с одинаковым промптом и temperature 0 / 0.5 / 1.
Запиши в `experiments/temperature_report.md`:
- сам промпт;
- 3 ответа;
- вывод: где ответ стабильнее, где разнообразнее, и где бы ты что использовал.

## Задание 4. Матрица выбора модели
Заполни `docs/product/model-decision-matrix.md` (шаблон уже в репозитории) минимум для 2 моделей, которые тебе доступны. Поля: модель · тип задачи · цена · latency · плюсы · минусы · когда использовать.

## Definition of Done
Все пункты `checklist.md` отмечены, PR открыт.
