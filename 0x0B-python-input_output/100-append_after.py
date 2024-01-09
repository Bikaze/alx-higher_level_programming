#!/usr/bin/python3
"""
append_after() function
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string
    """

    with open(filename, 'r', encoding='utf-8') as f:
        data = f.readlines()

    new_text = ""
    for sentence in data:
        if search_string in sentence:
            new_text += sentence + new_string
        else:
            new_text += sentence

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_text)
