import pandas as pd
from flask import Flask, jsonify, request, render_template
import numpy as np
import pickle

from sklearn.feature_extraction.text import HashingVectorizer
# load model
model = pickle.load(open('text_all_sources.pkl','rb'))

# app
app = Flask(__name__)
@app.route("/")
def index():
     return render_template('index.html')
# routes

@app.route('/submit', methods=['GET','POST'])

def predict():
    # Get the data from the POST request.
    data = request.form.get("input1")
    hash_vectorizer = HashingVectorizer(stop_words='english')
    print(data)
    data = hash_vectorizer.fit_transform([data])
    # Make prediction using model loaded from disk as per the data.
    print("data is loaded successfully " + str(data))
    prediction = model.predict(data)
    # Take the first value of prediction

    output = prediction[0]
    print(output)
    prediction = output
    return render_template('prediction.html', prediction=prediction)
    #return jsonify(output)



if __name__ == '__main__':
    app.run(port = 8910, debug=True)