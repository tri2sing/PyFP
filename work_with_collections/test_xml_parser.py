'''
Created on Dec 18, 2015

@author: Sameer Adhikari
'''

import os
import urllib.request

from work_with_collections.xml_parser import\
     xml_tree_to_row_iterator,\
     latitude_longitude_iterator

def test_xml_tree_to_row_iterator():
    with open(os.getcwd() + '/work_with_collections/locations.xml') as source:
        rows = tuple(xml_tree_to_row_iterator(source))
        assert(len(rows) == 6)
        assert(len(rows[0]) == 3)

def test_latitude_longitude_iterator():
    # Demonstrates use of an alternate function to open the file while reusing the iterators as-is.
    with urllib.request.urlopen('file:' + os.getcwd() + '/work_with_collections/locations.xml') as source:
        rows = tuple(latitude_longitude_iterator(xml_tree_to_row_iterator(source)))
        assert(len(rows) == 6)
        assert(len(rows[0]) == 2)
