# memory_store.py

import chromadb
from chromadb.config import Settings
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Initialize ChromaDB
chroma_client = chromadb.Client(Settings(anonymized_telemetry=True))
collection = chroma_client.get_or_create_collection("memory")

EMBED_MODEL = "text-embedding-3-small"

def get_embedding(text: str) -> list:
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=[text]
    )
    return response.data[0].embedding

def add_memory(text: str):
    embedding = get_embedding(text)
    collection.add(documents=[text], embeddings=[embedding], ids=[text])

def retrieve_memories(query: str, n_results: int = 3):
    embedding = get_embedding(query)
    results = collection.query(query_embeddings=[embedding], n_results=n_results)
    return results["documents"][0] if results and results["documents"] else []
