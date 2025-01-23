#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    final_list = []
    for row in matrix:
        num_squered = list(map(lambda num: num ** 2, row))
        final_list.append(num_squered)
    return final_list
