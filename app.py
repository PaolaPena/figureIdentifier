from fastai.vision.all import *
import gradio as gr

learn = load_learner('model.pkl')

categories = ('circle','square','triangle')

def classify_image(img):
    pred,idx, probs = learn.predict(img)
    return dict(zip(categories, map(float, probs)))

image  = gr.inputs.Image(shape=(192,192))
label = gr.outputs.Label()
examples = ['circle.png','square.png','triangle.png']

intf = gr.Interface(fn=classify_image, inputs = image, outputs = label, examples = examples)
intf.launch(inline=False, share = True)
