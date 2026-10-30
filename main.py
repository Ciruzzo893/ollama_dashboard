from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
import ollama
import psutil
import os

app = FastAPI()

# Configurazione CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Endpoint per la chat
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/ollama")
async def ollama():
    # Ottieni l'elenco dei modelli disponibili
    response = ollama.list()
    return {"models": response['models']}
