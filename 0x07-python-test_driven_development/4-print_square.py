#!/usr/bin/python3
"""
This module provides one function; 'print_square()'
>>> print_square(size=4)
####
####
####
####
"""


def print_square(size):
    """Takes one argument 'size', which is the size of the
    square matrix to be printed using the '#' characters
    """
    if (isinstance(size, float) and size < 0) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print('#', end='')
        print()
