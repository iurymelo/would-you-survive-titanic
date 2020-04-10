# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:43:04 2020

@author: iurym
"""
from app import app, request, jsonify

import pickle
import pandas as pd
import numpy as np

model = pickle.load(open('app/model/model.pickle', 'rb'))

@app.route('/predict')
def predict():
    age = request.args.get('age', None)
    sex = request.args.get('sex', None)
    pclass = request.args.get('pclass', None)
    sibsp = request.args.get('sibsp', None)
    
    data_np = np.array([[pclass, sex, age, sibsp]])

    data = pd.DataFrame(data_np, columns=['Pclass', 'Sex', 'Age', 'SibSp'])

    res = model.predict(data)
    res = str(res[0])
    
    data_return = {
        'survived': res
        }
    
    return jsonify(data_return)
