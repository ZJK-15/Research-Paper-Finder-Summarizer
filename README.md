🔬 AI-Powered Research Paper Finder & Summarizer

This application provides an intuitive Gradio interface to search for and summarize research papers from sources like ArXiv, powered by a backend n8n workflow and the Gemini API.

✨ Features

      Intelligent Search: Enter a research topic, and the app will query relevant papers.

      Automated Summarization: Each found paper is summarized to give you quick insights.

      Direct Access: Provides direct PDF links to the full research papers.

      User-Friendly Interface: Built with Gradio for a clean and interactive experience.

      Scalable Backend: Leverages n8n for flexible and powerful workflow automation.

⚙️ How It Works: The Architecture

     The project employs a client-server architecture, splitting functionality between a frontend UI and a backend workflow that communicate via a webhook.

     Frontend (Gradio): A user enters a research topic into the Gradio interface and clicks "Submit".

     Webhook Trigger: The Gradio app sends the topic as a POST request to a predefined n8n webhook URL.

     Backend (n8n Workflow): The n8n workflow is triggered upon receiving the webhook request and executes the following sequence:

     Webhook: Catches the incoming POST request containing the research topic.

     HTTP Request: Queries the arXiv API (specifically http://export.arxiv.org/api/query?search_query=...) using the provided topic.

     XML to JSON: Converts the raw XML response received from arXiv into a more structured JSON format for easier processing.

     Split Out: Isolates the first 5 relevant papers from the API results, focusing on a manageable subset for summarization.

     Message a Model (Gemini):For each of the selected papers, it sends the abstract and title to the Google Gemini Pro model with a specific prompt to generate 
                              a concise summary.

     Edit Fields: Structures the summarized data (including the original title, the newly generated summary, and the direct PDF link) into a clean, standardized 
                  JSON format.

     Display Results: The final, structured JSON data is then sent back to the Gradio app by the n8n workflow, which subsequently displays the formatted research 
                      paper summaries and links to the user.

     (The n8n workflow visualizes the entire backend process from receiving the webhook to summarizing with Gemini.)

🛠️ Tech Stack

      Frontend UI: Gradio
      Backend Workflow: n8n
      Frontend UI: Gradio
      Language Model: Google Gemini API
      Data Source: arXiv API
      Programming Language: Python
