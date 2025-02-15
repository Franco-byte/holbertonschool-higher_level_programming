#!/usr/bin/python3
'''
Create a Student
'''


class Student:
    '''
    This is a student :D
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        result = {}
        for key in attrs:
            if hasattr(self, key):
                result[key] = getattr(self, key)
        return result
