#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    compy_list = my_list.copy()
    if idx < 0:
        return my_list
    elif idx > len(my_list) - 1:
        return my_list
    else:
        compy_list[idx] = element
        return compy_list
