from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_response(user_input: str, memory_context: str) -> str:
    system_msg = "You are an assistant with long-term memory of user facts."
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": f"Memory: {memory_context}\n\nUser: {user_input}"}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def extract_deletion_target(user_input: str) -> str:
    system_msg = "You are an assistant that extracts what the user wants to forget from their sentence."
    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": f"Extract the thing to forget from: '{user_input}'. Only return the name/phrase, nothing else."}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip()
