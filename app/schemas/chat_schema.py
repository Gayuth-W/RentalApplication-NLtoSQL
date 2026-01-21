from pydantic import BaseModel
from typing import Any, List

class ChatRequest(BaseModel):
  question: str
  session_id: str | None=None
  
class ChatResponse(BaseModel):
  # answer: str
  sql: str
  # tables_used: List[Any]
<<<<<<< HEAD
  rows: List[Any]
=======
  # rows: List[Any]
>>>>>>> d96dea5 (fix: remove api key)
