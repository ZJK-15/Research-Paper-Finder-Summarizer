import gradio as gr
import requests

# --- Configuration ---
# IMPORTANT: Paste your n8n *Production* Webhook URL here.
# It should NOT contain "/webhook-test/".
N8N_WEBHOOK_URL = "https://zjk15.app.n8n.cloud/webhook-test/373725a0-5ce9-4f79-b5eb-5a7af93194bb"  #Add your N8N webhook URL

# --- Main Logic ---
def find_and_summarize(topic):
    """
    Sends a topic to the n8n workflow and formats the response for Gradio.
    """
    if not topic:
        return "Please enter a topic."
    if "YOUR_N8N_PRODUCTION_WEBHOOK_URL" in N8N_WEBHOOK_URL:
        return "ERROR: Please configure the N8N_WEBHOOK_URL in the app.py script."

    # Data to send to the n8n webhook
    payload = {"topic": topic}

    try:
        # Make the HTTP request to your n8n workflow
        response = requests.post(N8N_WEBHOOK_URL, json=payload)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        results = response.json()

        # FIX: Ensure the result from n8n is always a list
        if isinstance(results, dict):
            results = [results]

        if not results:
            return "No papers found for this topic."

        # --- Format the output for display in Gradio ---
        markdown_output = ""
        for i, paper in enumerate(results):
            # Using .get() provides a default value if a key is missing, preventing errors.
            title = paper.get('title', 'No Title Provided')
            summary = paper.get('summary', 'No Summary Provided')
            url = paper.get('url', '#')

            markdown_output += f"### {i+1}. {title}\n"
            markdown_output += f"**Summary:** {summary}\n\n"
            markdown_output += f"**[Read Paper (PDF)]({url})**\n\n"
            markdown_output += "---\n" # Adds a separator line

        return markdown_output

    except requests.exceptions.RequestException as e:
        # Handle network-related errors (e.g., connection refused, 404)
        return f"Error connecting to the workflow: {e}"
    except Exception as e:
        # Handle other potential errors (e.g., JSON decoding)
        return f"An unexpected error occurred: {e}"

# --- Gradio Interface ---
# Note: Changed allow_flagging to the modern flagging_mode parameter
iface = gr.Interface(
    fn=find_and_summarize,
    inputs=gr.Textbox(
        lines=1,
        placeholder="Graph Neural Networks (GNNs) for complex data relationships.",
        label="Enter a Research Topic"
    ),
    outputs=gr.Markdown(label="Summarized Papers 📜"),
    title="🔬 Research Paper Finder & Summarizer",
    description="Enter a topic to find and summarize the latest papers from ArXiv using n8n and Gemini.",
    flagging_mode="never",
    examples=[
        ["Explainable AI in Healthcare"],
        ["Quantum Computing Algorithms"],
        ["Generative Adversarial Networks for Art"],
        ["Reinforcement Learning in Robotics"],
        ["Climate Change Mitigation Strategies"]
    ]
)

# --- Launch the App ---
if __name__ == "__main__":
    iface.launch()
