from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import ask_agent

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
def chat(data: dict):
    return {"response": ask_agent(data["message"])}
