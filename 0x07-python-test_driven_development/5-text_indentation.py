#!/usr/bin/python3
"""
This module provides one function; 'text_indentation()'
prints a text with 2 new lines after each of these characters: . ? and :
"""


def text_indentation(text):
    """Takes one argument as text and then,
    prints the text with two new lines after these characters:
    '.', '?', ':'
    """

    sp_chars = ['.', '?', ':']

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in sp_chars:
        text = (i + '\n\n').join([phrase.strip() for phrase in text.split(i)])

    print(text)


if __name__ == "__main__":
    import doctest
    doctest.testfile("./tests/5-text_indentation.txt")
