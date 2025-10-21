import os
from dotenv import load_dotenv

load_dotenv()

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "mistral:instruct")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "ollama")
