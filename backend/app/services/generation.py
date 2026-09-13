import ollama

from backend.app.core.config import settings


def create_prompt(question: str, retrieved_chunks: list[dict]) -> str:
    """Build a grounded prompt using retrieved Dreamscape context."""

    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"[Source {i}: {chunk['source']}, "
            f"Chunk {chunk['chunk_id']}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are the Dreamscape knowledge assistant.

Answer the user's question using ONLY the information provided
in the retrieved Dreamscape context below.

Rules:
1. Do not invent or assume facts.
2. Do not use outside knowledge.
3. If the context does not contain enough information, say:
   "I don't have enough information in the Dreamscape knowledge base
   to answer that question."
4. Give a clear and concise answer.
5. At the end, list the source files used.

Retrieved Context:
------------------
{context}
------------------

User Question:
{question}

Answer:
"""

    return prompt


def generate_answer(question: str, retrieved_chunks: list[dict]) -> str:
    """Generate a grounded answer using the local Ollama model."""

    prompt = create_prompt(question, retrieved_chunks)

    response = ollama.chat(
        model=settings.OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]