# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 00:52:55 2020

@author: iurym
@description: Train the titanic surviving predictor passing the train and test
hd5 saved by data_preparation/the data_wrengling.py
"""
import argparse
import pickle
import dask.dataframe as dd
from dask.distributed import Client
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score, f1_score


ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', help='Path to the datasets', 
                required=True)
ap.add_argument('-o', '--output', help='Output to the trained network')
args = vars(ap.parse_args())

def save_model_disk(classifier):
    
    '''Saves a classifier on a pickle file on path ./data/model
    
    INPUT: classifier
    OUTPUT: pickle file on disk
    '''
    
    print('[INFO] Saving model on disk...')
    output_file_name = 'model.pickle'
    output_path = args['output']
    output_path = output_path if output_path[-1] == '/' else output_path + '/'
    pickle.dump(classifier, open(output_path + output_file_name, 'wb'))
    
    print('[INFO] TASK COMPLETED WITH SUCCESS!!')

def train_network():
    '''Gradient Boosting classifier to predict if a person would survive
    or not the Titanic sinking based on their age, gender, spouse or siblings
    onboard, and class (1st class, 2nd class, or 3rd class).
    
    RETURN: classifier
    '''
    classifier = GradientBoostingClassifier(random_state=15)
    
    path = args['input']
    path = path if path[-1] == '/' else path+'/'
    
    
    print('[INFO] Loading model...')
    train = dd.read_parquet(path + 'train/')
    test = dd.read_parquet(path + 'test/')

    
    train_y = train['Survived']
    train_X = train.drop(['Survived'], axis=1)
    train.compute()
    
    test_y = test['Survived']
    test_x = test.drop(['Survived'], axis=1)
    test.compute()
    
    print('[INFO] Training model...')
    classifier.fit(train_X, train_y)
    
    pred = classifier.predict(test_x)
    
    acc = accuracy_score(test_y, pred)
    fscore = f1_score(test_y, pred)
    
    print('[INFO] Training completed! ')
    print('Acc: {}, F1-Score: {}'.format(acc, fscore))
    
    save_model_disk(classifier)

if __name__ == '__main__':
    client = Client()
    train_network()