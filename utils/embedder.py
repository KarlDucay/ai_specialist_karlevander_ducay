import requests
import numpy as np


EMBED_MODEL = "nomic-embed-text"

def embed(text: str):
    res = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": text
        }
    )

    vec = res.json()["embedding"]

    return np.array(vec, dtype="float32").reshape(1, -1)