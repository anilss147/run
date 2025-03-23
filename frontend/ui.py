import gradio as gr
import logging
import time

logging.basicConfig(filename='gradio.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting Gradio application...")

def greet(name):
    logging.info(f"Received input: {name}")
    return "Hello, " + name + "!"

logging.info("Creating Gradio interface...")
iface = gr.Interface(fn=greet, inputs="text", outputs="text")

logging.info("Launching Gradio interface...")
iface.launch(share=False, server_name="127.0.0.1")

logging.info("Gradio application launched.")

time.sleep(5) #Adding a delay to make sure that the application has time to fully start.
logging.info("Gradio application should be ready.")
