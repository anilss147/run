import gradio as gr
import logging

logging.basicConfig(filename='gradio.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def chat(text):
    logging.info(f"Received input: {text}")
    return "UI Response: " + text

iface = gr.Interface(fn=chat, inputs="text", outputs="text")
iface.launch()
