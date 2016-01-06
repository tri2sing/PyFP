'''
Created on Jan 5, 2016

@author: Sameer Adhikari
'''

from collections import namedtuple

# To access elements in tuples requires working with indexes. 
# Consider the following constructs: segment, point, dimension.
# A point consists of two dimensions (x, y).
# A segment consists of two points (start, end).

point1 = (3, 8)
point2 = (10, 5)
segmt1 = (point1, point2)

print('='*80)
print('Start Point = {}, End Point = {}, Segment = {}'.format(point1, point2, segmt1))

print('='*80)
print('Approach 1')
print('end point x coordinate using index notation point[0] = {}'.format(point2[0]))
print('segment start point y coordinate using index notation segment[0][1] = {}'.format(segmt1[0][1]))

# The index approach works but lacks clarity, especially when part of a large module.
# Using lambdas we can conceal the use of indexes and make this more readable.
# The lambda approach allows us to use prefix notation to refer to a specific data.

start = lambda segement: segement[0]
end = lambda segement: segement[1] 
xdim = lambda point: point[0]
ydim = lambda point: point[1]

print('='*80)
print('Approach 2')
print('end point x coordinate using lambda-based prefix notation xdim(point) = {}'.format(xdim(point2)))
print('segment start point y coordinate using lambda-based prefix notation ydim(point(segment) = {}'.format(ydim(start(segmt1))))


# An alternate lambda approach is to use the tuple unpacking to hide use of indexes.
# As this is an example, primarily for demonstration, we will redefine the lambdas.

start = lambda start, end: start
end = lambda start, end: end
xdim = lambda x, y: x
ydim = lambda x, y: y

print('='*80)
print('Approach 3')
print('end point x coordinate using lambda-based tuple unpacking xdim(*point) = {}'.format(xdim(*point2)))
print('segment start point y coordinate using lamda-based tuple unpacking ydim(*point(*segment) = {}'.format(ydim(*start(*segmt1))))

# Another approach is to use a namedtuple instead of a regular tuple.
# The namedtuple allows us to use suffix notation to access specific attributes.
# Visually the suffix notation does not mesh with the FP style as well as the prefix notation.
# As this is an example, primarily for demonstration, we will redefine the variables.

Point = namedtuple('Point', ('xdim', 'ydim'))
Segment = namedtuple('Segment', ('start', 'end'))
point1 = Point(3, 8)
point2 = Point(10, 5)
segmt1 = Segment(point1, point2)

print('='*80)
print('Start Point = {}, End Point = {}, \nSegment = {}'.format(point1, point2, segmt1))

print('='*80)
print('Approach 4')
print('end point x coordinate using namedtuple-based suffix notation point.xdim = {}'.format(point2.xdim))
print('segment start point y coordinate using namedtuple-based suffix notation segement.start.ydim = {}'.format(segmt1.start.ydim))



print('='*80)