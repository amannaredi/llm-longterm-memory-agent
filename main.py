# main.py

from memory_store import add_memory, retrieve_memories, delete_memory
from extractor import is_memory_worthy, extract_memory
from openai_wrapper import gpt_response
from openai_wrapper import extract_deletion_target

def chat():
    print("LLM Memory Agent (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        if is_memory_worthy(user_input):
            memory = extract_memory(user_input)
            add_memory(memory)
            print(f"Memory stored: {memory}")

        if "don't use" in user_input.lower() or "stop using" in user_input.lower():
            keyword = extract_deletion_target(user_input)
            deleted = delete_memory(keyword)
            if deleted:
                print(f"Memory deleted: {deleted}")
            else:
                print(f"No memory found related to: {keyword}")

        context = retrieve_memories(user_input)
        if context:
            print(f"Retrieved context: {context}")

        reply = gpt_response(user_input, "\n".join(context))
        print(f"GPT: {reply}")

if __name__ == "__main__":
    chat()
