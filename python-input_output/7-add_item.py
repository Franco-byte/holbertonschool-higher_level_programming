#!/usr/bin/python3
'''
Use sys.argv
'''

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'
try:
    word = load_from_json_file(filename)
except FileNotFoundError:
    word = []

word.extend(sys.argv[1:])
save_to_json_file(word, filename)
