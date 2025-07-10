import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

model = SentenceTransformer("all-MiniLM-L6-v2")
index = faiss.read_index("./dataset/faiss.index")

with open("./dataset/chunks.json", "r", encoding="utf-8") as f:
    chunks = json.load(f)
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)
llm = genai.GenerativeModel("gemini-1.5-flash-latest")


def answer_question(query: str, k: int = 3) -> str:
    query_embedding = model.encode([query])

    D, I = index.search(np.array(query_embedding).astype(np.float32), k=3)

    retrieved_chunks = [chunks[idx]["content"] for idx in I[0]]
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You're an AI assistant helping users learn more about Zakaria Goumri.

Below is some background information. Use it to give a helpful, polite, and friendly response to the user's question.

--- CONTEXT ---
{context}
--- END CONTEXT ---

Now answer this question as if you're having a casual, respectful conversation:

{query}

Respond:
"""

    try:
        response = llm.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error calling Gemini: {e}"
