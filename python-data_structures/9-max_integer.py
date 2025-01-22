#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        copy = my_list
        copy.sort(reverse=True)
        return copy[0]
