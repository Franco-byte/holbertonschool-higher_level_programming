#!/usr/bin/python3
'''
Read a file text
'''


def read_file(filename=""):
    '''
    Read "filename" and print it
    '''
    if filename == "":
        return

    with open(filename, "r") as text:
        print(text.read(), end='')
