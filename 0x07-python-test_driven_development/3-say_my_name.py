#!/usr/bin/python3
"""
This module provides one function; 'say_my_name()'
>>> say_my_name(first_name, last_name)
My name is first_name last_name
"""


def say_my_name(first_name, last_name=""):
    """Takes two string arguments 'first_name' and 'last_name' which
    is optional and then prints 'My name is <first name> <last name>"""

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
