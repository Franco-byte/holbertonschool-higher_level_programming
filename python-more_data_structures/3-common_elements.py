#!/usr/bin/python3
def common_elements(set_1, set_2):
    for elemnt in set_1:
        if elemnt in set_2:
            return elemnt
    return 0