import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000/analyze"

def analyze_incident(persona, incident):
    response = requests.post(API_URL, json={"persona": persona, "incident": incident})
    return response.json().get("response", "No response received")

# Define UI
with gr.Blocks() as demo:
    gr.Markdown("# IT Support Chatbot")

    with gr.Tabs():
        for persona in ["os_support", "db_support", "network_support", "hardware_support", "storage_support"]:
            with gr.Tab(persona.replace("_", " ").title()):
                incident_input = gr.Textbox(label="Describe the issue")
                submit_button = gr.Button("Analyze")
                response_output = gr.Textbox(label="Response", interactive=False)

                submit_button.click(analyze_incident, inputs=[gr.Textbox(value=persona, visible=False), incident_input], outputs=response_output)

# Run Gradio UI
demo.launch()
