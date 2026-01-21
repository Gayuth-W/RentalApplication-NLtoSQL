from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.chains.sql_chains import run_nl2sql

router =APIRouter()

@router.post("/chat", response_model=ChatResponse)
def nl2sql_endpoint(payload: ChatRequest):
  
  result = run_nl2sql(
    question=payload.question,
    session_id=payload.session_id
  )  
  return result