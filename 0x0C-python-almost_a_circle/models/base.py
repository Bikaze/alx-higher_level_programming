#!/usr/bin/python3
"""This module contains the class 'Base'"""


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
