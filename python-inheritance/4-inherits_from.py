#!/usr/bin/python3
'''
Funtion to compare subclass and clses
'''


def inherits_from(obj, a_class):
    '''
    Return True if "obj" is a subclass of "a_class", otherwise False
    '''
    return issubclass(obj, a_class)
