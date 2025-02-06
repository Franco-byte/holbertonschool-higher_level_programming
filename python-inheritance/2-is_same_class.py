#!/usr/bin/python3
'''
Funtion to compare instans and clses
'''


def is_same_class(obj, a_class):
    '''
    Return True if "obj" is a instance of "a_class", otherwise False
    '''
    return type(obj) is a_class
