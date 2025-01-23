#!/usr/bin/python3
def uniq_add(my_list=[]):
    if not my_list:
        return 0
    my_list.sort()
    result = my_list[0]
    for num in range(len(my_list) - 1):
        if my_list[num] < my_list[num + 1]:
            result += my_list[num + 1]
    return result
