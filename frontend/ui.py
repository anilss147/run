import gradio as gr
import logging
import os

log_file_path = os.path.join(os.getcwd(), 'gradio.log') # Get current working directory.

logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting Gradio application...")

def greet(name):
    logging.info(f"Received input: {name}")
    return "Hello, " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch()
