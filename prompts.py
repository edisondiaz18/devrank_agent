# Almacena las plantillas de prompts para la IA

def get_issue_analysis_prompt(title, body, labels, comments_count, age_days):
    """Genera el prompt para analizar un issue de GitHub."""

    label_str = ", ".join(labels) if labels else "None"

    prompt = f"""
    Analyze the following GitHub issue to estimate its urgency, potential impact, and complexity for prioritization.
    Provide estimations on a scale of 1 (lowest) to 5 (highest). Respond ONLY with a JSON object containing 'urgency', 'impact', and 'complexity' keys with integer values.

    Issue Details:
    - Title: {title}
    - Description: {body[:500]}... # Truncate body for brevity if needed
    - Labels: {label_str}
    - Comments Count: {comments_count}
    - Age (days): {age_days}

    Analysis Criteria:
    - Urgency: Consider labels like 'bug', 'critical', 'security'. Older unresolved critical issues are more urgent.
    - Impact: Consider how many users might be affected or if it impacts core functionality. Labels like 'enhancement', 'feature' might have high impact.
    - Complexity: Consider the description length, technical terms, labels like 'refactor', 'documentation', 'good first issue' (low complexity).

    Estimated Analysis (JSON Output Only):
    """
    return prompt