# Punto de entrada principal

import github_client
import analysis_engine

def main():
    print("Fetching open issues...")
    issues = github_client.get_open_issues()

    if not issues:
        print("No issues found or error fetching issues.")
        return

    print(f"Analyzing {len(issues)} issues with Azure OpenAI...")
    analyzed_issues = []
    for issue in issues:
        print(f"  Analyzing issue #{issue.get('number', 'N/A')}: {issue.get('title', 'N/A')}")
        ai_analysis = analysis_engine.analyze_issue_with_ai(issue)
        priority_score = analysis_engine.calculate_priority(ai_analysis)
        analyzed_issues.append({
            **issue, # Combina datos originales
            'ai_analysis': ai_analysis,
            'priority_score': priority_score
        })

    # Ordenar issues por puntaje de prioridad (descendente)
    analyzed_issues.sort(key=lambda x: x['priority_score'], reverse=True)

    print("\n--- Prioritized Issues Report ---")
    for issue in analyzed_issues:
        analysis = issue['ai_analysis']
        print(f"\nIssue #{issue.get('number')}: {issue.get('title')} (Score: {issue.get('priority_score'):.1f})")
        print(f"  AI Analysis -> Urgency: {analysis.get('urgency')}/5 | Impact: {analysis.get('impact')}/5 | Complexity: {analysis.get('complexity')}/5")
        print(f"  Labels: {issue.get('labels', [])} | Comments: {issue.get('comments_count')} | Age: {issue.get('age_days')} days")

    print("\n--- End of Report ---")

if __name__ == "__main__":
    main()