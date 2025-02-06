#!/usr/bin/python3
'''
Funtion to compare subclass and clses
'''


def inherits_from(obj, a_class):
    '''
    Return True if "obj" is a subclass of "a_class", otherwise False
    '''
    return isinstance(obj, a_class) and type(obj) is not a_class
