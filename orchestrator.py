from fastapi import FastAPI
import requests
from upsert import upsert
from utils.dynamic_k import generate_k_value
from utils.search import search
app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.2:3b"

upsert()  # Upsert documents into the vector store on startup

# Load system prompt from file
with open("system.md", "r", encoding="utf-8") as f:
    SYSTEM_PROMPT = f.read()

@app.get("/ask")
def ask_question(question: str):
    try: 
        # 1. Retrieve relevant chunks
        k = generate_k_value(question)        
        results = search(question, k)
        
        context = "\n\n".join([
            r["chunk"] for r in results
        ])

        final_prompt = f"""
        Use the context below to answer the question.
        CONTEXT:
        {context}

        QUESTION:
        {question}

        Answer clearly and only use the context when relevant.
        """
        payload = {
            "model": MODEL,
            "prompt": final_prompt,
            "system": SYSTEM_PROMPT,
            "stream": False
        }

        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code != 200:
            return {
                "error": "Failed to reach Ollama",
                "details": response.text
            }

        data = response.json()
        grounding = True
        if "no mention of" in data.get("response") :
            grounding =False
        return {
            "answer": data.get("response"),
            "sources": [r["file"] for r in results],
            "grounding": grounding

        }
    except Exception as e:
        return {
            "error": "An error occurred",
            "details": str(e)
        }