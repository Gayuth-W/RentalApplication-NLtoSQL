from pydantic import BaseModel
from typing import Any, List

class ChatRequest(BaseModel):
  question: str
  session_id: str | None=None
  
class ChatResponse(BaseModel):
  answer: str
  sql: str
  rows: List[Any]