from langchain_openai import ChatOpenAI
from app.core.config import settings

def get_openrouter_llm():
    return ChatOpenAI(
        model_name=settings.LLM_MODEL_NAME,
        openai_api_key=settings.OPENROUTER_API_KEY,
        openai_api_base="https://openrouter.ai/api/v1"
    )
