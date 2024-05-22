import gradio as gr
from joblib import load

model = load("Classifier.joblib")

def pred(Email):
    l = model.predict([Email])
    if l[0]==1:
        return "Spam ⚠️"
    else:
        return "👍"

iface = gr.Interface(fn=pred, inputs="text", outputs="text", allow_flagging="never", description="Enter Your Message Below :")
iface.launch(share=True)
