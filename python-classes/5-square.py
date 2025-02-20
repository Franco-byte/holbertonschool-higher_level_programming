#!/usr/bin/python3
'''
Create a square
'''


class Square:
    '''
    Print area with "#"
    '''
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()

        for row in range(self.size):
            for repeat in range(self.size):
                print("#", end='')
            print()
