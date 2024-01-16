#!/usr/bin/python3
"""This module contains the class 'Base'"""

import json


class Base:
    """This is the base class for models"""

    # private class attribute
    __nb_objects = 0

    def __init__(self, id=None):
        """This is the constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries=None):
        if list is not None:
            return json.dumps(list_dictionaries)
        else:
            return '[]'
