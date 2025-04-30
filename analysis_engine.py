# Lógica para interactuar con Azure OpenAI y calcular prioridad

import os
from openai import AzureOpenAI
import json
from config import AZURE_OPENAI_API_KEY, AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_DEPLOYMENT_NAME
from prompts import get_issue_analysis_prompt

client = AzureOpenAI(
    api_key=AZURE_OPENAI_API_KEY,
    api_version="2024-02-01", # Usa la versión de API más reciente que soporte tu modelo
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

def analyze_issue_with_ai(issue_data):
    """Analiza un issue usando Azure OpenAI."""
    prompt = get_issue_analysis_prompt(
        title=issue_data.get('title', ''),
        body=issue_data.get('body', ''),
        labels=issue_data.get('labels', []),
        comments_count=issue_data.get('comments_count', 0),
        age_days=issue_data.get('age_days', 0)
    )

    try:
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are an AI assistant helping prioritize GitHub issues."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2, # Baja temperatura para respuestas más consistentes/deterministas
            max_tokens=100,
            response_format={"type": "json_object"} # ¡Importante para forzar salida JSON!
        )

        analysis_str = response.choices[0].message.content
        analysis = json.loads(analysis_str)
        # Validar que el JSON tiene las claves esperadas (urgency, impact, complexity)
        if all(k in analysis for k in ('urgency', 'impact', 'complexity')):
            return analysis
        else:
            print(f"Error: Unexpected JSON format from AI: {analysis_str}")
            return {'urgency': 0, 'impact': 0, 'complexity': 0} # Fallback

    except Exception as e:
        print(f"Error calling Azure OpenAI: {e}")
        return {'urgency': 0, 'impact': 0, 'complexity': 0} # Fallback

def calculate_priority(analysis, weights={'urgency': 3, 'impact': 2, 'complexity': -1}):
    """Calcula un puntaje de prioridad basado en el análisis de IA."""
    score = (analysis.get('urgency', 0) * weights['urgency'] +
             analysis.get('impact', 0) * weights['impact'] +
             analysis.get('complexity', 0) * weights['complexity'])
    return score