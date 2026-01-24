from fastapi import FastAPI
from app.api.chat import router
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()

app.include_router(router, prefix="/api")

@app.get("/")
def health():
  return {"status":"ok"}

origins = [
    "http://localhost:5173",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/chat")
async def chat(message: dict):
  return {"reply": "Received: " + message.get("message", "")}