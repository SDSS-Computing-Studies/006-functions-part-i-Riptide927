#!python3

"""
Create a function called distance()
Input is 2 tuples, that each contain an (x,y) coordinate.
Return value is the distance between the (x,y) coordinates.
Note that the coordinates should be signed (positive or negative) floats
(2 points)
"""
import math
def distance(x,y):
    z = x[0] - y[0]
    n = x[1] - y[1]
    return math.sqrt(n**2 + z**2)