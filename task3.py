#!python3
"""
Create a function called perimeter()
The input is a list.
The return value is the sum of all the numbers in the list
added together
(2 points)
"""
def perimeter(sides=[]):
    y=0
    for x in sides:
        y+=x
    return y 