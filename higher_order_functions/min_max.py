'''
Created on Dec 19, 2015

@author: Sameer Adhikari
'''

# Examples demonstrating the use of max and min as a higher-order function.

def getx(point):
    x, y, z = point
    return x

def gety(point):
    x, y, z = point
    return y

def getz(point):
    x, y, z = point
    return z

# The pattern in these points is to get distinct answers for max and min in each dimension
points3D = [(1, 5, 9), (4, 8, 3), (7, 2, 6)]

print('Points = {}'.format(points3D))

print(64*'-')
print('Defined function used in key')
print('Point max x = {}'.format(max(points3D, key=getx)))
print('Point max y = {}'.format(max(points3D, key=gety)))
print('Point max z = {}'.format(max(points3D, key=getz)))
print('Point min x = {}'.format(min(points3D, key=getx)))
print('Point min y = {}'.format(min(points3D, key=gety)))
print('Point min z = {}'.format(min(points3D, key=getz)))

print(64*'-')
print('Lambda form used in key')
print('Point max x = {}'.format(max(points3D, key=lambda point: point[0])))
print('Point max y = {}'.format(max(points3D, key=lambda point: point[1])))
print('Point max y = {}'.format(max(points3D, key=lambda point: point[2])))
print('Point min x = {}'.format(min(points3D, key=lambda point: point[0])))
print('Point min y = {}'.format(min(points3D, key=lambda point: point[1])))
print('Point min y = {}'.format(min(points3D, key=lambda point: point[2])))


