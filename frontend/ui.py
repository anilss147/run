import gradio as gr

def greet(name):
    return "Hello, " + name + "!"

iface = gr.Interface(fn=greet, inputs="text", outputs="text")
iface.launch(share=False, server_name="127.0.0.1")
