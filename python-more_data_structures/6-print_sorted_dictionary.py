#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_order = dict(sorted(a_dictionary.items()))
    for keys, values in dict_order.items():
        print(f"{keys}: {values}")
