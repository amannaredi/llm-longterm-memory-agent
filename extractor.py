from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def is_memory_worthy(message: str) -> bool:
    """
    Use GPT to determine whether the message contains factual or preference-based information worth storing.
    """
    messages = [
        {
            "role": "system",
            "content": "You are an assistant that decides if a user message contains factual, preference, or interest-related information that should be stored in memory. Reply with only 'yes' or 'no'."
        },
        {
            "role": "user",
            "content": f"Should this be remembered: '{message}'?"
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip().lower() == "yes"

def is_deletion_intent(message: str) -> bool:
    """
    Use GPT to semantically determine if the user's message implies forgetting or removing a memory.
    """
    messages = [
        {
            "role": "system",
            "content": "You're an assistant that determines whether the user wants to forget or delete something. Reply with only 'yes' or 'no'."
        },
        {
            "role": "user",
            "content": f"Does this mean the user wants to delete something: '{message}'?"
        }
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip().lower() == "yes"

def extract_memory(message: str) -> str:
    """
    Return the message itself as the memory content.
    """
    return message.strip()

