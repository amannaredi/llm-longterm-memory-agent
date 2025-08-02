
def is_memory_worthy(message: str) -> bool:
    triggers = ["i use", "i like", "i don't use", "my favourite", "i prefer"]
    return any(trigger in message.lower() for trigger in triggers)

def extract_memory(message: str) -> str:
    return message.strip()
