from langchain_community.vectorstores import Chroma
from app.embeddings.factory import get_embeddings
from app.core.config import settings

def get_vector_store():
    # using our flexible embedding factory now!
    embeddings = get_embeddings()
    return Chroma(
        persist_directory=settings.CHROMA_PERSIST_DIRECTORY,
        embedding_function=embeddings
    )
