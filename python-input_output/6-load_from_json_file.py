#!/usr/bin/python3
'''
Learning to use json.load() to read and crete a python objet
'''


import json


def load_from_json_file(filename):
    '''
    Use .load to read and create
    '''
    with open(filename, "r") as f:
        return json.load(f)
