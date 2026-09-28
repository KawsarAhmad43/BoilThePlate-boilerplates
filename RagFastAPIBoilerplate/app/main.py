from fastapi import FastAPI
from app.api import chat

app = FastAPI(title="Model Agnostic RAG API")
# plugging in the chat router
app.include_router(chat.router)

@app.get("/")
def read_root():
    return {"message": "RAG API is running!"}
