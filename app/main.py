from fastapi import FastAPI
from app.api.chat import router

app=FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def health():
  return {"status":"ok"}