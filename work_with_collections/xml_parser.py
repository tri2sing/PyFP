'''
Created on Dec 15, 2015

@author: Sameer Adhikari
'''

import xml.etree.ElementTree as etr
'''Demonstrate extraction of latitude and longitude values from a Keyhole Markup Language (KML) file using an almost 
purely functional approach by explicitly separating low-level XML parsing from higher-level data reorganization. '''

def split_at_comma(text):
    '''Returns a specific split for a string.  
    Maintain an syntactic uniformity with FP conventions, 
    instead of directly using the string split function.'''
    return text.split(',')

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
    # The XMl path in findall is case-sensitive, that is why the "coordinates" element is lowercase.
    # Instead of coordinate.text.split(',')  in the generator expression, we use our wrapper for uniform style.
    return (split_at_comma(coordinate.text)
        for coordinate in doc.findall('./ns0:Document/ns0:Folder/ns0:Placemark/ns0:Point/ns0:coordinates', ns_map))


def latitude_longitude_filter(longitude, latitude, altitude):
    '''Filter out the altitude data and swap the order of longitude and latitude.
    Maintains syntactic uniformity with FP conventions when used in caller. '''
    return latitude, longitude


def latitude_longitude_iterator(row_iterator):
    '''Transform the low-level data to an higher-level application-specific data.'''
    # Use tuple unpacking (*row) for the row to get the three values
    return (latitude_longitude_filter(*row) for row in row_iterator)

def lat_lon_float_iterator(lat_lon_itr):
    return ((float(lat), float(lon)) for lat, lon in lat_lon_itr)
        
def main():
    with open('locations.xml') as source:
        coordinates = \
                    lat_lon_float_iterator(
                        latitude_longitude_iterator(
                            xml_tree_to_row_iterator(source)
                        )
                    )
        for coordinate in coordinates:
            print(coordinate)


if __name__ == '__main__':
    main()
    
