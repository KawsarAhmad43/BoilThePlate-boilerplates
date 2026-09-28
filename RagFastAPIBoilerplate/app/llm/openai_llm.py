from langchain_openai import ChatOpenAI
from app.core.config import settings

def get_openai_llm():
    return ChatOpenAI(
        model_name=settings.LLM_MODEL_NAME, 
        openai_api_key=settings.OPENAI_API_KEY
    )
