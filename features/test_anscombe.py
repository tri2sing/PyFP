'''
Created on Dec 14, 2015

@author: Sameer Adhikari
'''

import os
from features.anscombe import csv_row_iterator,\
    csv_row_trim_iterator, series_point_generator

def test_csv_row_iterator():
    print(os.getcwd()) # If test is successful this does not get printed to stdout
    # py.test looks for a file to open in the project folder rather than the 
    # package folder unlike the case when we run the module itself, hence the 
    # path to the file to open needs to be specified in this manner.
    with open(os.getcwd() + '/features/anscombe.txt') as source:
        rows = tuple(csv_row_iterator(source, '\t'))
        assert(len(rows) == 14)
        

def test_csv_head_trimmer():
    with open(os.getcwd() + '/features/anscombe.txt') as source:
        rows = tuple(csv_row_trim_iterator(csv_row_iterator(source, '\t')))
        assert(len(rows) == 11)
    

def test_series_point_generator():
    with open(os.getcwd() + '/features/anscombe.txt') as source:
        data = tuple(csv_row_trim_iterator(csv_row_iterator(source)))
        
        series_0 = tuple(series_point_generator(0, data))
        assert(len(series_0) == 11)
        assert(len(series_0[0]) == 2)
        
        series_1 = tuple(series_point_generator(1, data))
        assert(len(series_1) == 11)
        assert(len(series_1[0]) == 2)
        
        series_2 = tuple(series_point_generator(2, data))
        assert(len(series_2) == 11)
        assert(len(series_2[0]) == 2)
        
        series_3 = tuple(series_point_generator(3, data))
        assert(len(series_3) == 11)
        assert(len(series_3[0]) == 2)
