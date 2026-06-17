import os
from src.utils.vector_store import get_index, get_metadatas_store
from src.utils.embedder import embed
from src.utils.chunk_text import chunk_text
import numpy as np

def load_corpus(folder="corpus"):
    docs = []

    for file in os.listdir(folder):
        if file.endswith(".md"):
            with open(os.path.join(folder, file), "r", encoding="utf-8") as f:
                docs.append({
                    "file": file,
                    "text": f.read()
                })

    return docs


def upsert():
    docs = load_corpus()
    index= get_index()
    metadata_store = get_metadatas_store()
    for doc in docs:
        chunks = chunk_text(doc["text"], 2000, 300)

        for chunk in chunks:
            vector = embed(chunk)
            
            index.add(vector)
            metadata_store.append({
                "file": doc["file"],
                "chunk": chunk
            })

    print(f"Upserted {len(metadata_store)} chunks")

