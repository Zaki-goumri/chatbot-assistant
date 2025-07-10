import faiss
import json
import numpy as np


with open("./dataset/chunks.json", "r", encoding="utf-8") as f:
    data = json.load(f)

embeddings = np.array([item["embedding"] for item in data], dtype="float32")
metadata = [{"source": item["source"], "content": item["content"]}
            for item in data]

faiss.normalize_L2(embeddings)
dimension = embeddings.shape[1]
index = faiss.IndexFlatIP(dimension)

index.add(embeddings)

faiss.write_index(index, "./dataset/faiss.index")
with open("./dataset/metadat.json", "w", encoding="utf-8") as f:
    json.dump(metadata, f, indent=2)

print("FAISS index and metadata saved.")
