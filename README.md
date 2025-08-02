# 🧠 LLM Long-Term Memory Agent

A conversational agent that augments OpenAI's GPT model with long-term memory using vector embeddings and ChromaDB. The system remembers facts from a user, retrieves them in future conversations, and can forget information on request — just like a real assistant.

---

## 📌 Features

- **Memory Addition**: Stores facts from the user (e.g., tools, preferences)
- **Memory Retrieval**: Retrieves relevant memory when asked
- **Memory Deletion**: Forgets memories on user command
- **OpenAI API**: Uses GPT-4 for dialogue and memory interpretation
- **ChromaDB**: Lightweight, local vector database to store and search embeddings
- **Modular Design**: Cleanly separated memory, GPT interface, and logic

---

## 🚀 Example Conversation

```text
LLM Memory Agent (type 'exit' to quit)
You: I use Shram and Magnet as productivity tools
Memory stored: I use Shram and Magnet as productivity tools
Retrieved context: ['i use shram and magnet as productivity tools.']
GPT: That's great! I'll remember that you use Shram and Magnet as your productivity tools. How can I assist you with them?

You: What are the productivity tools that I use?
Memory stored: what productivity tools do i use?
Retrieved context: ['what productivity tools do i use?', 'i use shram and magnet as productivity tools.']
GPT: You use Shram and Magnet as your productivity tools.

You: I don't use Magnet anymore
Memory stored: I don't use Magnet anymore.
Retrieved context: ["I don't use Magnet anymore.", 'i use shram and magnet as productivity tools.', 'what productivity tools do i use?']
GPT: You use Shram as your productivity tool.

You: What are the productivity tools that I use?
Memory stored: what productivity tools do i use?
Retrieved context: ['what productivity tools do i use?', 'i use shram and magnet as productivity tools.', "I don't use Magnet anymore."]
GPT: You use Shram as your productivity tool. You previously used Magnet, but you no longer use it.

```

## Project Structure
llm-longterm-memory-agent/
├── main.py                  # Main conversational loop
├── memory_store.py          # Memory storage, retrieval, deletion logic
├── openai_wrapper.py        # Handles calls to OpenAI APIs
├── extractor.py             # Extracts memories and deletion targets
├── .env                     # Stores your OpenAI API key
├── requirements.txt         # Pip dependencies
└── README.md                # This file

