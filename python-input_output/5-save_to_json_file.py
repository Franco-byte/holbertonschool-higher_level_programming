#!/usr/bin/python3
'''
Learning to use json.dump() to write a file in JSON
'''


import json


def save_to_json_file(my_obj, filename):
    '''
    Write a file with json
    '''
    with open(filename, "w") as f:
        json.dump(my_obj, f)
