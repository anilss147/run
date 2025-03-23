import gradio as gr
import logging
import os

# Configure logging
log_file_path = os.path.join(os.getcwd(), 'gradio.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting Gradio application...")

print("Gradio launch initiated")

gr.Interface(lambda x: x, "text", "text").launch(share=False, server_name="127.0.0.1", server_port=7861, debug=True)

logging.info("Gradio application launched.")
