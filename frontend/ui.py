import gradio as gr
import logging
import time
import os

# Configure logging
log_file_path = os.path.join(os.getcwd(), 'gradio.log')
logging.basicConfig(filename=log_file_path, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting Gradio application...")

def greet(name):
    logging.info(f"Received input: {name}")
    return "Hello, " + name + "!"

logging.info("Creating Gradio interface...")
iface = gr.Interface(fn=greet, inputs="text", outputs="text")

logging.info("Launching Gradio interface...")
iface.launch(share=False, server_name="127.0.0.1", server_port=7860)

logging.info("Gradio application launched.")

time.sleep(5)  # Add delay to ensure application is fully started.
logging.info("Gradio application should be ready.")

# Add any relevant code from your original ui.py file here.
# For example, if you have other functions or UI elements, add them below.
# Example:

# def another_function(input_value):
#     logging.info(f"Another function called with: {input_value}")
#     return f"Processed: {input_value}"

# iface2 = gr.Interface(fn=another_function, inputs="text", outputs="text")
# iface2.launch(share=False, server_name="127.0.0.1", server_port=7861) #if you have more interfaces they need different ports.

# logging.info("Second Gradio application launched.")
