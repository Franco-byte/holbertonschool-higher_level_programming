#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    noc_list = []
    for char in my_list:
        if char not in ('C', 'c'):
            noc_list.append(char)
    cadena = ''.join(noc_list)
    return cadena

def no_c(my_string):
    return "".join([c for c in my_string if c not in "cC"])
