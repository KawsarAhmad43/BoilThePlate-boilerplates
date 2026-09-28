import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # model options: ollama, openai, openrouter
    LLM_PROVIDER: str = "ollama"
    LLM_MODEL_NAME: str = "llama3"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OPENAI_API_KEY: str = ""
    OPENROUTER_API_KEY: str = ""
    
    # saving chroma data locally so it doesn't crash on other PCs
    CHROMA_PERSIST_DIRECTORY: str = os.path.join(os.getcwd(), "chroma_data")
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()
