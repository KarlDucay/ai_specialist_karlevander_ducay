import numpy as np
from utils.embedder import embed
from utils.vector_store import get_index, get_metadatas_store

def search(query, k=3):
    query_vec = embed(query)
    
    index = get_index()
    metadata_store = get_metadatas_store()  
    
    indices = index.search(query_vec, k)

    results = []
    for i in indices[0]:
        if i < len(metadata_store):
            results.append(metadata_store[i])

    return results