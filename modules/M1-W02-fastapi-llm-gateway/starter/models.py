from pydantic import BaseModel, Field


class AskRequest(BaseModel):
    question: str = Field(min_length=1)
    temperature: float = 0.0


class AskResponse(BaseModel):
    answer: str
    model: str
    tokens: int
