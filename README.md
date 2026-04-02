# Fine-Tuned-RAG-Chatbot-with-Streaming-Responses
This project is a Retrieval-Augmented Generation (RAG) system that allows users to query PDFs using a Streamlit-based chat interface. It uses LangChain, OpenAI embeddings, and ChromaDB for efficient document retrieval.

## Features
- Chat-based interface using Streamlit
- PDF document processing
- Semantic search using embeddings
- Fast retrieval with ChromaDB
- LLM-powered responses



## Project Structure
Amlgo project/
│── app.py
│── requirements.txt
│── .env
│── src/
│   ├── pipeline.py
│   ├── retriever.py
│   └── generator.py
│── chunks/
│   └── embedded_text.py



## Tech Stack
- Python
- Streamlit
- LangChain
- OpenAI API
- ChromaDB


🔹 Embedding Model

We use OpenAI’s text-embedding-3-large model for generating vector representations of text.

Why this model?
	•	High-quality semantic understanding of text
	•	Captures contextual meaning better than traditional methods
	•	Works well for document retrieval tasks (RAG)
	•	Optimized for similarity search in vector databases like ChromaDB

Role in the system:
	•	Converts PDF chunks into embeddings
	•	Converts user queries into embeddings
	•	Enables efficient similarity search between query and stored documents


🔹 Instructions to run the chatbot with streaming response enabled

Step 1: Activate Virtual Environment
       source venv/bin/activate


Step 2: Run the Streamlit App
       streamlit run app.py

Step 3: Use the Chat Interface
	•	Enter your query in the chat input
	•	The response will be streamed in real-time
	•	Relevant context is retrieved from your documents automatically

Implementation video link ---- https://drive.google.com/file/d/19kBAX8kWNjrC3AdF2-_CYEFXKX5IbPBQ/view?usp=sharing

Githiub repository url ---- https://github.com/Rabbani2001/Fine-Tuned-RAG-Chatbot-with-Streaming-Responses.git
