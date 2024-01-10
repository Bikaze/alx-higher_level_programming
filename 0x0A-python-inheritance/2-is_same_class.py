#!/usr/bin/python3
"""
is_same_class(obj, a_class)
"""


def is_same_class(obj, a_class):
    """Return 'True' if the object is exactly an instance of the
    specified class; otherwise 'False'"""
    
    if a_class is not object:
        return isinstance(obj, a_class)
    else:
        return False
