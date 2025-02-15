#!/usr/bin/python3
'''
Pascal' triangle
'''


def pascal_triangle(n):
    '''
    how to create a pascal'triangle
    '''
    triangle = [[1], [1, 1]]
    prev_row = [1, 1]
    new_row = [1]
    n = n - 2

    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    if n <= 0:
        return []
    
    for row in range(n):
        new_row = [1]
        for i in range(len(prev_row) - 1):
            new_row.append(prev_row[i] + prev_row[i + 1])
        new_row.append(1)
        triangle.append(new_row)
        prev_row = new_row
    
    return triangle
