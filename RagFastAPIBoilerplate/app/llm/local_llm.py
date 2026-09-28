from langchain_community.chat_models import ChatOllama
from app.core.config import settings

def get_local_llm():
    return ChatOllama(
        model=settings.LLM_MODEL_NAME, 
        base_url=settings.OLLAMA_BASE_URL
    )
