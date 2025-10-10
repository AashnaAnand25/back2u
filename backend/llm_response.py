# backend/llm_response.py
from groq import Groq
from backend.rag_pipeline import create_vector_store, retrieve_relevant
import os

def generate_response(user_query):
    """Uses RAG + Groq LLaMA 3 model to generate an answer."""
    db = create_vector_store()
    relevant_chunks = retrieve_relevant(user_query, db)
    context = "\n".join(relevant_chunks)

    prompt = f"""
    You are an AI mentor representing the user's future self.
    Using the following context from their past experiences, give a motivating and actionable answer.

    Context:
    {context}

    User's question:
    {user_query}

    Future-Self Response:
    """

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    return response.choices[0].message.content.strip()