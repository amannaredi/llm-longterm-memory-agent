from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def gpt_response(user_input: str, memory_context: list, deletions: list = None) -> str:
    system_msg = (
        "You are a helpful assistant with long-term memory. "
        "Use user memory to answer questions, but respect deletion notes. "
        "If a user has said they no longer use something, do not include it."
    )

    memory_summary = "\n".join(memory_context)
    forget_note = f"\nForget the following: {', '.join(deletions)}" if deletions else ""

    messages = [
        {"role": "system", "content": system_msg},
        {"role": "user", "content": f"Memory:\n{memory_summary}{forget_note}\n\nUser: {user_input}"}
    ]

    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()


def extract_deletion_target(user_input: str) -> str:
    messages = [
        {"role": "system", "content": "Extract the concept or item the user wants to forget."},
        {"role": "user", "content": f"Sentence: '{user_input}' — only return what to forget."}
    ]
    response = client.chat.completions.create(
        model="gpt-4",
        messages=messages,
        temperature=0
    )
    return response.choices[0].message.content.strip()
