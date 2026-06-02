# Checklist — M1-W02

- [ ] Ветка `feature/m1-w02-fastapi-llm-gateway`
- [ ] `/health` -> 200 `{"status":"ok"}`
- [ ] `/ask` принимает Pydantic-запрос, возвращает Pydantic-ответ
- [ ] LLM-вызов вынесен в `llm_client.py`
- [ ] ≥3 pytest зелёные, LLM замокан
- [ ] Секреты из `.env`, не в коде
- [ ] OpenAPI экспортирован в `docs/openapi/`
- [ ] Quiz ≥80%
- [ ] `assessments/weekly/W02.md` заполнен (self-score 0–4)
- [ ] PR открыт, issue закрыта
