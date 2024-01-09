#!/usr/bin/python3
"""This file contains the function 'append_write()'"""


def append_write(filename="", text=""):
    """Appends a string at the end of the text file"""

    with open(filename, 'a', encoding="UTF-8") as data_file:
        return data_file.write(text)
