import gradio as gr
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Starting Gradio application...")
print("Gradio launch initiated")

gr.Interface(lambda x: x, "text", "text").launch(share=False, server_name="127.0.0.1", server_port=7861)

logging.info("Gradio application launched.")
