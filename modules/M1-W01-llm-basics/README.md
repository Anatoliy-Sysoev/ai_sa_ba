# M1-W01 — Основы LLM и первый вызов модели

> Статус: 🔲 не начат · Приоритет: P0 · Трек: LLM · Оценка времени: 10–12 ч

## Цель недели
Понять практические ограничения LLM глазами архитектора (не математику трансформеров) и сделать первый воспроизводимый вызов модели через Python с сохранением результата в структурированном виде.

## Что нужно понять (теория → `theory.md`)
- Токены и почему «просто засунуть документ в модель» не работает.
- Context window, temperature, детерминизм.
- Откуда берутся галлюцинации и почему для бизнеса нужен structured output + источники.
- Разница prompt vs context.

## Что нужно сделать (практика → `practice.md`)
1. Поднять Python-проект `projects/01-llm-gateway-fastapi/`.
2. Сделать первый вызов LLM API, сохранить ответ в JSON.
3. Эксперимент с temperature (0 / 0.5 / 1) + отчёт.
4. Заполнить `docs/product/model-decision-matrix.md`.

## Артефакты недели (→ `artifacts.md`)
- `projects/01-llm-gateway-fastapi/experiments/first_llm_call.py`
- `projects/01-llm-gateway-fastapi/experiments/temperature_report.md`
- `docs/product/model-decision-matrix.md`
- `assessments/weekly/W01.md`

## Гейт недели (зачёт)
- [ ] код запускается;
- [ ] секреты не в git (есть `.env.example`, реальный `.env` в `.gitignore`);
- [ ] ответ сохраняется в JSON;
- [ ] `temperature_report.md` написан;
- [ ] `quiz.md` пройден >= 80%;
- [ ] `assessments/weekly/W01.md` заполнен с self-score 0-4.

## Порядок прохождения
`theory.md` -> `resources.md` -> `practice.md` -> `starter/` -> `tests.md` -> `quiz.md` -> `checklist.md` -> `solution-notes.md`
