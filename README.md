# LLM Long-Term Memory Agent

A memory-augmented chatbot system built with OpenAI's GPT-4 and ChromaDB, designed to **store**, **retrieve**, and **forget** user-specific information semantically across interactions.

---

## Features

- **Semantic Memory Detection**: Automatically determines if a message contains information worth remembering using GPT.
- **Contextual Retrieval**: Fetches semantically similar past memories for the current user query.
- **Forget Mechanism**: If a user expresses deletion intent (e.g., “I don’t use Magnet”), it is tracked and excluded from responses.
- **Conversation-Aware Responses**: GPT-4 uses memory and deletions to generate accurate, privacy-respecting replies.
- **Embedding-based Memory Storage**: Uses `text-embedding-3-small` model and ChromaDB for vector search.

---

---

## Example Conversation

```
LLM Memory Agent (type 'exit' to quit)
You: I use Shram and Magnet as productivity tools
Memory stored: I use Shram and Magnet as productivity tools.
Retrieved context: ['I use Shram and Magnet as productivity tools.']
GPT: Sure, I have noted that you use Shram and Magnet as your productivity tools. How can I assist you with them?

You: What productivity tools do I use. 
Retrieved context: ['I use Shram and Magnet as productivity tools.']
GPT: You use Shram and Magnet as your productivity tools.

You: I don't use Magent anymore.
Memory stored: I don't use Magent anymore.
Noted deletion: Magent
Retrieved context: ["I don't use Magent anymore.", 'I use Shram and Magnet as productivity tools.']
GPT: Understood, you no longer use Magent. You currently use Shram and Magnet as your productivity tools.

You: What productivity tools do I use?
Retrieved context: ['I use Shram and Magnet as productivity tools.', "I don't use Magent anymore."]
GPT: You use Shram as a productivity tool.

```

## Project Structure
```
llm-longterm-memory-agent/
│
├── main.py             # Conversation loop
├── memory_store.py     # ChromaDB memory operations
├── openai_wrapper.py   # GPT logic and deletion target extraction
├── extractor.py        # Semantic memory/deletion intent checks
├── .env                # OpenAI API key (not pushed!)
├── requirements.txt    # Python dependencies
├── environment.yml     # Conda environment (optional)
└── README.md
```

## Getting Started

### 1. Clone the repository

```
git clone https://github.com/amannaredi/llm-longterm-memory-agent.git
cd llm-longterm-memory-agent
```
### 2. Set up environment
```
conda env create -f environment.yml
conda activate llm-memory
```
### 3. Add your OpenAI API key
```
Create a .env file:
OPENAI_API_KEY=sk-XXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Run the chatbot:
```
python main.py
```
### You'll see:
```
LLM Memory Agent (type 'exit' to quit)
You:
```
Type messages like:

- I use Notion and Trello for productivity.

- What do I use for productivity?

- I don’t use Trello anymore.

- What do I use for productivity now?

The bot will remember, forget, and respond accordingly.

## How It Works
Component	Purpose
 - **is_memory_worthy()**	Uses GPT to determine if input should be saved
 - **add_memory()**	Saves input as an embedding in ChromaDB
 - **retrieve_memories()**	Returns most relevant past messages
 - **is_deletion_intent()**	Uses GPT to semantically detect deletion
 - **extract_deletion_target()**	Extracts what to forget from user message
 - **gpt_response()**	Combines user query + memory + forget notes for GPT-4 response

## Requirements
 - Python 3.8+
 - openai
 - chromadb
 - python-dotenv

## Powered By
 - OpenAI GPT-4
 - ChromaDB
 - text-embedding-3-small

## Future Improvements
Here are some ways this project can be further improved:

**1. Persistent Memory Storage**
Currently, memory exists only in-memory and is lost when the app exits. To support real long-term memory:

Enable persistent storage in ChromaDB using persist_directory and chroma_client.persist().

This would allow memories to persist across sessions and system restarts.

**2. Smarter Memory Management**
To avoid bloating the memory with irrelevant information:

Implement memory deduplication to prevent storing repeated facts.

Introduce a relevance score or decay mechanism to phase out less useful memories over time.

**3. Improved Context Retrieval**
Currently, we retrieve top-N similar memories. This can be made more intelligent by:

Fine-tuning similarity scoring (e.g., weighted embeddings or hybrid retrieval with keywords).

Using user intent classification to determine when to search memory.

**4. Smarter Deletion Logic**
Instead of soft deletion via GPT filtering, you can:

Implement soft tags (e.g., “deprecated”) on documents and filter them during retrieval.

Allow GPT to not just mark but semantically rewrite outdated memories.

**5. Web or Chatbot Interface**
Integrate the memory agent into:

A Streamlit or Flask web app for interactive demos.

Messaging platforms like Slack, Telegram, or Discord via their respective APIs.

