import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_answer(query, contexts):
    context_text = "\n\n".join(contexts)

    prompt = f"""
You are an intelligent AI assistant.

Answer the user's question using only the context below.
Give a short, clear answer in simple English.
If the context has partial information, answer from that.
Only say "Not enough information" if the context is completely unrelated.

Context:
{context_text}

Question:
{query}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content