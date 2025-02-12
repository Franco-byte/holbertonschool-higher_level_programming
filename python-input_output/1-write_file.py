#!/usr/bin/python3
'''
Write a a new file
'''


def write_file(filename="", text=""):
    '''
    Use a "w" to create a new file or overwrite it
    Use .write() to write in the file
    '''
    with open(filename, "w") as txt:
        return txt.write(text)
