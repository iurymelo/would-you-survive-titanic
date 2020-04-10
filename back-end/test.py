# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 06:09:48 2020

@author: iurym
"""

import pickle
from sklearn import model_selection
from sklearn.ensemble import GradientBoostingClassifier
import numpy as np

data_raw = [[1, 1, 22, 1]]
data = np.array(data_raw)
model = pickle.load(open('model.pickle', 'rb'))

res = model.predict(data)
print(res)