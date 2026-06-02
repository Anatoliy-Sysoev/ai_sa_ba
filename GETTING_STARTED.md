# Как залить этот курс в свой GitHub

Этот архив — готовый git-репозиторий с историей коммитов. Я не могу запушить его в твой аккаунт (нет доступа), поэтому пушишь ты — 4 команды.

## Вариант 1: репозиторий ai_sa_ba уже создан на GitHub (пустой)
```bash
unzip ai_sa_ba.zip && cd ai_sa_ba
git remote add origin https://github.com/Anatoliy-Sysoev/ai_sa_ba.git
git push -u origin main
```

## Вариант 2: создать репозиторий через gh CLI
```bash
unzip ai_sa_ba.zip && cd ai_sa_ba
gh repo create Anatoliy-Sysoev/ai_sa_ba --public --source=. --remote=origin --push
```

## Нарезать задачи (issues + milestones)
После пуша, из корня репозитория:
```bash
gh auth login            # один раз
bash scripts/create_issues.sh Anatoliy-Sysoev/ai_sa_ba
```
Создаст 6 milestones (M1–M6) и 24 issue (W01–W24).

## Проверить прогресс в любой момент
```bash
python scripts/check_progress.py
```

## Сгенерировать наполнение следующей недели из шаблона
```bash
python scripts/create_week.py M2-W06-vector-db-qdrant "Qdrant vector search"
```
(папки-стабы уже есть; команда нужна, если захочешь пересоздать модуль по шаблону с полным набором файлов)

## Первый шаг обучения
Открой `modules/M1-W01-llm-basics/README.md` и иди по порядку: theory → practice → quiz → checklist → PR.
