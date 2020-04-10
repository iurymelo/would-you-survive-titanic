# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:52:55 2020

@author: iurym
@description: Train the titanic surviving predictor passing the train and test
hdf files
"""

import os
import time
import pickle
import dask.dataframe as dd
from dask.distributed import Client
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score

def wait_dataset():
    '''Check if the data wrangler finished its work.
    
    Returns
    -------
    None
    '''
    
    flag = False
    path = 'data_preparation/data/finished.lock'
    print('[INFO] Waiting for the dataset...')
    while not flag:
        flag = os.path.exists(path)
        # Wait 5 seconds
        time.sleep(5)
        
def save_model_disk(classifier):
    
    '''Saves a classifier on a pickle file on path ./data/model
    
    Parameters
    ----------
    classifier: sklearn classifier
    
    Returns
    -------
    None
    '''
    
    # Save a pickle file on disk containing the trained classifier
    print('[INFO] Saving model on disk...')
    pickle.dump(classifier, open('training/data/model/model.pickle', 'wb'))
    
    print('[INFO] TASK COMPLETED WITH SUCCESS!!')

def train_network():
    '''Trains a gradient Boosting classifier to predict if a person would survive
    or not the Titanic sinking based on their age, gender, spouse or siblings
    onboard, and class (1st class, 2nd class, or 3rd class).
    
    Returns
    -------
    None
    '''
    
    # Load the classifier
    classifier = GradientBoostingClassifier(random_state=15)  
    
    # Wait parquet to be created
    wait_dataset()
    
    # Load parquet in memory
    print('[INFO] Loading model...')
    train = dd.read_parquet('data_preparation/data/train/train.parquet')
    test = dd.read_parquet('data_preparation/data/test/test.parquet')
    print('[INFO] Model loaded')

    
    # Load the train dataset
    train_y = train['Survived']
    train_X = train.drop(['Survived'], axis=1)
    train.compute()
    
    # Load the test dataset    
    test_y = test['Survived']
    test_x = test.drop(['Survived'], axis=1)
    test.compute()
    print('[DEBUG] TEST HEAD')
    print(test_x.head())
    print(test_y.head())
    
    # Train the classifier
    print('[INFO] Training model...')
    classifier.fit(train_X, train_y)
    
    # Predict with the test dataset
    pred = classifier.predict(test_x)
    
    # Compare with the test dataset results, and create
    # two metrics: Accuracy and F1 Score 
    acc = accuracy_score(test_y, pred)
    fscore = f1_score(test_y, pred)
    
    
    print('[INFO] Training completed! ')
    print('Acc: {}, F1-Score: {}'.format(acc, fscore))
    
    save_model_disk(classifier)

if __name__ == '__main__':
    client = Client()
    train_network()
