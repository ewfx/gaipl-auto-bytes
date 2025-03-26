from fastapi import FastAPI
from pydantic import BaseModel
import ollama
import faiss
import json
import numpy as np
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Define system prompts for different personas
PERSONA_PROMPTS = {
    "os_support": "You are an expert OS support engineer. Provide detailed solutions for OS-related issues.",
    "db_support": "You are a database administrator. Answer only database-related queries with precise RCA and solutions.",
    "network_support": "You are a network engineer. Solve network connectivity and security issues.",
    "hardware_support": "You are a hardware technician. Provide troubleshooting steps for hardware failures.",
    "storage_support": "You are a storage engineer. Help with storage-related issues and configurations."
}

# Load FAISS index and texts
index = faiss.read_index("incident_index.faiss")
with open("incident_texts.json", "r") as f:
    stored_texts = json.load(f)

# Load embedding model
embedder = SentenceTransformer("all-MiniLM-L6-v2")

class IncidentRequest(BaseModel):
    persona: str
    incident: str

def retrieve_similar_incident(query):
    query_embedding = embedder.encode([query])
    _, indices = index.search(np.array(query_embedding), 1)
    return stored_texts[indices[0][0]]

@app.post("/analyze")
async def analyze_incident(request: IncidentRequest):
    # Retrieve similar incident
    similar_incident = retrieve_similar_incident(request.incident)

    # Prepare system prompt
    system_prompt = PERSONA_PROMPTS.get(request.persona, "You are a general IT support agent.")
    
    # Format input with retrieved knowledge
    input_text = f"Persona: {request.persona} | Incident: {request.incident} | Similar case: {similar_incident}"
    
    # Call Ollama
    response = ollama.chat(model="llama3", messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": input_text}
    ])

    return {"response": response["message"]["content"]}

# Run the server: uvicorn app:app --reload
