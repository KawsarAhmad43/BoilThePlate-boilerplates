from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_openai import OpenAIEmbeddings
from app.core.config import settings

def get_embeddings():
    # easy toggle between local free embeddings or paid openai ones
    provider = settings.LLM_PROVIDER.lower()
    
    if provider == "openai":
        return OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
    else:
        # fallback to local huggingface for everything else (ollama, openrouter)
        return HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
