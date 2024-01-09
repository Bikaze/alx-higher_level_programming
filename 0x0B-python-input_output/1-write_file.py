#!/usr/bin/python3
"""This file contains the functions 'write_file()'"""


def write_file(filename="", text=""):
    """Writes a string to a text file and returns the
    number of characters written"""

    with open(filename, 'w', encoding='UTF-8') as data_file:
        return data_file.write(text)
