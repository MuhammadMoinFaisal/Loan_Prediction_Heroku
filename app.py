from flask import Flask, request, render_template

import pickle 

import numpy as np

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))


@app.route('/',methods=['GET'])
def Home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender = int(request.form['Gender'])
        Married =int(request.form['Married'])
        Dependents = int(request.form['Dependents'])
        Education = int(request.form['Education'])
        Self_Employed = int(request.form['Self_Employed'])

        predictions = model.predict([[Gender, Married, Dependents, Education, Self_Employed]])

        output = round(predictions[0],2)
        return render_template('home.html', prediction_text = "Loan Prediction {}".format(output))

if __name__ == "__main__":
    app.run(debug=True)

