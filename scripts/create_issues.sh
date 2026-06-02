#!/usr/bin/env bash
# Создаёт milestones и 24 issue в твоём репозитории через GitHub CLI.
# Требуется установленный и авторизованный gh: https://cli.github.com/
#   gh auth login
# Запуск из корня репозитория:
#   bash scripts/create_issues.sh Anatoliy-Sysoev/ai_sa_ba
set -euo pipefail
REPO="${1:?Укажи репозиторий, напр.: Anatoliy-Sysoev/ai_sa_ba}"

echo "Создаю milestones..."
for m in \
  "M1 — LLM Foundation + FastAPI" \
  "M2 — RAG + Documents" \
  "M3 — Agents + LangGraph" \
  "M4 — Production + Observability" \
  "M5 — Product + Security + FinOps" \
  "M6 — Capstone + Portfolio"; do
  gh api "repos/$REPO/milestones" -f title="$m" >/dev/null 2>&1 || echo "  milestone '$m' уже есть"
done

# week|milestone-number|title
while IFS='|' read -r week ms title; do
  [ -z "$week" ] && continue
  gh issue create --repo "$REPO" \
    --title "[$week] $title" \
    --label "learning" \
    --milestone "$(gh api repos/$REPO/milestones --jq ".[$((ms-1))].title")" \
    --body "См. modules/. Закрой неделю через PR с артефактом. Гейт — в README модуля." \
    >/dev/null && echo "issue [$week] создан"
done <<'ROWS'
W01|1|LLM basics
W02|1|FastAPI gateway
W03|1|Structured output + tool calling
W04|1|Monthly exam: LLM gateway
W05|2|RAG indexing
W06|2|Qdrant vector search
W07|2|RAG API
W08|2|RAG eval
W09|3|LangGraph basics
W10|3|ReAct / Plan-Execute
W11|3|Human-in-the-loop
W12|3|Monthly exam: agents
W13|4|Observability
W14|4|Eval + cost/latency
W15|4|Production hardening
W16|4|Monthly exam: production
W17|5|AI use case scoring
W18|5|Security / PII
W19|5|ROI / FinOps
W20|5|Monthly exam: product
W21|6|Capstone design
W22|6|Capstone implementation
W23|6|Capstone eval + demo
W24|6|Portfolio + interview
ROWS
echo "Готово."
