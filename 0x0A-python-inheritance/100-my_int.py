#!/usr/bin/python3
"""
class MyInt()
"""


class MyInt(int):
    """Class representing a subclass of class int"""

    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value != other
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, int):
            return self.value == other
        else:
            return False
