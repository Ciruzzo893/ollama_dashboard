from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from contextlib import asynccontextmanager
import ollama
import psutil
import os
import shutil
import requests
import subprocess
from datetime import datetime

app = FastAPI()

# Configurazione CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configurazione CORS per gli header
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
)

# Endpoint per la chat
@app.get("/")
async def read_root():
    return {"message": "Hello, World!"}

@app.get("/hello")
async def say_hello():
    return {"message": "Hello World"}

@app.get("/ollama")
async def ollama():
    # Ottieni l'elenco dei modelli disponibili
    response = ollama.list()
    return {"models": response['models']}
