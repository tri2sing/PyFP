'''
Created on Dec 14, 2015

@author: Sameer Adhikari
'''

import os
from features.anscombe import csv_row_iterator,\
    csv_head_trimmer

def test_csv_row_iterator():
    print(os.getcwd()) # If test is successful this does not get printed to stdout
    with open(os.getcwd() + '/features/anscombe.txt') as source:
        rows = list(csv_row_iterator(source, '\t'))
        assert(len(rows) == 14)
        

def test_csv_head_trimmer():
    with open(os.getcwd() + '/features/anscombe.txt') as source:
        rows = list(csv_head_trimmer(csv_row_iterator(source, '\t')))
        assert(len(rows) == 11)
    