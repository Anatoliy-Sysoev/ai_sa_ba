"""M1-W02 starter — FastAPI gateway. Допиши TODO."""
from fastapi import FastAPI, HTTPException
from .models import AskRequest, AskResponse
from . import llm_client

app = FastAPI(title="LLM Gateway", version="0.1.0")


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/ask", response_model=AskResponse)
def ask(req: AskRequest) -> AskResponse:
    try:
        result = llm_client.call_llm(req.question, temperature=req.temperature)
    except Exception:
        # TODO: залогировать без утечки секретов
        raise HTTPException(status_code=502, detail="LLM provider error")
    return AskResponse(answer=result["answer"], model=result["model"], tokens=result["tokens"])
