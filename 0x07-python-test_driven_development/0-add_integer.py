"""
This module supplies one function, add_integer(), for example
>>> add_integer(2, 2)
4
"""


def add_integer(a, b=98):
    """Return the sum of two integers: a and b
        a and b must be integers or floats
    """

    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
