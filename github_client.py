# Lógica para interactuar con la API de GitHub

import requests
from datetime import datetime, timezone
from config import GITHUB_TOKEN, REPO_NAME

# O usar PyGithub: from github import Github

def get_open_issues():
    """Obtiene los issues abiertos del repositorio configurado."""
    issues_data = []
    # --- ¡IMPLEMENTAR AQUÍ! ---
    # Usar 'requests' o 'PyGithub' para:
    # 1. Autenticarse con GITHUB_TOKEN.
    # 2. Hacer una petición a la API de GitHub para obtener issues abiertos de REPO_NAME.
    # 3. Para cada issue, extraer: number, title, body, labels (lista de nombres), comments (count), created_at.
    # 4. Calcular age_days = (datetime.now(timezone.utc) - created_at_datetime).days
    # 5. Añadir un diccionario con estos datos a la lista issues_data.
    # Ejemplo (con requests, muy simplificado):
    # headers = {'Authorization': f'token {GITHUB_TOKEN}'}
    # url = f'https://api.github.com/repos/{REPO_NAME}/issues?state=open'
    # response = requests.get(url, headers=headers)
    # if response.status_code == 200:
    #     raw_issues = response.json()
    #     for issue in raw_issues:
    #          # Procesar y añadir a issues_data...
    #          pass # Añade tu lógica de extracción aquí
    # else:
    #     print(f"Error fetching issues: {response.status_code}")
    print("Placeholder: Implementa la lógica de GitHub API aquí.")
    # --- Fin de Implementación ---
    # Retornar datos de ejemplo mientras implementas:
    return [
        {'number': 1, 'title': 'Fix critical login bug', 'body': 'Users cannot log in.', 'labels': ['bug', 'critical'], 'comments_count': 5, 'age_days': 2},
        {'number': 2, 'title': 'Add dark mode feature', 'body': 'Implement a dark theme for the UI.', 'labels': ['feature', 'ui'], 'comments_count': 10, 'age_days': 30},
        {'number': 3, 'title': 'Update documentation', 'body': 'README needs updating.', 'labels': ['documentation'], 'comments_count': 1, 'age_days': 5},
    ]