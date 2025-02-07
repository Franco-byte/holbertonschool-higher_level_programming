#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
'''
Ineheting
'''


class Rectangle(BaseGeometry):
    '''
    Inherits
    '''
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
