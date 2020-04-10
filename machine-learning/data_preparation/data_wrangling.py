# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 22:36:33 2020

@author: iurym
@description: This file is used to clear and prepare the dataset.
"""

import dask.dataframe as dd
from dask.distributed import Client

def save_dataset_disk(train, test):
    
    '''Save the train and test dataset on disk to be accessed by the
    training function later.
    
    Parameters
    ----------
    train: dataframe
          train dataset in dask drataframe
    test: dataframe
          test dataframe in dask dataframe
    
    Returns
    -------
    None
    '''

    print('[INFO] Saving datasets on:')
    print('data/train/')
    print('data/test/')
    
    # Save in disk as a parquet file
    train.to_parquet('data_preparation/data/train/train.parquet')
    test.to_parquet('data_preparation/data/test/test.parquet')
    
    # Save a flag file to say it is finished
    f = open('data_preparation/data/finished.lock', 'x')
    f.close()    

def prepare_dataset():
    
    '''Prepare the dataset removing unnecessary columns, removing rows with
    nan, and transfoming strings to numbers.
    
    RETURNS
    -------
    None
    '''
    
    # Dask is a overkill for this small dataset. 
    # I am using just as an example.
    df = dd.read_csv('data_preparation/data/titanic.csv', blocksize=300)
    
    
    # Clean the data
    df = df.drop(df.columns.difference(['Survived', 'Pclass', 'Sex', 
                                        'Age', 'SibSp']), axis=1)
    
    # Remove ages with NaN
    df = df.dropna()
    
    # Transform the string "male" in 0 and "female" in 1
    df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
    
    # Split the train, test dataset
    train, test = df.random_split([0.8, 0.2])
    
    # Command dask to compute the commands above
    df.compute()
    
    save_dataset_disk(train, test)
    
if __name__  == '__main__':
    client = Client()
    prepare_dataset()
