#!/usr/bin/python3
"""This file contains the function 'from_json_string(my_str)"""
import json


def from_json_string(my_str):
    """Returns the object representation by a JSON string"""

    return json.loads(my_str)
