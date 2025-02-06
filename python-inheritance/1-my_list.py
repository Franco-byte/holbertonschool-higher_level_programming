#!/usr/bin/python3
'''
Inherits the class list to print the sorted list
'''


class MyList(list):
    '''
    Print the sorted list
    '''
    def print_sorted(self):
        print(sorted(self))
