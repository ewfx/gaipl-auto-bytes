# 🚀 Project Name

## 📌 Table of Contents
- [Introduction](#introduction)
- [Demo](#demo)
- [Inspiration](#inspiration)
- [What It Does](#what-it-does)
- [How We Built It](#how-we-built-it)
- [Challenges We Faced](#challenges-we-faced)
- [How to Run](#how-to-run)
- [Tech Stack](#tech-stack)
- [Team](#team)

---

## 🎯 Introduction
This project is an AI-powered IT Support Chatbot designed to provide expert technical assistance across multiple domains, including OS support, database management, networking, hardware troubleshooting, and storage management. The chatbot utilizes Ollama for natural language processing, FAISS for efficient retrieval of past incidents, and Gradio for an interactive web-based UI.

## 🎥 Demo
🔗 [Live Demo](#) (if applicable)  
📹 [artifacts\demo\DB_persona.mp4](#) (if applicable)  
🖼️ Screenshots:
![Screenshot 1](artifacts\demo\DB_support.png)
![Screenshot 2](artifacts\demo\OS_support.png)

## 💡 Inspiration
The project was inspired by the challenges IT support teams face in handling frequent and recurring incidents. Automating responses and leveraging historical data can significantly reduce resolution times, improve accuracy, and optimize IT operations.

## ⚙️ What It Does
Provides expert assistance across multiple IT domains.

Uses Ollama for intelligent query processing.

Retrieves relevant past incidents using FAISS for enhanced accuracy.

Displays responses interactively via a Gradio web UI.

Supports multiple personas for domain-specific assistance.

## 🛠️ How We Built It
Data Preparation: Compiled past incident reports in JSONL format.

Vector Storage: Indexed incident data using FAISS and Sentence Transformers.

Backend Development:

Created a FastAPI server.

Integrated Ollama for AI-based responses.

Implemented retrieval-augmented generation (RAG) using FAISS.

Frontend Development:

Built an interactive Gradio UI with persona-based tabs.

Integrated the FastAPI backend for real-time responses.

## 🚧 Challenges We Faced
Ensuring accurate responses: Fine-tuning persona-based queries for better contextual understanding.

Efficient retrieval: Implementing FAISS indexing for quick and relevant information retrieval.

User experience: Designing an intuitive and responsive UI with multiple personas.

Performance tuning: Optimizing API calls and embedding models for faster response times.

## 🏃 How to Run

1. Install Dependencies
pip install fastapi uvicorn ollama gradio faiss-cpu sentence-transformers requests
2. Set Up the FAISS Database
python vector_store.py
3. Start the Backend
uvicorn backend:app --reload
4. Start the Gradio Frontend
python frontend.py
5. Access the UI
Open http://localhost:7860 in a web browser and start using the chatbot.

## 🏗️ Tech Stack
- 🔹 Frontend: Gradio
- 🔹 Backend: FastAPI, Ollama
- 🔹 Database: FAISS, Sentence Transformers
- 🔹 Other: JSONL for past incidents

## 👥 Team AutoBytes
- **Vishnu Theertha** - [https://github.com/vishnu0389](#)
- **Joydeep Ghosh** - 
- **Satyaki Chatterjee** - 
- **Venkatesh Girjali** - 
- **Sonal Chouhan** - 