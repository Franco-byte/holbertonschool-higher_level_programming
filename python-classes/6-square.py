#!/usr/bin/python3
'''
Create a square
'''

class Square:
    '''
    Size anda position square defined
    '''
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()

        if self.position[1] > 0:
            for enter in range(self.position[1]):
                print()

        for row in range(self.size):
            if self.position[0] > 0:
                for space in range(self.position[0]):
                    print(" ", end='')
            for colum in range(self.size):
                print("#", end='')
            print()
