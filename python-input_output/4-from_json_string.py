#!/usr/bin/python3
'''
Learning to use json.loads() to traslate
'''


import json


def from_json_string(my_str):
    '''
    Traslate JSON to objet
    '''
    return json.loads(my_str)
