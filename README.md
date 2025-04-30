# Descripción del proyecto (¡MUY IMPORTANTE!)

# DevRank Agent - AI-Powered GitHub Issue Prioritization

**Hackathon Submission for Microsoft AI Agent Hackathon (Category: Best in Python)**

## 1. Problem Statement

Developers and project managers often face a large backlog of GitHub issues. Manually sifting through them to decide what to work on next is time-consuming and prone to overlooking critical tasks.

## 2. Solution: DevRank Agent

DevRank Agent is a Python application that connects to a specified GitHub repository, fetches open issues, and uses Azure OpenAI to analyze each issue's title, description, labels, and metadata. It estimates the urgency, potential impact, and complexity, calculating an overall priority score. The agent then presents a ranked list of issues, enabling teams to focus their efforts more effectively.

## 3. Architecture

*(¡Inserta un diagrama simple aquí! Puede ser texto o una imagen)*

* **Input:** GitHub Repo Name, GitHub Token, Azure OpenAI Credentials
* **Components:**
    * `github_client.py`: Fetches issues via GitHub API.
    * `prompts.py`: Defines prompts for LLM analysis.
    * `analysis_engine.py`: Calls Azure OpenAI API, parses results, calculates priority score.
    * `main.py`: Orchestrates the workflow and displays the report.
* **Output:** Prioritized list of GitHub issues printed to the console.

## 4. Tech Stack

* Python 3.x
* Azure OpenAI (GPT-3.5/GPT-4)
* Requests / PyGithub (for GitHub API interaction)
* python-dotenv

## 5. How to Run

1.  **Prerequisites:**
    * Python 3.8+ installed.
    * Azure subscription with access to Azure OpenAI. Deploy a GPT model (e.g., `gpt-35-turbo`).
    * GitHub Personal Access Token with `repo` scope.
2.  **Clone the repository:**
    ```bash
    git clone <your-repo-url>
    cd devrank-agent
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure environment variables:** Create a `.env` file in the root directory with your credentials:
    ```plaintext
    GITHUB_PERSONAL_ACCESS_TOKEN=ghp_YourTokenHere
    GITHUB_REPO_NAME=YourGitHubUsername/YourRepoName  # e.g., microsoft/vscode
    AZURE_OPENAI_API_KEY=YourAzureOpenAIKey
    AZURE_OPENAI_ENDPOINT=[https://YourEndpoint.openai.azure.com/](https://YourEndpoint.openai.azure.com/)
    AZURE_OPENAI_DEPLOYMENT_NAME=YourDeploymentName
    ```
5.  **Run the agent:**
    ```bash
    python main.py
    ```

## 6. Responsible AI Considerations

* **Bias:** The AI's analysis might inherit biases from its training data. The prioritization score is a suggestion, not a definitive command. Human oversight is recommended.
* **Transparency:** The agent shows the AI's estimated scores (urgency, impact, complexity) alongside the final priority score, providing some insight into the decision-making.
* **Data Privacy:** Uses GitHub tokens and potentially accesses issue data. Ensure tokens are handled securely (using `.env` and `.gitignore`).

## 7. Future Work / Potential Enhancements

* Web interface instead of console output.
* Allow user configuration of priority weights.
* More sophisticated NLP analysis (e.g., extracting key entities).
* Integration with project management tools.
* Support for other issue trackers (Jira, etc.).

---
*Submission by [Tu Nombre/Tu Equipo]*
