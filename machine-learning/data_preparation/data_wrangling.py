# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:36:33 2020

@author: iurym
@description: This file is used to clear and prepare the dataset.
"""

import argparse
import dask.dataframe as dd
from dask.distributed import Client

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', help='Path to the CSV file', 
                required=True)
ap.add_argument('-o', '--output', help='Path to save the Train/Test files', 
                required=True)
args = vars(ap.parse_args())

def save_dataset_disk(train, test):
    
    '''Save the train and test dataset on disk to be accessed by the
    training function later.
    
    INPUT: train_dataset, test_dataset
    OUTPUT: train_x, train_y, test_x, test_y
    '''
    output_dir = args['output']
    
    # Check if the last character is /, if not add it.
    output_dir = output_dir if output_dir[-1] == '/' else output_dir+'/'

    print('[INFO] Saving train dataset on disk')
    train.to_parquet(output_dir + 'train/' + 'train.parquet')
    test.to_parquet(output_dir + 'test/' + 'test.parquet')
    

    

def prepare_dataset():
    
    '''Prepare the dataset removing unnecessary columns, removing rows with
    nan, and transfoming strings to numbers.
    
    INPUT: none
    OUTPUT: train and test dataset.
    '''
    
    # Dask is a overkill for this small dataset. 
    # I am using just as an example.
    df = dd.read_csv(args['input'], blocksize=300)
    
    
    # Clean the data
    df = df.drop(df.columns.difference(['Survived', 'Pclass', 'Sex', 
                                        'Age', 'SibSp']), axis=1)
    
    # Remove ages with NaN
    df = df.dropna()
    
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    
    train, test = df.random_split([0.8, 0.2])
    
    df.compute()
    
    save_dataset_disk(train, test)
    
if __name__  == '__main__':
    client = Client()
    prepare_dataset()