#!/usr/bin/python3
def no_c(my_string):
    my_list = list(my_string)
    for char in my_list:
        if char == 'C':
            my_list.remove('C')
        if char == 'c':
            my_list.remove('c')
    cadena = ''.join(my_list)
    return cadena
