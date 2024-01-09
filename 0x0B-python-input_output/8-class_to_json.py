#!/usr/bin/python3
"""This file contains the definition of 'class_to_json(obj)' function
"""


def class_to_json(obj):
    """Returns the dictionary representation of an object attributes
    """

    return vars(obj)
