#!/usr/bin/python3
"""This file contains the function 'load_from_json_file(filename)'"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file"""

    with open(filename, 'r', encoding='UTF-8') as data_file:
        return json.load(data_file)
