#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    final_set = set_1.union(set_2)
    for repeat in set_1:
        if repeat in set_2:
            final_set.remove(repeat)
    return final_set
