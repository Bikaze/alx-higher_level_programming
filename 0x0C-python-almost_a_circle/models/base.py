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
        """Makes a list of dictionaries Json-stringified"""
        if list is not None and list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves a JSON string representation of list_objs to a file"""
        if list_objs is None:
            j_str = '[]'
        else:
            j_str = cls.to_json_string([obj.to_dictionary() for obj in
                                        list_objs])

        with open(f'{cls.__name__}.json', 'w') as file:
            file.write(j_str)
