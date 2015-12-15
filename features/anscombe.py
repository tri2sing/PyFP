'''
Created on Dec 14, 2015

@author: Sameer Adhikari
'''

# Example of generators through working with Anscombe's Quartet
# https://en.wikipedia.org/wiki/Anscombe's_quartet

import csv
from collections import namedtuple
from pprint import pprint


def csv_row_iterator(source, delimiter='\t'):
    '''Return an iterator for the rows of a csv file '''
    return csv.reader(source, delimiter=delimiter)


def csv_row_trim_iterator(row_iterator):
    '''Remove the first three rows of anscombe's quartet data assuming a specific format'''
    title = next(row_iterator)
    assert(len(title) == 1 and title[0] == "Anscombe's Quartet")
    heading = next(row_iterator)
    assert(len(heading) == 4 and heading == ['I', 'II', 'III', 'IV'])
    columns = next(row_iterator)
    assert(len(columns) == 8 and columns == ['x ', 'y ', 'x ', 'y ', 'x ', 'y ', 'x ', 'y'])
    return row_iterator


def series_point_generator(series_num, row_iterator):
    ''' Each row of Anscombe's Quartet data consists four (x, y) points from different series.
        This generator yields the points from all rows from a specified series (0, 1, 2, 3'''
    Point = namedtuple('Point', ('x', 'y'))
    for row in row_iterator:
        yield Point(*row[2 * series_num : 2 * series_num + 2])
             

def main():
    with open('anscombe.txt') as source:
        # Materialize the iterator using tuple() so that it can be reused multiple times.
        # In FP we prefer to use tuple compared to list because we prefer immutable objects.
        data = tuple(csv_row_trim_iterator(csv_row_iterator(source)))
        series_0 = tuple(series_point_generator(0, data))
        series_1 = tuple(series_point_generator(1, data))
        series_2 = tuple(series_point_generator(2, data))
        series_3 = tuple(series_point_generator(3, data))
        pprint(data)
        pprint(series_0)
        pprint(series_1)
        pprint(series_2)
        pprint(series_3)

if __name__ == '__main__':
    main()
