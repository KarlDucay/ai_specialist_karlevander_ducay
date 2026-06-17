import faiss
import numpy as np

dimension = 768  # nomic-embed-text = 768 dims
index = faiss.IndexFlatL2(dimension)

metadata_store = []

def get_metadatas_store():
    return metadata_store

def add(vector):
    v = np.array([vector]).astype("float32")
    index.add(v)

def get_index():
    return index