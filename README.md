*****AI Weather Assistant*****

An AI-powered weather chat application built using React + Vite + Tailwind CSS on the frontend and FastAPI + LangChain + OpenRouter on the backend.
The assistant understands natural language queries and dynamically uses a weather tool (Open-Meteo, no API key) to provide real-time weather insights.

*****Features*****

->Chat-based UI (modern, responsive design)

->LLM-powered assistant using OpenRouter

->Tool calling with LangChain

->Real-time weather data using Open-Meteo (no API key required

->FastAPI backend with REST API

->Tailwind CSS for clean and modern UI

->End-to-end React ↔ FastAPI integration

*****How It Works*****

User sends a natural language query via the chat UI
->FastAPI receives the request
->LangChain passes the query to the LLM
->LLM dynamically calls the Open-Meteo weather tool
->Weather data is returned and converted into a human-friendly response
->Response is displayed in the chat interface


<img width="994" height="781" alt="Screenshot 2025-12-19 060314" src="https://github.com/user-attachments/assets/f74e5fb5-886c-45fa-9466-cc49f6a37d1a" />


Why Open-Meteo?

->Completely free

->No API key required

->Reliable global coverage


*****System Architecture*****

The system follows a client–server architecture:

Frontend: React + Vite + Tailwind CSS

Backend: FastAPI + LangChain

AI Layer: OpenRouter LLM

Weather Data Source: Open-Meteo API (keyless)
