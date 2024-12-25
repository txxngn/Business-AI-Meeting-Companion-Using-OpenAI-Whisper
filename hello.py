import gradio as gr

def greet(name):
    return "Hello " + name + "!"

demo = gr.Interface(fn=greet, inputs="text", outputs="text")
"""
fn: the function to wrap a UI around
inputs: which component(s) to use for the input (e.g. “text”, “image” or “audio”)
outputs: which component(s) to use for the output (e.g. “text”, “image” or “label”)
"""
demo.launch(server_name="0.0.0.0", server_port= 7860)