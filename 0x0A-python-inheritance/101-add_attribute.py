#!/usr/bin/python3
"""
add_attribute()
"""


def add_attribute(obj, name, value):
    """Adds a new attribute to an object if it's possible"""

    if hasattr(obj, "__dict__") or (hasattr(obj, "__slots__") and name in obj.__slots__):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
