import ollama
from backend.app.core.config import settings


INSUFFICIENT_INFO = (
    "I don't have enough information in the Dreamscape knowledge base "
    "to answer that question."
)


def create_prompt(question: str, retrieved_chunks: list[dict]) -> str:
    context_parts = []

    for i, chunk in enumerate(retrieved_chunks, start=1):
        context_parts.append(
            f"[Source {i}: {chunk['source']}, "
            f"Chunk {chunk['chunk_id']}]\n"
            f"{chunk['text']}"
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are a strict knowledge-base assistant for the fictional world Dreamscape.

You MUST answer using ONLY the retrieved context.

RULES:
- Use only information explicitly written in the context.
- Never invent facts.
- Never add names, places, kingdoms, characters, events, objects,
  abilities, or relationships that are not written in the context.
- Never use knowledge from other fictional worlds.
- Do not guess.
- If the answer is not supported by the context, say:
  "{INSUFFICIENT_INFO}"
- Keep the answer short: 1 to 3 sentences.
- Do not include sources in your answer.
- The application will display the sources separately.

Before answering, silently check that every factual statement
you make is supported by the retrieved context.

RETRIEVED CONTEXT:
==================
{context}
==================

QUESTION:
{question}

ANSWER:
"""

    return prompt


def generate_answer(question: str, retrieved_chunks: list[dict]) -> str:
    prompt = create_prompt(question, retrieved_chunks)

    response = ollama.chat(
        model=settings.OLLAMA_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        options={
            "temperature": 0
        }
    )

    answer = response["message"]["content"].strip()

    return answer