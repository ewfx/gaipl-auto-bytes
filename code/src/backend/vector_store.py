import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

# Load pre-trained embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Load dataset (ensure "incidents.jsonl" exists)
data = []
with open("incidents.jsonl", "r") as file:
    for line in file:
        data.append(json.loads(line))

# Convert incidents into embeddings
texts = [f"{item['persona']} | {item['incident']} | {item['rca']} | {item['solution']}" for item in data]
embeddings = embedder.encode(texts)

# Create FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings))

# Save FAISS index
faiss.write_index(index, "incident_index.faiss")

# Save text data for retrieval
with open("incident_texts.json", "w") as f:
    json.dump(texts, f)

print("FAISS index created and stored successfully!")
