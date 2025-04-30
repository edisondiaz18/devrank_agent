# Guarda claves de API, nombre de repo, etc. (¡NO subir a GitHub!)

import os
from dotenv import load_dotenv

load_dotenv() # Carga variables desde un archivo .env

GITHUB_TOKEN = os.getenv("GITHUB_PERSONAL_ACCESS_TOKEN")
REPO_NAME = os.getenv("GITHUB_REPO_NAME") # Ej: "octocat/Spoon-Knife"
AZURE_OPENAI_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_DEPLOYMENT_NAME = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME") # Nombre de tu despliegue GPT