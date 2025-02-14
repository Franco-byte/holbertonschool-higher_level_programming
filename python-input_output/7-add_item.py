#!/usr/bin/python3
'''
Use sys.argv
'''


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


import sys


filename = 'add_item.json'
save_to_json_file(sys.argv[1:], filename)
load_from_json_file(filename)
