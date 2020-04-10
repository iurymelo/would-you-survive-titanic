# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 05:29:26 2020

@author: iurym
"""

import pickle
import numpy as np
from flask import Flask, request, jsonify
from sklearn import model_selection
from sklearn.ensemble import GradientBoostingClassifier

classifier = GradientBoostingClassifier()

model = pickle.load(open('model.pickle', 'rb'))

app = Flask(__name__)



#127.0.0.1:5000/predict?sex=1&age=22&pclass=1&sibsp=2
#GET /books
@app.route('/predict')
def predict():
    age = request.args.get('age', None)
    sex = request.args.get('sex', None)
    pclass = request.args.get('pclass', None)
    sibsp = request.args.get('sibsp', None)
    
    data_raw = [[pclass, sex, age, sibsp]]
    
    data = np.array(data_raw)
    
    res = model.predict(data)
    res = str(res[0])
    
    data_return = {
        'survived': res
        }
    
    return jsonify(data_return)


app.run(port=5000)

