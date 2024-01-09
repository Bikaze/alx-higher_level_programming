#!/usr/bin/python3
"""This file contains the function 'save_to_json_file(my_obj, filename)'"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file, using a JSON representation"""

    with open(filename, 'w', encoding='UTF-8') as data_file:
        json.dump(my_obj, data_file)
