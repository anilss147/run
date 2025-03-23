import gradio as gr
import logging
import time
import os
import pandas as pd

# Configure logging
log_file_path = os.path.join(os.getcwd(), 'gradio.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting Gradio application...")

def process_data(name):
    logging.info(f"Processing data for: {name}")
    try:
        df = pd.read_csv("data/data.csv")
        result = df[df["name"] == name].to_string()
        return result
    except FileNotFoundError:
        return "Data file not found."

logging.info("Creating Gradio interface...")
iface = gr.Interface(
    fn=process_data,
    inputs="text",
    outputs="text",
    title="Data Processor",
    description="Enter a name to retrieve data.",
    examples=["John", "Jane", "Bob"],
    css="static/style.css",
    thumbnail="images/logo.png"
)

logging.info("Launching Gradio interface...")
iface.launch(share=False, server_name="127.0.0.1", server_port=7860)

logging.info("Gradio application launched.")

time.sleep(5)  # Add delay to ensure application is fully started.
logging.info("Gradio application should be ready.")
