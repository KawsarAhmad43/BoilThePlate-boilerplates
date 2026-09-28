from app.core.config import settings
from app.llm.local_llm import get_local_llm
from app.llm.openai_llm import get_openai_llm
from app.llm.openrouter_llm import get_openrouter_llm

def get_llm():
    provider = settings.LLM_PROVIDER.lower()
    
    if provider == "openai":
        return get_openai_llm()
    elif provider == "openrouter":
        return get_openrouter_llm()
    elif provider == "ollama" or provider == "local":
        return get_local_llm()
    else:
        raise ValueError(f"Invalid LLM_PROVIDER in config: {provider}")
