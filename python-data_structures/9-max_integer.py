#!/usr/bin/python3
def max_integer(my_list=[]):
    copy = my_list
    copy.sort(reverse=True)
    return copy[0] 
