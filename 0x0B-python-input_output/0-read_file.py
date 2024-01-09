#!/usr/bin/python3
"""Module contains the 'read_file' function"""


def read_file(filename=""):
    """Reads a text file(UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as data_file:
        for line in  data_file:
            print(line, end="")
