#!/usr/bin/python3
"""This script adds all arguments to a Python list, and then saves them
to the file 'add_item.json"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


args = sys.argv[1:]
try:
    existing_matrix = load_from_json_file('add_item.json')
except FileNotFoundError:
    save_to_json_file(args, 'add_item.json')
else:
    save_to_json_file(existing_matrix + args, 'add_item.json')
