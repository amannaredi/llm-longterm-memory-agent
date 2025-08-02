from memory_store import add_memory, retrieve_memories
from openai_wrapper import gpt_response, extract_deletion_target
from extractor import is_memory_worthy, is_deletion_intent, extract_memory

def chat():
    print("LLM Memory Agent (type 'exit' to quit)")
    deleted_items = []

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break

        # Handle memory-worthy input
        if is_memory_worthy(user_input):
            memory = extract_memory(user_input)
            add_memory(memory)
            print(f"✅ Memory stored: {memory}")

        # Handle semantic deletion
        if is_deletion_intent(user_input):
            deletion_target = extract_deletion_target(user_input)
            deleted_items.append(deletion_target)
            print(f"🧠 Noted deletion: {deletion_target}")

        # Get relevant context
        context = retrieve_memories(user_input)
        if context:
            print(f"🧠 Retrieved context: {context}")

        # Call GPT with context + deletions
        reply = gpt_response(user_input, context, deleted_items)
        print(f"GPT: {reply}")

if __name__ == "__main__":
    chat()
