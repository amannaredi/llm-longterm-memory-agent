import chromadb
from chromadb.config import Settings
import openai
import os
from dotenv import load_dotenv
import logging
from openai import OpenAI

# Load .env and API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI()
# Silence telemetry warning
logging.getLogger("chromadb").setLevel(logging.ERROR)

# Create ChromaDB client
chroma_client = chromadb.Client(Settings(anonymized_telemetry=True))
collection = chroma_client.get_or_create_collection("memory")

# Define model name as a string
EMBED_MODEL = "text-embedding-3-small"

# Fix type hint: model is str, not EMBED_MODEL (which doesn't exist yet at that point)
def get_embedding(text: str, model: str = EMBED_MODEL) -> list:
    response = client.embeddings.create(
        input=[text],
        model=model
    )
    return response.data[0].embedding

def add_memory(text: str):
    embedding = get_embedding(text)
    collection.add(documents=[text], embeddings=[embedding], ids=[text])

def retrieve_memories(query: str, n_results: int = 3):
    embedding = get_embedding(query)
    results = collection.query(query_embeddings=[embedding], n_results=n_results)
    return results["documents"][0] if results and results["documents"] else []

def delete_memory(keyword: str):
    all_items = collection.get()
    to_delete = [doc_id for doc_id in all_items["ids"] if keyword.lower() in doc_id.lower()]
    if to_delete:
        collection.delete(ids=to_delete)
        return to_delete
    return []
