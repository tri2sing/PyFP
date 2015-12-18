'''
Created on Dec 18, 2015

@author: Sameer Adhikari
'''

import os
from work_with_collections.xml_parser import xml_tree_to_row_iterator

def test_xml_tree_to_row_iterator():
        with open(os.getcwd() + '/work_with_collections/locations.xml') as source:
            rows = tuple(xml_tree_to_row_iterator(source))
            assert(len(rows) == 6)
