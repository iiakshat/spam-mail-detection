import gradio as gr
import pickle
import pandas as pd
from urlextract import URLExtract
import URLFeatureExtraction

with open("models/spam-clf.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/xgb.dat", "rb") as f:
    model2 = pickle.load(f)

df = pd.DataFrame(columns=['URL', 'Phishy?'])

def isPhishing(link):
    global df

    features = URLFeatureExtraction.featureExtraction(link)
    print(features)
    
    prediction = model2.predict([features])
    print(prediction)

    df = df._append({'URL': link, 'Phishy?': "UnSafe" if prediction[0] else "Safe"}, ignore_index=True)
    return prediction[0]

def isSpam(Email):
    out = model.predict([Email])
    return "Spam" if out[0] else "Not Spam"

def check_URL(Email):
    extractor = URLExtract()
    urls = extractor.find_urls(Email)
    n_urls = len(urls)
    if urls:
        bad_urls = sum([isPhishing(url) for url in urls])
    else:
        bad_urls = 0
    print("Out of {} urls {} are phishing".format(n_urls, bad_urls))

    return bad_urls

def check_Mail(Email):
    state = max(URLFeatureExtraction.state, 0)
    return [isSpam(Email), check_URL(Email), state, df]

iface = gr.Interface(
    fn=check_Mail,
    inputs=gr.Textbox(lines=6, placeholder="Enter or paste email here", label="Email"),
    outputs=[
        gr.Textbox(label="Spam or Not"),
        gr.Textbox(label="Phishing Links Detected"),
        gr.Textbox(label="Consider this Mail as"),
        gr.Dataframe(label="Insights", interactive=False)
    ]
)

# Launch the Gradio app
iface.launch()