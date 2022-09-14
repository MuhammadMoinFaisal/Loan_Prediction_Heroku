from flask import Flask, request

import pickle

import pandas as pd

from flask import jsonify

app = Flask(__name__)

pickle_in  = open(r'model.pkl', 'rb')


model = pickle.load(pickle_in)


@app.route("/")

def Welcome():

    return "Welcome to This Page Dear"


@app.route("/prediction", methods=['POST'])

def prediction_model():
    content = request.json

    data = pd.DataFrame(content)

    dict_to_retun = model.predict(data).tolist()

    return jsonify(dict_to_retun)


if __name__ == "__main__":
    app.run(host = '127.0.0.1', port = 9000)
