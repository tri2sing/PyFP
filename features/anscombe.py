'''
Created on Dec 14, 2015

@author: Sameer Adhikari
'''

# Example of generators through working with Anscombe's Quartet
# https://en.wikipedia.org/wiki/Anscombe's_quartet

import csv

def csv_row_iterator(source, delimiter='\t'):
    '''Return an iterator for the rows of a csv file '''
    return csv.reader(source, delimiter=delimiter)

def csv_head_trimmer(row_iterator):
    '''Remove the first three rows of anscombe's quartet data assuming a specific format'''
    title = next(row_iterator)
    assert(len(title) == 1 and title[0] == "Anscombe's Quartet")
    heading = next(row_iterator)
    assert(len(heading) == 4 and heading == ['I', 'II', 'III', 'IV'])
    columns = next(row_iterator)
    assert(len(columns) == 8 and columns == ['x ', 'y ', 'x ', 'y ', 'x ', 'y ', 'x ', 'y'])
    return row_iterator
    

def main():
    with open('anscombe.txt') as source:
        for row in csv_head_trimmer(csv_row_iterator(source)):
            print(row)

if __name__ == '__main__':
    main()
