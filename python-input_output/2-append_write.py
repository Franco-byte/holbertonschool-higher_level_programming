#!/usr/bin/python3
'''
Learning to use open() function and modes
'''


def append_write(filename="", text=""):
    '''
    Use "a+" mode option to add a str in a file
    '''
    with open(filename, "a+") as f:
        return f.write(text)
