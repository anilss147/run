# frontend/ui.py
import gradio as gr
import logging
import time
import os

# Configure logging
log_file_path = os.path.join(os.getcwd(), 'gradio.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting Gradio application...")

def identity(x):
    logging.info(f"Received input: {x}")
    return x

logging.info("Creating Gradio interface...")
iface = gr.Interface(fn=identity, inputs="text", outputs="text")

logging.info("Launching Gradio interface...")
iface.launch(share=False, server_name="127.0.0.1", server_port=7860)

logging.info("Gradio application launched.")

time.sleep(5)  # Add delay to ensure application is fully started.
logging.info("Gradio application should be ready.")
