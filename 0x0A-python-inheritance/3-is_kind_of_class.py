#!/usr/bin/python3
"""
is_kind_of_class(obj, a_class)
"""


def is_kind_of_class(obj, a_class):
    """Return 'True' if the object is an instance of the
    specified class; otherwise 'False'"""

    return isinstance(obj, a_class)
