import gradio as gr
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting Gradio application...")

def greet(name):
    logging.info(f"Received input: {name}")
    return "Hello, " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")

logging.info("Launching Gradio interface...")
iface.launch()

logging.info("Gradio application launched.")
