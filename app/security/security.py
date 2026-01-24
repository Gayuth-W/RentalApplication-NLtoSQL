# from fastapi import FastAPI
# from fastapi.middleware.cors import CORSMiddleware

# app = FastAPI()

# # Allowed origins
# origins = [
#     "http://localhost:5173",  # your React frontend
#     "http://localhost:8000",
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],  # allow GET, POST, OPTIONS, etc.
#     allow_headers=["*"],
# )

# # Your chat endpoint
# @app.post("/api/chat")
# async def chat(message: dict):
#     return {"reply": "Received: " + message.get("message", "")}