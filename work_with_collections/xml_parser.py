'''
Created on Dec 15, 2015

@author: Sameer Adhikari
'''

import xml.etree.ElementTree as etr

def xml_tree_to_row_iterator(file_obj):
    '''Parses a file at low-level and yields an iterable sequence of tuples.
    Uses a for loop to go through the matching contents in the file.'''
    # ns = namespace
    ns_map = {
        'ns0': 'http://www.opengis.net/kml/2.2',
        'ns1': 'http://www.google.com/kml/ext/2.2'
        }
    doc = etr.parse(file_obj)
    # A generator expression is a high-performance, memory-efficient generalization of list comprehension.
    # To create a generator expression, wrap a comprehension expression in () instead of [] or {}.
    # The XM path in findall is case-sensitive, that is why the coordinates element.
    return (coordinate.text.split(',') 
        for coordinate in doc.findall('./ns0:Document/ns0:Folder/ns0:Placemark/ns0:Point/ns0:coordinates', ns_map))
        
def main():
    with open('locations.xml') as source:
        coordinates = xml_tree_to_row_iterator(source)
        for coordinate in coordinates:
            print(coordinate)

if __name__ == '__main__':
    main()