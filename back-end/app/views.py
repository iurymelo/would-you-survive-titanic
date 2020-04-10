# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:43:04 2020

@author: iurym
"""
from app import app, request, jsonify

import pickle
import pandas as pd
import numpy as np

# Load the pickle model
model = pickle.load(open('app/model/model.pickle', 'rb'))

# GET REQUEST
@app.route('/predict')
def predict():
    '''Predict the results sent at the request params.
    Request example: 
        http:127.0.0.0:5000/predict??age=23&sex=0&pclass=2&sibsp=0

    Returns
    -------
    json
        json file with "survived" key, and value 0 for not survived and
        1 for survived

    '''
    # Get the params 
    age = request.args.get('age', None)
    sex = request.args.get('sex', None)
    pclass = request.args.get('pclass', None)
    sibsp = request.args.get('sibsp', None)
    
    # Convert to numpy array
    data_np = np.array([[pclass, sex, age, sibsp]])

    # Convert to pandas dataframes
    data = pd.DataFrame(data_np, columns=['Pclass', 'Sex', 'Age', 'SibSp'])

    # Predict
    res = model.predict(data)
    res = str(res[0])
    
    # Save result in a python dict
    data_return = {
        'survived': res
        }
    
    # Return the dict converted to JSON
    return jsonify(data_return)
