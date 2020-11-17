import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('regressor.pkl', 'rb'))
model1 = pickle.load(open('linearregressor.pkl', 'rb'))
lb = pickle.load(open('lb', 'rb'))
lb1 = pickle.load(open('lb1', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [str(x) for x in request.form.values()]
    print(features)
    year = int(features[0])
    kms_driven = int(features[1])
    final_features = []
    #a=[]
    #a = 
    #print(a)
    final_features.append(year)
    final_features.append(kms_driven)
    final_features.append(lb.transform([features[2]])[0])
    final_features.append(lb1.transform([features[3]])[0])
    print(len(final_features))
    prediction = model.predict([final_features])
    pred1=model1.predict([final_features])
    output = round(prediction[0], 0)   
    output1 = round(pred1[0], 0)
    out1 = [output, output1]
    s='''\
... Price with repect to RANDOM FOREST REGRESSION is {0} .
...  Price with respect to LINEAR REGRESSION is {1}.\
... '''.format(out1[0],out1[1])
#     out = '''Price with repect to RANDOM FOREST REGRESSION is {0} \n Price with respect to LINEAR REGRESSION is {1}'''.format(out1[0],out1[1])
    return render_template('index.html',prediction_text = s)
 


if __name__ == "__main__":
    app.run(debug=True)
