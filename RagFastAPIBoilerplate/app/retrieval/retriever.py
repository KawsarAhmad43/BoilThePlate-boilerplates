from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import FlashrankRerank
from app.database.vector_db import get_vector_store

def get_advanced_retriever():
    # step 1: get base vector retriever (fetch top 10 docs)
    vector_store = get_vector_store()
    base_retriever = vector_store.as_retriever(search_kwargs={"k": 10})
    
    # step 2: wrap it with flashrank to sort and pick the absolute best 3
    compressor = FlashrankRerank()
    compression_retriever = ContextualCompressionRetriever(
        base_compressor=compressor, 
        base_retriever=base_retriever
    )
    
    return compression_retriever
