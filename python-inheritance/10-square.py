#!/usr/bin/python3
'''
Square inherated to Rectangle
'''


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Create a Square
    '''
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
