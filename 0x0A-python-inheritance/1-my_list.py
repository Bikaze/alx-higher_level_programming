#!/usr/bin/python3
"""
class MyList
"""


class MyList(list):
    """class MyList inherits from the built-in list class"""

    def print_sorted(self):
        print(sorted(self))
