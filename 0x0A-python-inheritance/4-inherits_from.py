#!/usr/bin/python3
"""
inherits_from(obj, a_class)
"""


def inherits_from(obj, a_class):
    """Return 'True' if the object is an instance of the class that
    inherited from the specified class; otherwise 'False'"""

    return issubclass(type(obj), a_class) and type(obj) != a_class
